"""Falsify a projection-only support bound by exhaustive domination masks."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from source import checked_source
checked_source()

def neighborhoods(n,m=1):
    out=[]
    for i in range(n):
        for j in range(m):
            vs={(i,j)}|{(a,j) for a in (i-1,i+1) if 0<=a<n}|{(i,b) for b in (j-1,j+1) if 0<=b<m}
            out.append(sum(1<<(a*m+b) for a,b in vs))
    return out

def dominating(n,m=1):
    nb=neighborhoods(n,m); full=(1<<(n*m))-1
    for mask in range(1,1<<(n*m)):
        covered=0
        for i,c in enumerate(nb):
            if mask>>i&1:covered|=c
        if covered==full:yield mask

def gamma(n):return min(x.bit_count() for x in dominating(n))

rows=[]; first=None
for n in range(2,5):
    for m in range(2,5):
        gg,gh=gamma(n),gamma(m); total=failures=0; smallest=n*m
        for mask in dominating(n,m):
            total+=1; size=mask.bit_count();smallest=min(smallest,size)
            pts=[(i,j) for i in range(n) for j in range(m) if mask>>(i*m+j)&1]
            pg=len({i for i,j in pts});ph=len({j for i,j in pts})
            bound=max(gg*ph,gh*pg)
            if size<bound:
                failures+=1
                witness={'G':f'P{n}','H':f'P{m}','gamma_G':gg,'gamma_H':gh,
                    'D':pts,'size':size,'projection_G':pg,'projection_H':ph,'candidate_bound':bound,
                    'row_sizes':[sum(i==a for i,j in pts) for a in range(n)]}
                if first is None or size<first['size']:first=witness
            assert size>=gg*gh # bounded Vizing check, never an all-graph claim
        rows.append({'G':f'P{n}','H':f'P{m}','dominating_sets':total,
            'minimum_size':smallest,'projection_bound_failures':failures})
assert first is not None
print(json.dumps({'candidate':'|D| >= max(gamma(G)*|projection_H(D)|, gamma(H)*|projection_G(D)|)',
    'domain':'all dominating subsets of Pn square Pm for 2<=n,m<=4',
    'cases':rows,'counterexample':first,
    'status':'candidate falsified; corrected overlap inequality open; existing Vizing program unchanged'},indent=2))
