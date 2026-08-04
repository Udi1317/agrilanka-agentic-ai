"""
Structured Agent Message Protocol & Message Bus
Implements structured message exchange between autonomous agents using standard dataclasses.
Fulfills Pattern B: Agent-to-Agent Communication Protocol.
"""
import uuid
import datetime
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional

class MessageType:
    ROUTING = "ROUTING"
    PLANNING = "PLANNING"
    SUBTASK_REQUEST = "SUBTASK_REQUEST"
    SUBTASK_RESPONSE = "SUBTASK_RESPONSE"
    TOOL_EXECUTION = "TOOL_EXECUTION"
    CRITIQUE_REQUEST = "CRITIQUE_REQUEST"
    CRITIQUE_RESPONSE = "CRITIQUE_RESPONSE"
    FINAL_SYNTHESIS = "FINAL_SYNTHESIS"

@dataclass
class AgentMessage:
    sender: str
    recipient: str
    message_type: str
    content: str
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    payload: Dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3])
    correlation_id: Optional[str] = None

class MessageBus:
    """
    In-memory Agent Message Bus for recording, routing, and auditing structured agent communications.
    """
    def __init__(self):
        self.history: List[AgentMessage] = []

    def publish(self, message: AgentMessage) -> None:
        self.history.append(message)

    def get_messages(self, correlation_id: Optional[str] = None) -> List[AgentMessage]:
        if correlation_id:
            return [m for m in self.history if m.correlation_id == correlation_id]
        return self.history

    def clear(self) -> None:
        self.history.clear()

    def generate_sequence_diagram(self) -> str:
        """
        Generates Mermaid sequence diagram syntax representing the message flow.
        """
        lines = ["sequenceDiagram", "    autonumber"]
        participants = set()
        for msg in self.history:
            participants.add(msg.sender)
            participants.add(msg.recipient)
        
        for p in sorted(list(participants)):
            lines.append(f"    participant {p}")
            
        for msg in self.history:
            clean_content = msg.content.replace("\n", " ")[:40]
            lines.append(f"    {msg.sender}->>{msg.recipient}: [{msg.message_type}] {clean_content}...")
            
        return "\n".join(lines)
