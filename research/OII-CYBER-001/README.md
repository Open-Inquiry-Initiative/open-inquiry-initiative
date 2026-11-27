# OII-CYBER-001 — Global Cybersecurity Incident and Systemic Risk Observatory

Version 0.1.0 | 2026-11-27 | Preliminary public research
Status: initial source audit completed; independent external review pending.

## Scope
Initial disclosure window 2026-11-06 through 2026-11-27 inclusive. Historical baseline candidate 2016–2026. Earlier incident inventory is a lead list, not validated evidence. Publication does not establish coordination or acceleration.

## Initial registry
| ID | Disclosure/report date | Entity | Evidence classification | Finding |
|---|---|---|---|---|
| C001 | 2026-11-27 | USAF Cloud One | Credible reporting, single originating investigation | Reuters reports intrusion and service-management disruption; attribution, extent and theft unknown. |
| C002 | 2026-11-24 | CIA/ODNI | Independently reported by Reuters and AP | Unclassified analysis system breached; ODNI reported no disruption to classified systems or critical capabilities. Count as one incident pending distinct evidence. |
| C003 | 2026-11-25 | FinCEN | Agency acknowledgment reported by Reuters | Limited unauthorized access; certain services taken offline; investigation ongoing. |
| C004 | 2026-11-21 | FBI NCIC | Reported, primary confirmation pending | Suspected intrusion; scope unknown. |
| X001 | unknown | NSA communications | Outage only | Exclude from attack counts absent evidence. |
| X002 | unknown | Aviation ground stop | Outage only | Exclude from attack counts absent evidence. |

## Source ledger (consulted 2026-11-27)
- C001: Reuters original investigation: https://www.reuters.com/world/hackers-breach-us-air-force-flagship-cloud-one-computing-platform-2026-11-27/
- C001/C004: BleepingComputer: https://www.bleepingcomputer.com/news/security/us-air-force-cloud-platform-reportedly-hacked-in-latest-federal-breach/ — derivative for C001, not independent confirmation.
- C002: Reuters via Investing.com: https://www.investing.com/news/world-news/us-cia-odni-suffer-cybersecurity-breach-of-some-unclassified-information-nyt-reports-5048922
- C002/X001/X002: Associated Press: https://apnews.com/article/bfa6d3b02e3b0e2779dfb613c900bd77 — separate reporting, anonymous source identity overlap unknown.
- C003: Reuters via Yahoo, quoting agency official: https://malaysia.news.yahoo.com/us-fincen-takes-systems-offline-144239506.html

## Research gates
1. Source-verified registry; capture incident, discovery and disclosure dates separately.
2. Historical baseline: evaluate consistent public incident datasets and coverage changes.
3. Compare frequency with matched calendar windows, report denominators and reporting delays.
4. Identify shared dependencies without inferring shared perpetrators.
5. Record AI involvement only when supported by incident-specific evidence.
6. Assess cascading failures and distinguish attacks from ordinary outages.
7. Test overdispersion, seasonality, reporting bias and alternative explanations; publish uncertainty and negative results.
8. Test defensive compartmentalization, least privilege, audit integrity and recovery using synthetic workloads only.
9. Publish machine-readable registry, methods, source lineage and limitations; solicit independent review.

## Limitations
This is a bounded federal pilot, not a global census. No historical counts, statistical significance tests, forensic examination or independent human replication have been completed. Source syndication is not independent evidence. The actual date of intrusion is unknown for these entries. No claim of coordination or general AI causation is supported. Do not treat missing records as evidence of absence.

## Release safeguards
Public defensive research only; exclude private data, credentials, exploit instructions and sensitive operational information. Preserve corrections and version history.
