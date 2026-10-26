# Projection-only candidate: falsification obligation

Candidate: for every dominating set D of G square H,
|D| >= max(gamma(G)|pi_H(D)|, gamma(H)|pi_G(D)|).
This proposes charging gamma(G) to each occupied H fiber, symmetrically.
External domination across fibers makes that charge suspect.

`experiments/first.py` exhausts every subset of Pn square Pm, 2<=n,m<=4,
checks domination by closed-neighborhood union, and emits a counterexample.
Its exact coordinates, factor domination numbers, row sizes and failed bound
are in `conformance/first.json`. The candidate is retracted, not a conjecture
supported by its passing cases. A corrected proposal must track which vertices
are dominated within a fiber and which require adjacent fibers, including overlap.
This counterexample does not refute Vizing's domination conjecture.
