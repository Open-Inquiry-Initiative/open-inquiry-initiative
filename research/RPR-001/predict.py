#!/usr/bin/env python3
"""Minimal dependency-readiness predictor. Standard library only; no trained AI."""
import datetime as dt
import json
import sys

def parse_time(value):
    value = value.replace("Z", "+00:00")
    parsed = dt.datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        raise ValueError("timestamps must contain timezone")
    return parsed.astimezone(dt.timezone.utc)

def rank(events, cutoff):
    ids = [e["id"] for e in events]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate event IDs")
    by_id = {e["id"]: e for e in events}
    for e in events:
        parse_time(e["timestamp"])
        if not isinstance(e.get("dependencies", []), list):
            raise ValueError("dependencies must be a list")
        for dep in e.get("dependencies", []):
            if dep not in by_id:
                raise ValueError("missing dependency: " + dep)
    observed = {e["id"] for e in events if parse_time(e["timestamp"]) <= cutoff}
    # Candidates are declared future events only in this synthetic smoke test.
    # Real prospective use MUST use a separately timestamped candidate registry
    # created before the cutoff, never future event labels.
    candidates = []
    for e in events:
        if e["id"] in observed:
            continue
        deps = e.get("dependencies", [])
        if not deps:
            continue
        completed = sum(dep in observed for dep in deps)
        candidates.append({"id": e["id"], "readiness": completed / len(deps),
                           "completed": completed, "required": len(deps)})
    return sorted(candidates, key=lambda x: (-x["readiness"], -x["completed"], x["id"]))

def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: predict.py DATA.json CUTOFF_ISO_UTC")
    with open(sys.argv[1], encoding="utf-8") as fh:
        events = json.load(fh)
    print(json.dumps({"cutoff": sys.argv[2], "warning": "synthetic oracle candidate set; NOT valid historical prediction",
                      "ranked": rank(events, parse_time(sys.argv[2]))}, indent=2))

if __name__ == "__main__":
    main()
