"""
Planner Agent Implementation (Pattern 2: Task Decomposition & Planning)
Location: src/agents/planner_agent.py & src/patterns/planner.py
Model: Groq / OpenRouter (llama-3.3-70b-versatile) for structured task breakdown
"""
import json
from typing import Dict, Any, List
from .base_agent import BaseAgent
from src.protocols.message import MessageType

class PlannerAgent(BaseAgent):
    def __init__(self, message_bus, llm_factory):
        super().__init__(
            name="PlannerAgent",
            role="Strategic Decomposition & Workflow Planner",
            message_bus=message_bus,
            llm_factory=llm_factory,
            model_name="llama-3.3-70b-versatile"
        )

    def process(self, query: str, context: Any = None) -> Dict[str, Any]:
        category = context.get("category", "MULTI_STEP_ADVISORY") if context else "MULTI_STEP_ADVISORY"
        
        system_prompt = (
            "You are the Planning Agent for AgriLanka Intelligence.\n"
            "Decompose the user's agricultural advisory query into sequential sub-tasks for specialist workers.\n"
            "Respond strictly in valid JSON format with array of plan_steps:\n"
            '{"plan_steps": ['
            '{"step_id": 1, "task": "Query FAISS vector store for SLS standards and EU MRL rules.", "assigned_agent": "ComplianceSpecialist", "tool": "FAISS_Vector_RAG"},'
            '{"step_id": 2, "task": "Calculate tariff, Cess tax, and net realizable FOB export value.", "assigned_agent": "ComplianceSpecialist", "tool": "Export_Duty_Calculator"},'
            '{"step_id": 3, "task": "Assess pest diagnostic and soil suitability.", "assigned_agent": "CropCareSpecialist", "tool": "Pest_Diagnostic_Tool"}'
            ']}'
        )

        prompt = f"Category: {category}\nQuery: {query}"
        response = self.llm_factory.invoke(
            model=self.model_name,
            prompt=prompt,
            system_prompt=system_prompt,
            temperature=0.2
        )

        try:
            parsed = json.loads(response["content"])
        except Exception:
            parsed = {
                "plan_steps": [
                    {"step_id": 1, "task": f"Retrieve domain knowledge for query category: {category}", "assigned_agent": "ComplianceSpecialist", "tool": "FAISS_Vector_RAG"},
                    {"step_id": 2, "task": "Perform export tariff and incentive evaluation", "assigned_agent": "ComplianceSpecialist", "tool": "Export_Duty_Calculator"},
                    {"step_id": 3, "task": "Synthesize pest management and agronomic advisory", "assigned_agent": "CropCareSpecialist", "tool": "Pest_Diagnostic_Tool"}
                ]
            }

        self.send_message(
            recipient="OrchestratorWorker",
            message_type=MessageType.PLANNING,
            content=f"Generated {len(parsed.get('plan_steps', []))} execution steps.",
            payload=parsed
        )

        return parsed
