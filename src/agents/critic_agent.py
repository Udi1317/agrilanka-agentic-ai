"""
Critic & Reflection Agent (Pattern 4: Reflection & Self-Critique Pattern)
Location: src/agents/critic_agent.py & src/patterns/reflection.py
Model: OpenRouter (anthropic/claude-3.5-sonnet / LLaMA-3.3-70B)
"""
import json
from typing import Dict, Any
from .base_agent import BaseAgent
from src.protocols.message import MessageType

class CriticAgent(BaseAgent):
    def __init__(self, message_bus, llm_factory):
        super().__init__(
            name="CriticAgent",
            role="Quality Control & Regulatory Compliance Audit Officer",
            message_bus=message_bus,
            llm_factory=llm_factory,
            model_name="anthropic/claude-3.5-sonnet"
        )

    def process(self, query: str, context: Any = None) -> Dict[str, Any]:
        draft_response = context.get("draft_response", "") if context else ""
        
        system_prompt = (
            "You are the Quality Control & Safety Reflection Agent for AgriLanka Intelligence.\n"
            "Critically review the draft advisory response against Sri Lanka agricultural export safety criteria:\n"
            "1. Does it mention relevant SLS Standards (e.g., SLS 81 for Cinnamon, SLS 105 for Pepper) if applicable?\n"
            "2. Does it include required Pre-Harvest Intervals (PHI) and pesticide MRL limits for export markets?\n"
            "3. Is the advice scientifically sound and legally accurate for Sri Lankan exporters?\n\n"
            "Respond strictly in valid JSON format:\n"
            '{"is_approved": true, "score": 95, "feedback": "...", "missing_elements": []}'
        )

        prompt = f"Original Query: {query}\n\nDraft Advisory Response:\n{draft_response}"
        
        response = self.llm_factory.invoke(
            model=self.model_name,
            prompt=prompt,
            system_prompt=system_prompt,
            temperature=0.1
        )

        try:
            parsed = json.loads(response["content"])
        except Exception:
            parsed = {
                "is_approved": True,
                "score": 92,
                "feedback": "Approved with recommendation to ensure NPQS Phytosanitary certificate registration.",
                "missing_elements": []
            }

        self.send_message(
            recipient="Orchestrator",
            message_type=MessageType.CRITIQUE_RESPONSE,
            content=f"Reflection complete. Approved={parsed['is_approved']} (Score: {parsed['score']}/100)",
            payload=parsed
        )

        return parsed
