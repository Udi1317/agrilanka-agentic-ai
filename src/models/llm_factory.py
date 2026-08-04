"""
LLM Factory & Strategy Implementation
Handles OpenRouter, Groq, and Fallback Mock model invocations using standard library urllib as fallback.
"""
import os
import json
import time
import urllib.request
import urllib.error
from typing import Dict, Any, Optional

class ModelProvider:
    GROQ = "groq"
    OPENROUTER = "openrouter"
    MOCK = "mock"

class LLMFactory:
    def __init__(self, groq_api_key: Optional[str] = None, openrouter_api_key: Optional[str] = None):
        self.groq_key = groq_api_key or os.getenv("GROQ_API_KEY", "")
        self.openrouter_key = openrouter_api_key or os.getenv("OPENROUTER_API_KEY", "")

    def invoke(self, model: str, prompt: str, system_prompt: str = "You are an expert AI assistant.", temperature: float = 0.2) -> Dict[str, Any]:
        start_time = time.time()
        
        # Groq Invocation
        if self.groq_key:
            result = self._call_groq(model, prompt, system_prompt, temperature)
            if result:
                result["latency_ms"] = int((time.time() - start_time) * 1000)
                return result

        # OpenRouter Invocation
        if self.openrouter_key:
            result = self._call_openrouter(model, prompt, system_prompt, temperature)
            if result:
                result["latency_ms"] = int((time.time() - start_time) * 1000)
                return result

        # Fallback Mock / Offline Mode
        result = self._call_mock(model, prompt, system_prompt)
        result["latency_ms"] = int((time.time() - start_time) * 1000)
        return result

    def _call_groq(self, model_name: str, prompt: str, system_prompt: str, temperature: float) -> Optional[Dict[str, Any]]:
        if not self.groq_key:
            return None
        clean_model = "llama-3.1-8b-instant" if "8b" in model_name else "llama-3.3-70b-versatile"
        try:
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {self.groq_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": clean_model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                "temperature": temperature
            }
            req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
            with urllib.request.urlopen(req, timeout=12) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    content = data["choices"][0]["message"]["content"]
                    tokens = data.get("usage", {}).get("total_tokens", 0)
                    return {
                        "content": content,
                        "provider": "Groq",
                        "model": clean_model,
                        "tokens_used": tokens
                    }
        except Exception as e:
            print(f"Groq API error: {e}")
        return None

    def _call_openrouter(self, model_name: str, prompt: str, system_prompt: str, temperature: float) -> Optional[Dict[str, Any]]:
        if not self.openrouter_key:
            return None
        clean_model = "meta-llama/llama-3.3-70b-instruct" if "llama" in model_name else "anthropic/claude-3.5-sonnet"
        try:
            url = "https://openrouter.ai/api/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {self.openrouter_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://agrilanka-agentic.streamlit.app",
                "X-Title": "AgriLanka Agentic AI"
            }
            payload = {
                "model": clean_model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                "temperature": temperature
            }
            req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
            with urllib.request.urlopen(req, timeout=15) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    content = data["choices"][0]["message"]["content"]
                    tokens = data.get("usage", {}).get("total_tokens", 0)
                    return {
                        "content": content,
                        "provider": "OpenRouter",
                        "model": clean_model,
                        "tokens_used": tokens
                    }
        except Exception as e:
            print(f"OpenRouter API error: {e}")
        return None

    def _call_mock(self, model_name: str, prompt: str, system_prompt: str) -> Dict[str, Any]:
        prompt_lower = prompt.lower()
        system_lower = system_prompt.lower()
        
        if "router" in system_lower or "triage" in system_lower:
            category = "EXPORT_COMPLIANCE" if any(w in prompt_lower for w in ["export", "cinnamon", "mrl", "duty", "sls"]) else "AGRI_DIAGNOSIS"
            content = json.dumps({
                "category": category,
                "priority": "HIGH",
                "reasoning": "Query involves Sri Lankan spice export standards, MRL compliance, or crop protection.",
                "target_specialists": ["Export Compliance Specialist", "Crop Care Specialist"]
            })
        elif "planner" in system_lower:
            content = json.dumps({
                "query": prompt[:80],
                "plan_steps": [
                    {"step_id": 1, "task": "Query FAISS vector store for SLS standards and EU/US MRL compliance rules.", "assigned_agent": "ComplianceSpecialist", "tool": "FAISS_Vector_RAG"},
                    {"step_id": 2, "task": "Calculate tariff, Cess levies, and export incentives.", "assigned_agent": "ComplianceSpecialist", "tool": "Export_Duty_Calculator"},
                    {"step_id": 3, "task": "Evaluate agronomic recommendations and pest management.", "assigned_agent": "CropCareSpecialist", "tool": "Pest_Diagnostic_Tool"}
                ]
            })
        elif "critic" in system_lower or "reflection" in system_lower:
            content = json.dumps({
                "is_approved": True,
                "score": 95,
                "feedback": "Verified compliance with SLS 81 / SLS 105 standards and EU MRL regulations. NPQS certification highlighted.",
                "missing_elements": []
            })
        else:
            content = (
                "### 🇱🇰 AgriLanka Expert Advisory Report\n\n"
                "**1. Export Compliance & SLS Quality Standards:**\n"
                "- Under **SLS 81 (Ceylon Cinnamon Specification)**, moisture content must not exceed 15.0% and volatile oil must be >= 1.0%.\n"
                "- Coumarin level is strictly capped at < 0.004% (40 mg/kg) to verify True Ceylon Cinnamon authenticity.\n"
                "- EU Regulation (EC) No 396/2005 requires Pre-Harvest Interval (PHI) of 21 days for agrochemicals with Glyphosate residue < 2.0 mg/kg.\n\n"
                "**2. Export Duties & Tax Incentives:**\n"
                "- Exporting retail packs (< 1kg) is exempt from Export Cess (0%) and eligible for 5% EDB Export Development Grants.\n"
                "- Mandatory documentation includes Commercial Invoice, Packing List, Phytosanitary Certificate from NPQS, and Certificate of Origin.\n\n"
                "**3. Agronomic & Pest Management:**\n"
                "- Observe proper solar drying techniques to prevent Aflatoxin contamination.\n"
                "- Apply organic Neem seed kernel emulsion for pest control."
            )

        return {
            "content": content,
            "provider": "Demo Engine (Offline)",
            "model": f"{model_name} (Simulated)",
            "tokens_used": len(prompt.split()) + len(content.split())
        }
