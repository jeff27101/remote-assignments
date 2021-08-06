
def count(number):
    result = {key:0 for key in sorted(set(number))}
    for i in number:
        result[i] += 1
    return result               

num = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(num)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}