from xgu.guarantee_k_in_d import f as guarantee_k_in_d

# populate_d
def f(q):
  d = {}

  for j in q:
    k, v=j[:2], j[3:]
    d = guarantee_k_in_d(d, k)
    d[k].add(v)

  return d
