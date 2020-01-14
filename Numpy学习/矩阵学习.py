import numpy as np

a = np.arange(15).reshape(3,5)
print('矩阵a',a)
print('a在每个维度的size',a.shape)
print('a的维度',a.ndim)
print('a的转置矩阵',a.T)
print('a的元素个数',a.size)
print('矩阵a的元素类型',a.dtype)
print('a的元素类型的字节大小',a.itemsize)
print('a的内存地址',a.data)
print('a的类型',type(a))


b = np.array([[1.5,2,3],[4,5,6]],'float64')
print('矩阵b',b)
print('矩阵b的数据类型',b.dtype)

'''零矩阵'''
c = np.zeros((5,6))
print('c矩阵',c)

'''一矩阵'''
d = np.ones((5,6),dtype='int64')
print('矩阵d',d)

'''empty矩阵的元素生成是随机的，依赖于当前的内存状态，默认为float64类型'''
e = np.empty((5,6))
print('随机矩阵',e)
print('随机矩阵',e)

'''创造特定序列的矩阵，提供类似range函数的功能,shape类型为1*n，可以利用reshape重塑'''
f = np.arange(10,30,5)
print('矩阵f',f)
f = f.reshape((2,2))
print('f矩阵重塑',f)

'''arange不能指定元素的个数，可以通过linspace指定,左闭右闭区间，其元素间隔有第三个参数（元素数量）来决定'''
g = np.linspace(0,9,3)
print('矩阵g',g)

'''矩阵的操作'''
#两矩阵相减
a = np.array([20,30,40,50])
b = np.arange(4)
print('矩阵相减',a-b)
print('b**2',b**2)
print('10*np.sin(a)',10*np.sin(a))
print(a<15)

#矩阵相乘dot
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[1,1,1],[2,2,2],[3,3,3]])
print('a,b矩阵相乘',a.dot(b))
print('a,b每个元素相乘',a*b)

#取a中最小元素
print(a.min())
print(np.min(a))

#取每个纵向数列的中间数
print('纵向数列中间数',np.median(a,axis = 0))
print('横向数列中间数',np.median(a,axis = 1))
print('取行索引为1的所在行',a[1,...])
print('取列索引为1的所在列',a[...,1])
print('切片,让矩阵a中所有小于5的元素都成为5，所有大于7的元素都成为7，只留下中间元素',np.clip(a,5,7))
print('a的所有元素平均数，不指定行，列,b',np.mean(a))
print('指定行，求平均',np.mean(a,axis=1))
print('取a的特定位置元素',a[2,2])

#取特定行或者特定列，亦或者特定行或列后面的所有元素
print('取a的行索引为1的所在行',a[1,:])
print('取a的行索引为1后面的所有行',a[1:,:])
print('取a的列索引为1',a[:,1])
print('取a的列索引1后面的所有列',a[:,1:])
print('取a的第一行和第二行',a[0:2,:])
print('取a的最后一行',a[-1])
print('取a的最后一行',a[-1,:])
print('取a的最后一列',a[:,-1])

#flat迭代器，取a中每一个元素
for element in a.flat:
    print(element,end= ' ')
print('\n')

#将a平铺
print('a平铺展开',a.flatten())
print(np.floor(a))

#将啊a,b横,纵向拼接
print('a,b横向拼接',np.hstack((a,b)))
print('a,b纵向拼接',np.vstack((a,b)))

#多个矩阵横纵向拼接
c = np.array([[7,8,9],[4,5,6],[1,2,3]])
print('a,b,c横向拼接',np.concatenate((a,b,c),axis = 1))
print('a,b,c纵向拼接',np.concatenate((a,b,c),axis = 0))

#分隔矩阵，value必须要求均匀分隔
print('a矩阵横向分隔',np.hsplit(a,3))
print('a矩阵纵向分隔',np.vsplit(a,3))

#不均匀分隔
print('a矩阵横向不均匀分隔',np.array_split(a,2,axis=1))
print('a矩阵纵向不均匀分隔',np.array_split(a,2,axis=0))

#深拷贝与浅拷贝
#浅拷贝,由于array是复杂对象，直接赋值，相当于对整个复杂对象添加了一个指针，并未开辟新的内存
c = a
a[1,:] =[0,0,0]
print('a改变后',a)
print('c',c)

#在array这里，利用copy是实现深拷贝，但不推荐，因为其他地方copy则为浅拷贝
import copy
c = copy.copy(a)
a[1,:] =[1,1,1]
print('a改变后',a)
print('c',c)

#深拷贝,用copy模块的deepcopy函数
import copy
c = copy.deepcopy(a)
a[1,:] = [2,3,4]
print('a改变后',a)
print('c',b)

