#
from collections import deque,defaultdict,Counter
s=[1,2,3,4,5,1,2,3,7,5,7,4,3,2,1,4,8,5,7,2,7,8,5]
feq=Counter(s)
print(feq)
#Counter({2: 4, 5: 4, 7: 4, 1: 3, 3: 3, 4: 3, 8: 2})
d=defaultdict(int)
for i in s:
    d[i]+=1
print(d)
#defaultdict(<class 'int'>, {1: 3, 2: 4, 3: 3, 4: 3, 5: 4, 7: 4, 8: 2})

d = deque()
d.appendleft(12)
d.pop()
d.append(12)
d.popleft()
print(d)
'''
12345678
  ------------------------
in                         out
  ------------------------

  -------------------------
out                          in
  -------------------------
  '''
#deque([])