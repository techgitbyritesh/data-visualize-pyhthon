import numpy as np
my_list=[1,3,5,7,9]
ver=np.array(my_list)
print(ver)
print(ver.shape)
my_list1=[1,4,3,2,5]
my_list2=[3,5,7,8,9]
my_list3=[11,12,13,12,10]
ver=np.array([my_list1,my_list2,my_list3])
print(ver)
print(ver.shape)
print(ver.reshape(5,3))
VER=np.array(["x",'y',"z",'k','m'])
print(VER[2])
print(ver[:,:])
print(ver[1:3,2:4])
ver=np.arange(0,10)

ver[3:]=50
print(ver)
ver2=np.linspace(1,10,50)
print(ver2)
ver4=np.arange(0,10)
print(ver4)
ver4[3:]=100
print(ver4)
val=2
ver4<2
print(np.random.rand(3,3))