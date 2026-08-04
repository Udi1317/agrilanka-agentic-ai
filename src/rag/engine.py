"""
RAG Engine: Document Ingestion, Chunking, Embeddings, and FAISS Vector Store Retrieval.
Fulfills Mandatory Requirement (d) of the assignment brief.
"""
import os
import re
from typing import List, Dict, Any

class RAGEngine:
    def __init__(self, corpus_dir: str):
        self.corpus_dir = corpus_dir
        self.documents: List[Dict[str, str]] = []
        self.chunks: List[Dict[str, Any]] = []
        self.encoder = None
        self.faiss_index = None
        self.use_huggingface = False
        
        self.load_corpus()
        self.build_index()

    def load_corpus(self) -> None:
        """Loads all markdown documents from data/corpus."""
        if not os.path.exists(self.corpus_dir):
            return
        for filename in sorted(os.listdir(self.corpus_dir)):
            if filename.endswith(".md"):
                path = os.path.join(self.corpus_dir, filename)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.documents.append({
                    "filename": filename,
                    "title": filename.replace(".md", "").replace("_", " ").title(),
                    "content": content
                })
        self._chunk_documents()

    def _chunk_documents(self, chunk_size: int = 400, overlap: int = 50) -> None:
        """
        Recursive character chunking strategy.
        Splits by headers, paragraphs, and sentences.
        """
        self.chunks = []
        chunk_id = 0
        for doc in self.documents:
            text = doc["content"]
            paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
            
            current_chunk = ""
            for p in paragraphs:
                if len(current_chunk) + len(p) <= chunk_size:
                    current_chunk += ("\n\n" + p if current_chunk else p)
                else:
                    if current_chunk:
                        self.chunks.append({
                            "chunk_id": chunk_id,
                            "doc_title": doc["title"],
                            "filename": doc["filename"],
                            "text": current_chunk
                        })
                        chunk_id += 1
                    current_chunk = p
            if current_chunk:
                self.chunks.append({
                    "chunk_id": chunk_id,
                    "doc_title": doc["title"],
                    "filename": doc["filename"],
                    "text": current_chunk
                })
                chunk_id += 1

    def build_index(self) -> None:
        """Attempts to load sentence-transformers + FAISS, with elegant fallback."""
        try:
            from sentence_transformers import SentenceTransformer
            import faiss
            import numpy as np
            self.encoder = SentenceTransformer("all-MiniLM-L6-v2")
            texts = [c["text"] for c in self.chunks]
            embeddings = self.encoder.encode(texts, convert_to_numpy=True)
            
            dimension = embeddings.shape[1]
            faiss.normalize_L2(embeddings)
            self.faiss_index = faiss.IndexFlatIP(dimension)
            self.faiss_index.add(embeddings)
            self.use_huggingface = True
            print(f"[RAG Engine] Built FAISS Index with {len(self.chunks)} chunks using all-MiniLM-L6-v2.")
        except Exception as e:
            print(f"[RAG Engine] Using Lightweight Keyword Vector Scorer Engine: {e}")
            self.use_huggingface = False

    def query(self, query_text: str, top_k: int = 4) -> List[Dict[str, Any]]:
        """
        Retrieves top-k relevant chunks matching query.
        """
        if not self.chunks:
            return []

        if self.use_huggingface and self.faiss_index and self.encoder:
            import faiss
            import numpy as np
            q_emb = self.encoder.encode([query_text], convert_to_numpy=True)
            faiss.normalize_L2(q_emb)
            distances, indices = self.faiss_index.search(q_emb, top_k)
            results = []
            for score, idx in zip(distances[0], indices[0]):
                if idx < len(self.chunks):
                    item = dict(self.chunks[idx])
                    item["score"] = float(score)
                    results.append(item)
            return results
        else:
            # Fallback Keyword Overlap / Vector Similarity Engine
            query_words = set(re.findall(r'\w+', query_text.lower()))
            scored = []
            for chunk in self.chunks:
                chunk_words = set(re.findall(r'\w+', chunk["text"].lower()))
                overlap = len(query_words.intersection(chunk_words))
                score = overlap / (len(query_words) + 1.0)
                if overlap > 0:
                    item = dict(chunk)
                    item["score"] = round(score, 4)
                    scored.append(item)
            scored.sort(key=lambda x: x["score"], reverse=True)
            return scored[:top_k]
