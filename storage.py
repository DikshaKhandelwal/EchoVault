import json
import os
import sqlite3
import time
from typing import Any, Dict, List, Optional, Tuple


DB_PATH = os.path.join(os.getcwd(), "echovault.db")


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS files (
            path TEXT PRIMARY KEY,
            summary TEXT,
            embedding TEXT,          -- JSON-encoded list[float]
            last_modified REAL,
            last_used REAL,
            tags TEXT                -- comma-separated
        )
        """
    )
    return conn


def upsert_file(
    path: str,
    summary: str,
    embedding: List[float],
    last_modified: float,
    tags: Optional[List[str]] = None,
) -> None:
    conn = get_conn()
    tags_str = ",".join(tags) if tags else ""
    conn.execute(
        """
        INSERT INTO files(path, summary, embedding, last_modified, last_used, tags)
        VALUES(?, ?, ?, ?, ?, ?)
        ON CONFLICT(path) DO UPDATE SET
            summary=excluded.summary,
            embedding=excluded.embedding,
            last_modified=excluded.last_modified,
            tags=excluded.tags
        """,
        (path, summary, json.dumps(embedding), last_modified, time.time(), tags_str),
    )
    conn.commit()
    conn.close()


def update_last_used(path: str) -> None:
    conn = get_conn()
    conn.execute("UPDATE files SET last_used=? WHERE path=?", (time.time(), path))
    conn.commit()
    conn.close()


def get_all() -> List[Dict[str, Any]]:
    conn = get_conn()
    cur = conn.execute(
        "SELECT path, summary, embedding, last_modified, last_used, tags FROM files"
    )
    rows = cur.fetchall()
    conn.close()
    results: List[Dict[str, Any]] = []
    for p, s, e, lm, lu, t in rows:
        results.append(
            {
                "path": p,
                "summary": s,
                "embedding": json.loads(e) if e else [],
                "last_modified": lm,
                "last_used": lu,
                "tags": (t or "").split(",") if t else [],
            }
        )
    return results


def get_by_path(path: str) -> Optional[Dict[str, Any]]:
    conn = get_conn()
    cur = conn.execute(
        "SELECT path, summary, embedding, last_modified, last_used, tags FROM files WHERE path=?",
        (path,),
    )
    row = cur.fetchone()
    conn.close()
    if not row:
        return None
    p, s, e, lm, lu, t = row
    return {
        "path": p,
        "summary": s,
        "embedding": json.loads(e) if e else [],
        "last_modified": lm,
        "last_used": lu,
        "tags": (t or "").split(",") if t else [],
    }


def delete_by_path(path: str) -> None:
    conn = get_conn()
    conn.execute("DELETE FROM files WHERE path=?", (path,))
    conn.commit()
    conn.close()


def upsert_many(records: List[Tuple[str, str, List[float], float, List[str]]]) -> None:
    conn = get_conn()
    now = time.time()
    conn.executemany(
        """
        INSERT INTO files(path, summary, embedding, last_modified, last_used, tags)
        VALUES(?, ?, ?, ?, ?, ?)
        ON CONFLICT(path) DO UPDATE SET
            summary=excluded.summary,
            embedding=excluded.embedding,
            last_modified=excluded.last_modified,
            tags=excluded.tags
        """,
        [
            (p, s, json.dumps(e), lm, now, ",".join(t or []))
            for p, s, e, lm, t in records
        ],
    )
    conn.commit()
    conn.close()


def count() -> int:
    conn = get_conn()
    cur = conn.execute("SELECT COUNT(*) FROM files")
    n = int(cur.fetchone()[0])
    conn.close()
    return n

