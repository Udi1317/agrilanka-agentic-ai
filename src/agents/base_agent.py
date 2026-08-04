"""
Abstract Base Agent supporting Structured Inter-Agent Communication
Fulfills Pattern B: Agent-to-Agent Communication Protocol.
"""
from typing import Dict, Any, List, Optional
from src.protocols.message import AgentMessage, MessageBus, MessageType
from src.models.llm_factory import LLMFactory

class BaseAgent:
    def __init__(self, name: str, role: str, message_bus: MessageBus, llm_factory: LLMFactory, model_name: str = "llama-3.1-8b-instant"):
        self.name = name
        self.role = role
        self.message_bus = message_bus
        self.llm_factory = llm_factory
        self.model_name = model_name

    def send_message(self, recipient: str, message_type: str, content: str, payload: Optional[Dict[str, Any]] = None, correlation_id: Optional[str] = None) -> AgentMessage:
        msg = AgentMessage(
            sender=self.name,
            recipient=recipient,
            message_type=message_type,
            content=content,
            payload=payload or {},
            correlation_id=correlation_id
        )
        self.message_bus.publish(msg)
        return msg

    def process(self, query: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement process method.")
