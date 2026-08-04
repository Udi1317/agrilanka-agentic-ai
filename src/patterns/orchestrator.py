"""
Master Multi-Agent Orchestrator Pipeline
Orchestrates Router, Planner, Specialist Workers (ReAct Tool Use), and Critic Reflection Agents.
Fulfills Pattern Requirements:
1. Router Pattern (src/patterns/router.py)
2. Planning & Task Decomposition Pattern (src/patterns/planner.py)
3. Orchestrator-Worker & Tool-Use Pattern (src/patterns/orchestrator.py)
4. Reflection / Self-Critique Pattern (src/patterns/reflection.py)
"""
import time
from typing import Dict, Any, List
from src.protocols.message import MessageBus, AgentMessage, MessageType
from src.models.llm_factory import LLMFactory
from src.rag.engine import RAGEngine
from src.agents.router_agent import RouterAgent
from src.agents.planner_agent import PlannerAgent
from src.agents.specialist_agents import ComplianceSpecialistAgent, CropCareSpecialistAgent
from src.agents.critic_agent import CriticAgent

class MasterOrchestrator:
    def __init__(self, message_bus: MessageBus, llm_factory: LLMFactory, rag_engine: RAGEngine):
        self.message_bus = message_bus
        self.llm_factory = llm_factory
        self.rag_engine = rag_engine

        # Initialize Agents
        self.router = RouterAgent(message_bus, llm_factory)
        self.planner = PlannerAgent(message_bus, llm_factory)
        self.compliance_specialist = ComplianceSpecialistAgent(message_bus, llm_factory, rag_engine)
        self.crop_specialist = CropCareSpecialistAgent(message_bus, llm_factory, rag_engine)
        self.critic = CriticAgent(message_bus, llm_factory)

    def run_pipeline(self, user_query: str) -> Dict[str, Any]:
        """
        Executes the full multi-agent pipeline and records execution history.
        """
        self.message_bus.clear()
        start_time = time.time()

        # Step 1: Pattern 1 - Intent Router Triage
        routing_res = self.router.process(user_query)

        # Step 2: Pattern 2 - Planning & Task Decomposition
        plan_res = self.planner.process(user_query, context=routing_res)

        # Step 3: Pattern 3 - Orchestrator-Worker Execution & Tool Use
        compliance_out = self.compliance_specialist.process(user_query)
        crop_out = self.crop_specialist.process(user_query)

        # Combine Specialist Draft Synthesis
        draft_response = (
            f"## 🌿 AgriLanka Expert Advisory Report\n\n"
            f"### 📋 1. Export Compliance & Regulatory Standards\n"
            f"{compliance_out['analysis']}\n\n"
            f"### 🚜 2. Agronomic & Integrated Pest Management Advisory\n"
            f"{crop_out['analysis']}\n"
        )

        # Step 4: Pattern 4 - Reflection & Self-Critique
        critique_res = self.critic.process(user_query, context={"draft_response": draft_response})

        # Refine if critic suggests improvements
        final_response = draft_response
        if not critique_res.get("is_approved", True):
            final_response += f"\n\n> ⚠️ **Quality Control Note**: {critique_res.get('feedback', '')}"

        total_time_ms = int((time.time() - start_time) * 1000)

        return {
            "query": user_query,
            "routing": routing_res,
            "plan": plan_res,
            "compliance_out": compliance_out,
            "crop_out": crop_out,
            "critique": critique_res,
            "final_advisory": final_response,
            "total_execution_ms": total_time_ms,
            "message_history": self.message_bus.get_messages(),
            "sequence_diagram": self.message_bus.generate_sequence_diagram()
        }
