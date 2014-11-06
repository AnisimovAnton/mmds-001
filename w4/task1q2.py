import copy
from math import sqrt

def dotproduct(a1,a2):
  res = 0
  for i in range(len(a1)):
    res += a1[i] * a2[i]
  return res

def norm(a1):
  res = 0
  for i in range(len(a1)):
    res += a1[i] * a1[i]
  return sqrt(res)

def cosdist(a1,a2):
  return 1 - (dotproduct(a1,a2) / (norm(a1) * norm(a2)))

a0 = [[1,0,1,0,1,2],[1,1,0,0,1,6],[0,1,0,1,0,2]]
scale = [0,0.5,1,2]

data = []
for j in range(len(scale)):
  tmp = copy.deepcopy(a0)
  for i in range(3):
    tmp[i][5] *= scale[j]
  data.append(tmp[:])

def Letter(i):
  if i == 0:
    return 'A'
  if i == 1:
    return 'B'
  if i == 2:
    return 'C'

for i in range(len(scale)):
  print 'a =', scale[i]
  for j in range(len(a0)):
    for k in range(j,len(a0)):
      if j != k:
        print Letter(j), Letter(k), cosdist(data[i][j],data[i][k])
  print

