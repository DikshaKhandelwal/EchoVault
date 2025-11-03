import os
import time
from typing import Dict, List, Tuple

from storage import get_all


SUPPORTED_EXTS = {".txt", ".md", ".pdf", ".docx"}


def scan_folder(folder: str) -> List[Tuple[str, float]]:
    results: List[Tuple[str, float]] = []
    for root, _, files in os.walk(folder):
        for f in files:
            if os.path.splitext(f)[1].lower() in SUPPORTED_EXTS:
                p = os.path.join(root, f)
                try:
                    results.append((p, os.path.getmtime(p)))
                except OSError:
                    pass
    return results
def diff_with_db(folder: str) -> Dict[str, List[str]]:
    on_disk = {p: m for p, m in scan_folder(folder)}
    in_db = {r["path"]: r for r in get_all()}
    to_add = [p for p in on_disk.keys() if p not in in_db]
    to_update = [p for p, m in on_disk.items() if p in in_db and m > (in_db[p]["last_modified"] or 0)]
    to_remove = [p for p in in_db.keys() if p not in on_disk]
    return {"add": to_add, "update": to_update, "remove": to_remove}
def suggest_archive(days: int = 60) -> List[str]:
    now = time.time()
    candidates: List[str] = []
    for r in get_all():
        last_used = r["last_used"] or r["last_modified"] or 0
        age_days = (now - last_used) / 86400.0
        if age_days >= days:
            candidates.append(r["path"])
    return candidates


def age_files_for_demo(pattern: str = "old_projects", days: int = 90):
    """Demo helper: artificially age matching files in database"""
    from storage import get_conn
    cutoff = time.time() - (days * 86400)
    conn = get_conn()
    for r in get_all():
        if pattern in r["path"]:
            conn.execute("UPDATE files SET last_used=?, last_modified=? WHERE path=?", 
                        (cutoff, cutoff, r["path"]))
    conn.commit()
    conn.close()

