# -*- coding: utf-8 -*-

def group_by_key(input_dic):
  result = {}
  for e in input_dict:
    result[e['key']] = result.setdefault(e['key'],0) + e['value']
  return result


input_dict = [{'key': 'a', 'value': 3}, {'key': 'b', 'value': 1}, 
{'key': 'c', 'value': 2}, {'key': 'a', 'value': 3}, {'key': 'c', 'value': 5}]

print(group_by_key(input_dict)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}