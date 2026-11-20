"""Offline deterministic Track B record generator. No network or GitHub writes."""
import hashlib
import json
import re
from datetime import date
from pathlib import Path

REQUIRED = ('title', 'summary', 'questions', 'hypotheses', 'evidence', 'next_steps')
SENSITIVE = re.compile(r'(?i)(password\s*[:=]|api[_ -]?key\s*[:=]|secret\s*[:=]|bearer\s+[a-z0-9._-]+|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----)')


def validate(record):
    if not isinstance(record, dict):
        raise ValueError('record must be an object')
    for key in REQUIRED:
        if key not in record or not isinstance(record[key], (str, list)) or not record[key]:
            raise ValueError(f'missing or invalid {key}')
    if not isinstance(record['title'], str) or not record['title'].strip():
        raise ValueError('title must be nonempty text')
    return record


def fingerprint(record):
    validate(record)
    normalized = json.dumps({k: record[k] for k in REQUIRED}, sort_keys=True, ensure_ascii=False, separators=(',', ':'))
    return hashlib.sha256(normalized.encode('utf-8')).hexdigest()


def render(record, identifier, day):
    validate(record)
    if not re.fullmatch(r'OII-B-\d{8}-\d{3}', identifier):
        raise ValueError('invalid identifier')
    if identifier[6:14] != day.strftime('%Y%m%d'):
        raise ValueError('identifier/date mismatch')
    def field(k):
        v = record[k]
        return '\n'.join('- ' + str(x) for x in v) if isinstance(v, list) else v.strip()
    return (f'# {identifier} — {record["title"].strip()}\n\n'
            f'**Date:** {day.isoformat()}  \n**Status:** Intake / unverified  \n'
            f'**Fingerprint:** `{fingerprint(record)}`\n\n'
            f'## Summary\n{field("summary")}\n\n## Research questions\n{field("questions")}\n\n'
            f'## Hypotheses (unverified)\n{field("hypotheses")}\n\n'
            f'## Evidence and references\n{field("evidence")}\n\n'
            f'## Next steps\n{field("next_steps")}\n\n'
            '## Publication review\n- [ ] Privacy and secrets review\n- [ ] Rights and licensing review\n'
            '- [ ] Evidence and claims review\n- [ ] Explicit publication approval\n\n'
            '## Track A promotion\n**Decision:** Not reviewed\n')


def generate(record, identifier, day):
    """Return markdown and advisory flags; never auto-approve publication."""
    markdown = render(record, identifier, day)
    return {'identifier': identifier, 'fingerprint': fingerprint(record),
            'markdown': markdown, 'review_flags': ['possible_secret'] if SENSITIVE.search(markdown) else [],
            'publication_approved': False}


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=Path)
    parser.add_argument('--id', required=True)
    parser.add_argument('--date', required=True)
    args = parser.parse_args()
    result = generate(json.loads(args.input.read_text(encoding='utf-8')), args.id, date.fromisoformat(args.date))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
