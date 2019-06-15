'''
accepts a list and start and end indicies, returns sum of values between (and
including) the start and end index.
if start parameter is not passed in, it should default to zero. if an end
parameter is not passed in, it should default to the last value in the list. if
end argument is too large, sum should still go through the end of the list.
'''

def range_in_list(lst, start=0, end=None):
  end = end or lst[-1]
  return sum(lst[start:end+1])

print(range_in_list([1,2,3,4,5], 0, 4))
print(range_in_list([1,2,3,4,5], 0, 3))
print(range_in_list([1,2,3,4,5], 1, 3))