#对矩阵取逆
d = np.array([[ 3.,  2.,  3.],
       [ 4.,  7.,  6.],
        [7., 8., 11.,]])
print(np.linalg.inv(d))
print(np.dot(d,np.linalg.inv(d)))


#打印10*10的1矩阵
print(np.ones((10,10)))
#打印1*10列的矩阵
print(np.ones(10))
print(np.array([[1],[2],[3]]).shape)

print(np.array([1,2,3]).shape)
print(np.c_[np.array([1,2,3]),np.array([4,5,6])])

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c = np.ones(2)
print(np.c_[a,c])
print(np.c_[a,b])
print(np.r_[a,b])

x = np.arange(4)
xx = x.reshape(4, 1)
print(x)
print(xx)

#一维数组参与点乘时，放在左边会变换为行向量，最后结果时行向量；放在右边变换为列向量，最后结果时列向量
a = np.array([1,2])
b = np.array([1,0])
c = np.array([[1,2],[4,5]])
print('两个一维数组点乘，为一个值',np.dot(a,b))

#一维数组在左边，视为行向量，无论左右，最后结果是一个一维数组
print('一维数组在左边',np.dot(a,c))

#一维数组在右边，视为列向量，最后结果是一个一维数组
print('一维数组在右边',np.dot(c,a))

print(np.c_[a,b])
print(np.r_[a,b])

a = np.array([1,2])
b = np.array([1,2])

#返回为一个值
print(np.dot(a,b))
print(a.dot(b))

print('a*b',a*b)

a = np.array([1,2]).reshape(1,2)
b = np.array([1,2])

#当矩阵和一个一维数组相乘，一维数组在左边时视为列向量，最后结果也是一个列向量
#当矩阵和一个一维数组相乘，一维数组在右边时视为行向量，最后结果也是一个行向量
print(a.dot(b))
#可以利用np.sum得到最终结果
print(np.sum(a.dot(b)))

#返回为一个矩阵
print(np.mat(a.reshape(1,2)) * np.mat(b.reshape(2,1)))
print(np.mat(a.reshape(1,2)).dot(np.mat(b.reshape(2,1))))

a = np.array([1,2,3,4]).reshape(4,1)
b = np.array([1,2,3,4,1,2,3,4]).reshape(4,2)
print(a)
print(b)
print(a * b)
a =  np.array([1,2,3,4])[:,np.newaxis]
print('增加维度后的a',a)

a = np.array([5,6,7,8])[np.newaxis,:]
print('增加维度后的a',a)

#一个列向量与一个一维数组相减，一维数组和列向量都会进行广播,广播成3 * 3的矩阵
#列向量广播为[[1,1,1],[2,2,2],[3,3,3]],一维数组广播为[[1,2,3],[1,2,3],[1,2,3]]
print(np.array([1,2,3]).reshape(3,1) - np.array([1,2,3]))


print(np.array([1,2,3]) ** 2)
print(np.array([1,2,3]) * np.array([1,2,3]))
print(np.square(np.array([1,2,3])))

print(np.array([[1,2,3],[1,2,3]]) * np.array([1,2,3]))

theta = np.array([-1,2])
alpha  = 0.5
X = np.array([[1,2],[3,4]])
y = np.array([1,2])
m = 2
theta[0] = theta[0] - np.sum((X.dot(theta) - y) * X[:, 0])
theta[1] = theta[1] - np.sum((X.dot(theta) - y) * X[:, 1])

print(theta)

theta = np.array([-1,2])
theta = theta - np. sum((X.dot(theta) - y)[:,np.newaxis] * X , 0)
print(theta)

a = np.array([1,4,3,2,5,6])
b = np.array([7,8,3,10,11,12])
print(a == b)
print(a[a == b])
print(np.mean(a == b))
print(np.where(a<3))
print(np.where(a<3,a,b))
print(np.where(a<5,10,6))
print(a[np.where(a<3)])
print(a[np.array([1,3])])
print(a<5)
print(a[a<5])

g = -np.arange(20).reshape(4,5)
print(g)

print(g[np.array([1,2]),np.array([2,3])[:,np.newaxis]])
print(g[1:4,0:4])
print(g[[1,2,3],np.array([0,1,2,3])[:,np.newaxis]])


g[[1,2,3],np.array([0,1,2,3])[:,np.newaxis]] = np.arange(12).reshape(4,3)
print(g)

print(np.ravel(g))

print(np.arange(1, 16).reshape((3, 5)))
print(np.arange(1, 16).reshape((3, 5)).T)
print(np.c_[np.ones(5),np.arange(1, 16).reshape((3, 5)).T])


#计算一个一维数组的积，可以将其改为一个对角矩阵,在计算行列式的值
a = np.array([1,2,3,4]).reshape(2,2)
#        
print('a', a)
val = np.linalg.det(a)
print('val', val)
