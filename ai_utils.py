import os
from typing import List, Tuple

import numpy as np
from openai import OpenAI


EMBED_MODEL = os.getenv("ECHOVAULT_EMBED_MODEL", "text-embedding-3-small")
GPT_MODEL = os.getenv("ECHOVAULT_GPT_MODEL", "gpt-4o-mini")


def _client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")
    return OpenAI(api_key=api_key)


def embed_text(text: str) -> List[float]:
    client = _client()
    text = text.strip().replace("\n", " ")[:6000]
    e = client.embeddings.create(model=EMBED_MODEL, input=text)
    return e.data[0].embedding


def summarize_text(text: str) -> Tuple[str, List[str]]:
    client = _client()
    prompt = (
        "Summarize the document in 4-6 concise bullet points. Also provide 2-4 high-level tags (single words)."
    )
    content = text[:4000]
    resp = client.chat.completions.create(
        model=GPT_MODEL,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content},
        ],
        temperature=0.2,
        max_tokens=300,
    )
    summary = resp.choices[0].message.content.strip()
    # Extract tags by asking embeddings on tag line or simple heuristic (last line starting with Tags:)
    tags: List[str] = []
    for line in summary.splitlines()[::-1]:
        if ":" in line and line.lower().startswith("tags"):
            tags = [t.strip().strip("-#*") for t in line.split(":", 1)[1].split(",")]
            break
    if not tags:
        # heuristic: pick top nouns via simple split (fallback)
        words = [w.strip(".,:;()[]{}!?") for w in content.split()[:100]]
        tags = sorted(set([w.lower() for w in words if w.istitle()]))[:4]
    return summary, tags


def cosine_sim(a: List[float], b: List[float]) -> float:
    va = np.array(a, dtype=np.float32)
    vb = np.array(b, dtype=np.float32)
    denom = (np.linalg.norm(va) * np.linalg.norm(vb))
    if denom == 0:
        return 0.0
    return float(np.dot(va, vb) / denom)


def chat_with_context(question: str, contexts: List[Tuple[str, str, str]]) -> str:
    """
    RAG-based Q&A using retrieved file contexts.
    contexts: List of (filename, summary, content_snippet)
    Returns: AI-generated answer with source citations
    """
    client = _client()
    
    # Build context from top retrieved files
    context_text = "\n\n".join([
        f"[Source: {fname}]\n{summary}\nContent: {content[:800]}"
        for fname, summary, content in contexts[:5]
    ])
    
    system_prompt = (
        "You are an intelligent assistant helping users find information in their files. "
        "Answer the question based ONLY on the provided file contexts. "
        "Always cite which file(s) you're referencing. "
        "If the answer isn't in the contexts, say so clearly."
    )
    
    user_prompt = f"QUESTION: {question}\n\nCONTEXTS:\n{context_text}"
    
    resp = client.chat.completions.create(
        model=GPT_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.3,
        max_tokens=500,
    )
    
    return resp.choices[0].message.content.strip()

