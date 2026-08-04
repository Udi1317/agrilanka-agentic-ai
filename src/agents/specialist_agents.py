"""
Domain Specialist Worker Agents (Pattern 3: Orchestrator-Worker & ReAct Tool Use)
Location: src/agents/specialist_agents.py & src/patterns/orchestrator.py
Model: OpenRouter / Groq (meta-llama/llama-3.3-70b-instruct)
"""
from typing import Dict, Any, List
from .base_agent import BaseAgent
from src.protocols.message import MessageType
from src.tools.export_duty_calculator import calculate_export_duty
from src.tools.climate_suitability import evaluate_climate_suitability
from src.tools.pest_diagnostic_tool import diagnose_pest

class ComplianceSpecialistAgent(BaseAgent):
    def __init__(self, message_bus, llm_factory, rag_engine):
        super().__init__(
            name="ComplianceSpecialist",
            role="Sri Lanka SLS Standards & EU Export Compliance Officer",
            message_bus=message_bus,
            llm_factory=llm_factory,
            model_name="meta-llama/llama-3.3-70b-instruct"
        )
        self.rag_engine = rag_engine

    def process(self, query: str, context: Any = None) -> Dict[str, Any]:
        # 1. Execute FAISS Vector RAG Tool
        retrieved_chunks = self.rag_engine.query(query, top_k=3)
        context_str = "\n---\n".join([f"[{c['doc_title']}]\n{c['text']}" for c in retrieved_chunks])
        
        # Notify Tool Execution via Message Protocol
        self.send_message(
            recipient="Orchestrator",
            message_type=MessageType.TOOL_EXECUTION,
            content=f"Executed FAISS Vector RAG Tool. Retrieved {len(retrieved_chunks)} domain context chunks.",
            payload={"tool": "FAISS_Vector_RAG", "chunks_count": len(retrieved_chunks)}
        )

        # 2. Execute Export Duty Calculator Tool if applicable
        tariff_data = {}
        if any(w in query.lower() for w in ["cinnamon", "pepper", "tea", "export", "duty", "cess"]):
            crop = "cinnamon" if "cinnamon" in query.lower() else "pepper" if "pepper" in query.lower() else "tea"
            pkg = "retail" if "retail" in query.lower() or "pack" in query.lower() else "bulk"
            tariff_data = calculate_export_duty(crop, quantity_kg=1000, package_type=pkg)
            
            self.send_message(
                recipient="Orchestrator",
                message_type=MessageType.TOOL_EXECUTION,
                content=f"Executed Export Duty Calculator for {crop} ({pkg}). Net Value: ${tariff_data['net_realizable_value_usd']}",
                payload={"tool": "Export_Duty_Calculator", "result": tariff_data}
            )

        # Synthesis Prompt
        system_prompt = (
            "You are the Export Compliance Specialist for AgriLanka Intelligence.\n"
            "Use the provided retrieved domain knowledge and tariff calculation to write detailed technical compliance advice."
        )
        prompt = f"User Query: {query}\n\nRetrieved Knowledge:\n{context_str}\n\nTariff Data:\n{tariff_data}"
        
        response = self.llm_factory.invoke(
            model=self.model_name,
            prompt=prompt,
            system_prompt=system_prompt,
            temperature=0.2
        )

        output = {
            "specialist": self.name,
            "analysis": response["content"],
            "retrieved_docs": [c["filename"] for c in retrieved_chunks],
            "tariff_data": tariff_data
        }

        self.send_message(
            recipient="Orchestrator",
            message_type=MessageType.SUBTASK_RESPONSE,
            content=f"Completed export compliance analysis.",
            payload=output
        )

        return output

class CropCareSpecialistAgent(BaseAgent):
    def __init__(self, message_bus, llm_factory, rag_engine):
        super().__init__(
            name="CropCareSpecialist",
            role="Agronomist & Integrated Pest Management Specialist",
            message_bus=message_bus,
            llm_factory=llm_factory,
            model_name="meta-llama/llama-3.3-70b-instruct"
        )
        self.rag_engine = rag_engine

    def process(self, query: str, context: Any = None) -> Dict[str, Any]:
        # 1. Execute Pest Diagnostic Tool
        diagnostic_res = diagnose_pest(query)
        self.send_message(
            recipient="Orchestrator",
            message_type=MessageType.TOOL_EXECUTION,
            content=f"Executed Pest Diagnostic Tool. Match: {diagnostic_res['matched']}",
            payload={"tool": "Pest_Diagnostic_Tool", "result": diagnostic_res}
        )

        # 2. Execute Agro-Climate Suitability Tool
        climate_res = evaluate_climate_suitability("wet_zone", "cinnamon")
        
        # 3. Retrieve RAG Chunks
        retrieved_chunks = self.rag_engine.query(query, top_k=2)
        context_str = "\n---\n".join([f"[{c['doc_title']}]\n{c['text']}" for c in retrieved_chunks])

        system_prompt = (
            "You are the Lead Agronomist & Crop Care Specialist for AgriLanka Intelligence.\n"
            "Provide actionable agricultural guidelines, pest control, soil pH correction, and fertilizer recommendations."
        )
        prompt = f"User Query: {query}\n\nDiagnostic:\n{diagnostic_res}\n\nRetrieved Context:\n{context_str}"

        response = self.llm_factory.invoke(
            model=self.model_name,
            prompt=prompt,
            system_prompt=system_prompt,
            temperature=0.2
        )

        output = {
            "specialist": self.name,
            "analysis": response["content"],
            "diagnostic_data": diagnostic_res,
            "climate_data": climate_res
        }

        self.send_message(
            recipient="Orchestrator",
            message_type=MessageType.SUBTASK_RESPONSE,
            content=f"Completed agronomic & crop care synthesis.",
            payload=output
        )

        return output
