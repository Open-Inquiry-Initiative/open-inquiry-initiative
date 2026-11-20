"""G3 offline staging planner. No network calls or repository mutation."""
import re
from datetime import date

ID_PATTERN = re.compile(r'^OII-B-(\d{8})-(\d{3})$')


class DuplicateRecord(ValueError):
    pass


def plan_stage(day: date, fingerprint: str, registry: list, title: str):
    """Plan next ID from a fresh registry snapshot. Caller MUST recheck before commit."""
    if not isinstance(day, date) or not re.fullmatch(r'[0-9a-f]{64}', fingerprint):
        raise ValueError('invalid date or fingerprint')
    if not isinstance(title, str) or not title.strip():
        raise ValueError('title required')
    if not isinstance(registry, list):
        raise ValueError('registry must be a list')
    used = set()
    for entry in registry:
        if not isinstance(entry, dict):
            raise ValueError('invalid registry entry')
        existing_id = entry.get('id')
        existing_fp = entry.get('fingerprint')
        if not isinstance(existing_id, str) or not ID_PATTERN.fullmatch(existing_id):
            raise ValueError('invalid registry identifier')
        if existing_fp == fingerprint:
            raise DuplicateRecord(existing_id)
        if existing_id in used:
            raise ValueError('registry contains duplicate identifiers')
        used.add(existing_id)
    prefix = f'OII-B-{day:%Y%m%d}-'
    seq = next((n for n in range(1, 1000) if f'{prefix}{n:03d}' not in used), None)
    if seq is None:
        raise ValueError('daily identifier space exhausted')
    identifier = f'{prefix}{seq:03d}'
    return {
        'identifier': identifier,
        'fingerprint': fingerprint,
        'path': f'research/intake/{day:%Y/%m}/{identifier}/README.md',
        'title': title.strip(),
        'requires_review': True,
        'requires_fresh_registry_check': True,
        'publication_approved': False,
        'status': 'PLANNED_ONLY',
    }


def verify_before_write(plan: dict, latest_registry: list):
    """Fail closed if the identifier or fingerprint has appeared since planning."""
    if plan.get('status') != 'PLANNED_ONLY':
        raise ValueError('unrecognized staging plan')
    for entry in latest_registry:
        if entry.get('id') == plan['identifier'] or entry.get('fingerprint') == plan['fingerprint']:
            raise DuplicateRecord('stale plan: replan against latest registry')
    return True
