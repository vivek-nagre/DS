import numpy as np

print("question number 1st"*1)
print("create a numpy array which is starting from 2 and end on 50 stepsize of 3")
x=np.arange(start=2,stop=50.5,step=3)
print(x,sep=",")
print(np.dtype)
print('data type of x is: ',x.dtype)
print()
print()
print("quetion number 2...."*2)
print('take the five element input from user and add it into numpy array')
l1=list()
l2=list()
for x1 in range(4):
    num1=int(input(f"enter {x1+1} number :"))
    l1.append(num1)
print("please enter the list 2 element")
for x2 in range(4):
    num2=int(input(f"enter {x2+1} number :"))
    l2.append(num2)
print("this is list 1")
print(l1)

print("this is list 2")
print(l2)

y=np.append(l1,l2)
print(y)
print(y.dtype)

print()
print()
print("question number 3....."*3)
print("shape of my array is:",end="")
c=np.array([[1,2,3,4],[3,4,5,6],[3,4,5,6] ])
print("Shape of my array:",c.shape)
print("Dimention:",c.ndim)
row, col = c.shape
print(row)
print(col)
print("size:",c.size)
m=c.reshape(4,3)
print("after reshape function:",m.shape)

print()
print()


print("question number 4......."*4)
print("conversion of 1-D array into 2-D array")
a_1D=np.arange(1,11)
x=a_1D.reshape(5,2)
print(f"orginal array{a_1D}\n conversion of 1D into 2D:\n{x}")
print(f"dimention of a_1d is: {a_1D.ndim} and \n dimention of x is:{x.ndim}")
print(x[1][0])


print("question number 5...."*5)
arr1=np.array([1,2,3,3])
arr2=np.array([4,5,6,5])

print("horizonal stack array:",np.hstack((arr1,arr2)))
print("vertical stack array:\n",np.vstack((arr1,arr2)))
print()
print()
print("question number 6..."*5)
print("unique lement and copied elemeneet count...")
(unique, counts) = np.unique(arr2, return_counts=True)
frequencies = np.asarray((unique, counts)).T

print(frequencies)


