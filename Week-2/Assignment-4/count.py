
def count(input_list):
    result = {}
    for e in input_list:
        result[e] = result.get(e,0)+1
    return result               

num = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(num)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}