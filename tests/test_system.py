"""
Comprehensive Test Suite for AgriLanka Agentic AI
Tests:
1. RAG Corpus Ingestion & FAISS Vector Indexing
2. Structured Agent Message Protocol & Message Bus
3. Multi-Agent Pipeline Execution across all 4 Agentic Patterns
4. RAG Evaluation Suite with 5 Benchmark Queries
"""
import os
import sys

# Ensure root is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.protocols.message import MessageBus, AgentMessage, MessageType
from src.models.llm_factory import LLMFactory
from src.rag.engine import RAGEngine
from src.rag.evaluator import RAGEvaluator
from src.patterns.orchestrator import MasterOrchestrator
from src.tools.export_duty_calculator import calculate_export_duty

CORPUS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'corpus'))

def test_rag_corpus_loading():
    rag = RAGEngine(CORPUS_DIR)
    assert len(rag.documents) >= 20, f"Expected at least 20 corpus docs, got {len(rag.documents)}"
    assert len(rag.chunks) > 30, f"Expected >30 chunks, got {len(rag.chunks)}"
    print("[OK] RAG Corpus Loading Test Passed.")

def test_rag_retrieval_query():
    rag = RAGEngine(CORPUS_DIR)
    results = rag.query("Ceylon Cinnamon SLS 81 coumarin level", top_k=2)
    assert len(results) > 0
    assert "cinnamon" in results[0]["text"].lower()
    print("[OK] RAG Query Retrieval Test Passed.")

def test_rag_benchmark_evaluation():
    rag = RAGEngine(CORPUS_DIR)
    evaluator = RAGEvaluator(rag)
    results = evaluator.run_evaluations()
    assert len(results) == 5
    matches = sum(1 for r in results if r["is_match"])
    print(f"[OK] RAG Evaluation Test Passed. Success Rate: {matches}/5 queries matched expected docs.")
    assert matches >= 3

def test_export_duty_calculator():
    res = calculate_export_duty("cinnamon", quantity_kg=1000, package_type="retail")
    assert res["cess_levy_usd"] == 0.0
    assert res["edb_grant_usd"] > 0.0
    print("[OK] Export Duty Calculator Test Passed.")

def test_agent_message_bus():
    bus = MessageBus()
    msg = AgentMessage(
        sender="TestAgent",
        recipient="ReceiverAgent",
        message_type=MessageType.ROUTING,
        content="Testing message bus",
        payload={"key": "value"}
    )
    bus.publish(msg)
    history = bus.get_messages()
    assert len(history) == 1
    assert history[0].sender == "TestAgent"
    
    diagram = bus.generate_sequence_diagram()
    assert "sequenceDiagram" in diagram
    print("[OK] Agent Message Protocol & Bus Test Passed.")

def test_full_pipeline_execution():
    bus = MessageBus()
    llm = LLMFactory() # Uses fallback mock if no keys set
    rag = RAGEngine(CORPUS_DIR)
    orchestrator = MasterOrchestrator(bus, llm, rag)
    
    output = orchestrator.run_pipeline("What are the SLS 81 quality standards and EU MRL limits for Ceylon Cinnamon export?")
    assert "final_advisory" in output
    assert len(output["message_history"]) >= 4
    assert "sequence_diagram" in output
    print("[OK] Full Multi-Agent Pipeline Execution Test Passed.")

if __name__ == "__main__":
    test_rag_corpus_loading()
    test_rag_retrieval_query()
    test_rag_benchmark_evaluation()
    test_export_duty_calculator()
    test_agent_message_bus()
    test_full_pipeline_execution()
    print("\nALL AGENTIC AI SYSTEM TESTS PASSED SUCCESSFULLY!")
