# -*- coding: utf-8 -*-

def group_by_key(input_dic):
  all_key = [i['key'] for i in input_dic]
  all_value = [i['value'] for i in input_dic]
  result = {k:0 for k in sorted(set(all_key))}
  cal = list(zip(all_key,all_value))
  for x,y in cal:
    result[x] +=y
  return result

input_dict = [{'key': 'a', 'value': 3}, {'key': 'b', 'value': 1}, 
{'key': 'c', 'value': 2}, {'key': 'a', 'value': 3}, {'key': 'c', 'value': 5}]

print(group_by_key(input_dict)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}