from collections import defaultdict

S=input()
T=input()
Scnt=defaultdict(int)
Tcnt=defaultdict(int)
for c in S: Scnt[c]+=1
for c in T: Tcnt[c]+=1

for c in "atcoder":
  M=max(Scnt[c],Tcnt[c])
  if Scnt['@']<M-Scnt[c] or Tcnt['@']<M-Tcnt[c]:
    print("No")
    exit()
  Scnt['@']-=M-Scnt[c]
  Scnt[c]=M
  Tcnt['@']-=M-Tcnt[c]
  Tcnt[c]=M

print("Yes" if Scnt==Tcnt else "No")