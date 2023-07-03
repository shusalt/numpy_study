import numpy as np
import numpy.matlib
'''numpy 矩阵库(Matrix)'''
if __name__ == '__main__':
    '''转置矩阵'''
    a=np.arange(12).reshape(3,4)
    print('原数组')
    print(a)
    print('\n')
    print('转置后的数组：')
    print(a.T)

    '''numpy.matlib.empty()'''
    print(np.matlib.empty((2,2)))

    '''numpy.matlib.zeros() --> 创建一个以0填充的矩阵'''
    print(np.matlib.zeros((2,2)))

    '''numpy.matlib.ones() --> 创建一个以1填充的矩阵'''
    print(np.matlib.ones((2,2)))


    '''numpy.matlib.eys() --> 函数返回一个矩阵，对角线元素为1，其他位置为零'''
    print(np.matlib.eye(3,3,0,dtype=float))

    '''numpy.matlib.identity() --> 返回单位矩阵'''
    print(np.matlib.identity(5,dtype=float))

    '''numpy.matlib.rand() --> 随机数的矩阵'''
    print(np.matlib.rand(3,3))

    '''矩阵、数组相互转换'''
    a=np.matrix('1,2;3,4')
    print(a)
    j=np.asarray(a)
    print(j)
    k=np.asmatrix(j)
    print(k)
