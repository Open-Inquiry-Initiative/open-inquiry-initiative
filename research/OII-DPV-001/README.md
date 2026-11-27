# OII-DPV-001 — Digital Provenance and Independent Verification
Authorized 2026-11-26. Preliminary AI-assisted research note, not peer reviewed.

## Evidence
User supplied a video (visual analysis only) and screenshots of a social-media post, comments and seven mathematical slides. The video alleges censorship; the slides claim P=NP and VP≠VNP (claimed date Nov 23–24, 2026). A partially obscured heading attributes an algebraic result to Claude. Neither attribution nor identity nor agency involvement is established. Government-like logos are not evidence of endorsement.

## Source inventory
Directly visible: https://zenodo.org/records/20560386 (video), https://zenodo.org/records/22696934 (caption and seven slides), https://zenodo.org/records/24397987 (comment). Related search leads from earlier AI-assisted review: https://zenodo.org/records/17619983 (God Operator Riemann Combo), https://doi.org/10.5281/zenodo.17263747 (Riemann and 3I/ATLAS), https://doi.org/10.5281/zenodo.17262436 (Omega Prime Proof), https://doi.org/10.5281/zenodo.17129113 (Prime Imperative). Related records are leads, not verified versions of the original three. Prior conversation reported retrieval failures and a 410 for a related PDF; raw HTTP logs unavailable, so repeat independently. Prior conversation reported an odd-length 141-character signature extraction failing hex decoding; exact input unavailable, so this is an unreplicated report, not evidence of invalid original signature.

## Slide review
1. Random 3-SAT density m/n near 4.27 is a familiar empirical transition; 3.85 unexplained. Satisfiability probability is not worst-case runtime.
2. Successor arithmetic proves 1+1=2; checking a proof differs from finding one. A polynomial-time bounded proof search claim requires precise encoding and proof system.
3. 14! = 87178291200. Subset recurrence f(S)=sum_{j in S} a_{|S|,j} f(S minus j), f(empty)=1, computes permanent in O(n 2^n) arithmetic operations.
4–6. Determinant has polynomial arithmetic complexity; Gaussian elimination O(n^3) field operations, with pivot/sign handling. Permanent is VNP-complete over suitable fields (characteristic not 2). Known exponential algorithms do not establish a general lower bound.
7. VP≠VNP asserted, no full proof visible. Classical P vs NP and algebraic VP vs VNP are distinct.

## Validation plan
Recover source bytes and metadata, record timestamps, hashes, status and archive history. Compare withdrawal policy https://about.zenodo.org/policies/ and independent records; do not infer agency involvement from missing pages. Verify any recovered signature against the independently established public key and exact message/hash convention; fresh challenge and provenance needed for identity claims. For Riemann claims require full spectral correspondence proof, for orbital claims independent ephemerides and preregistered statistical null models, for retrocausality controlled replication. For complexity claims require complete proof, precise model, asymptotic bounds and expert review. Reference https://www.claymath.org/millennium/p-vs-np/ and Valiant 1979, The Complexity of Computing the Permanent.
Preserve negative results and competing explanations under RABE-001. No raw third-party media republished pending rights/privacy review. No proof, identity, censorship attribution or breakthrough established. Engineering follow-up: ../OII-DPV-001-EXT-001/README.md.
