# Track B offline research record generator — G2

Prototype only. No chat-history access, GitHub writes, publication, automatic ID reservation or privacy approval.

Requires Python 3.10+ and the standard library.

Run tests:

```bash
cd tools/research-intake
python -m unittest -v
```

Generate a record from a locally supplied JSON object with `title`, `summary`, `questions`, `hypotheses`, `evidence`, `next_steps`:

```bash
python intake.py input.json --id OII-B-20261119-001 --date 2026-11-19
```

Output is JSON containing Markdown, SHA-256 content fingerprint, advisory review flags, and `publication_approved: false`. Do not treat regex secret checks as comprehensive DLP. Identifiers are caller-supplied and not collision-safe until G3. Never use unreviewed output for public publication.

Local initial verification: eight unittest cases passed on 2026-11-19; GitHub CI and independent environment verification not yet performed.
