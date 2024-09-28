data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data):
    total_sum = 0
    for i in data:
        if type(i) == int or type(i) == float:
            total_sum += i
        elif type(i) == str:
            total_sum += len(i)
        elif type(i) == list or type(i) == tuple or type(i) == set:
            total_sum += calculate_structure_sum(i)
        elif type(i) == dict:
            for k in i.items():
                total_sum += calculate_structure_sum(k)
        else:
            continue
    return total_sum
    
print(calculate_structure_sum(data_structure))