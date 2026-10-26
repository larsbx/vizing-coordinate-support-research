# First domination-support falsification

Every dominating subset of Pn square Pm for 2<=n,m<=4 was checked. The candidate
|D| >= max(gamma(G)|pi_H(D)|, gamma(H)|pi_G(D)|) fails; the receipt records every
fixture's number of dominating sets and number of failures, plus a witness.

On P2 square P4, with vertices numbered from zero along each path, take
D={(0,2),(0,3),(1,0)}. Then |D|=3, |pi_G(D)|=2, |pi_H(D)|=3,
gamma(P2)=1 and gamma(P4)=2. The candidate requires 4, so it is retracted.

A direct check independent of the mask-search machinery is short: (0,0) and
(1,1) neighbor (1,0); (0,1) neighbors (0,2); (1,2) neighbors (0,2); (1,3)
neighbors (0,3); the remaining three vertices belong to D. A single vertex
cannot dominate P4 since its closed neighborhood has at most three vertices;
{1,3} does dominate it. Thus the factor domination numbers used above are exact.

The bounded fixtures satisfy Vizing's usual product bound. This adds no evidence
to the independent repository's historical census or row-CSP acceptance records.
Next: track external domination and overlap within fibers before proposing a
replacement inequality. No all-graph domination result follows from this replay.
