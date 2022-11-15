from args import sum_squares
from args import absolute_sum
from args import personal_numbers

#args means I can use as many arguments as possible
def sum(*args):
  total = 0
  for arg in args:
    total += arg
    return total



    
print(sum(2,3,4,55,6,88,445,66,35))

#kwargs means using key values(limitless) its a step beyond args
# keys and values represented**
def a_sum(**kwargs):
  total = 0
  for key,value in kwargs.items():
    print (f'{key} = {value}')
    total += value
  return total



print(a_sum(x=3, y=5, z=22))




print(sum_squares(2,2,5,5))
print(absolute_sum(2,2))
print(personal_numbers("monica", 22, 47, 5, 5, 25, 3))