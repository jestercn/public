from functools import reduce
x_list = [1,2,3,4,5,6,7,8]
y_list = [1,2,3,4,5,6]
c_list = [1,0,2,0,3,0,6,0,9]
d_list = []
r = map(lambda x,y:x**2+y , x_list,y_list)
print(list(r))
r =  reduce(lambda x,y:x+y,d_list)
r = print(r)
r = filter(lambda x:x ,c_list)
print(list(r))
