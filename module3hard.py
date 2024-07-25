data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def unpacking(lis):
    rez = 0
    p = None
    if type(lis) == list or type(lis) == set or type(lis) == tuple:
        if len(lis) > 0:
            for j in lis:
               rez += unpacking(j)
        else:
            return 0
    elif type(lis) == dict:
        for k in lis:
            rez += len(k)
            rez += lis[k]
        return rez
    else:
        p = lis
        if type(p) == str:
            rez += len(p)
        else:
            rez += p
    return rez

def calculate_structure_sum(ds):
    prom = 0
    for i in ds:
        prom += unpacking(i)
    return prom


result = calculate_structure_sum(data_structure)
print(result)