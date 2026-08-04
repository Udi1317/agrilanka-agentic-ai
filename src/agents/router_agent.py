"""
Router Agent Implementation (Pattern 1: Intent Triage Router)
Location: src/agents/router_agent.py & src/patterns/router.py
Model: Groq (llama-3.1-8b-instant) for low latency
"""
import json
from typing import Dict, Any
from .base_agent import BaseAgent
from src.protocols.message import MessageType

class RouterAgent(BaseAgent):
    def __init__(self, message_bus, llm_factory):
        super().__init__(
            name="RouterAgent",
            role="Intent Classification & Triage Specialist",
            message_bus=message_bus,
            llm_factory=llm_factory,
            model_name="llama-3.1-8b-instant"
        )

    def process(self, query: str, context: Any = None) -> Dict[str, Any]:
        system_prompt = (
            "You are the Intent Routing Agent for AgriLanka Intelligence.\n"
            "Classify the user's query into ONE of the following categories:\n"
            "- EXPORT_COMPLIANCE (SLS standards, MRL regulations, tariffs, Cess tax, customs procedures)\n"
            "- AGRI_DIAGNOSIS (Pests, diseases, soil pH, fertilizer, yield optimization)\n"
            "- CLIMATE_SUITABILITY (Agro-ecological zones, rainfall, land suitability)\n"
            "- MULTI_STEP_ADVISORY (Complex requests involving both export standards and farming practices)\n\n"
            "Respond strictly with valid JSON format:\n"
            '{"category": "...", "priority": "HIGH", "reasoning": "...", "target_specialists": ["..."]}'
        )

        response = self.llm_factory.invoke(
            model=self.model_name,
            prompt=f"User Query: {query}",
            system_prompt=system_prompt,
            temperature=0.1
        )

        try:
            parsed = json.loads(response["content"])
        except Exception:
            parsed = {
                "category": "MULTI_STEP_ADVISORY",
                "priority": "HIGH",
                "reasoning": "Defaulting to multi-step advisory workflow.",
                "target_specialists": ["Export Compliance Specialist", "Crop Care Specialist"]
            }

        # Send structured agent message
        self.send_message(
            recipient="PlannerAgent",
            message_type=MessageType.ROUTING,
            content=f"Categorized query as [{parsed['category']}]",
            payload=parsed
        )

        return parsed
