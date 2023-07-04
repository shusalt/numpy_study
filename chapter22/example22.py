import numpy as np
'''Numpy 线性代数'''
if __name__ == '__main__':

    # '''矩阵的点积 numpy.dot(a,b,out=none)'''
    a=np.array([[1,2],[3,4]])
    b=np.array([[11,22],[33,44]])
    print('矩阵的点积（叉乘）')
    print(np.dot(a,b))


    '''numpy.vdot() --> 两个向量的点积'''
    a2=np.array([[1,2],[3,4]])
    b2=np.array([[11,12],[13,14]])
    print('两个向量的点积')
    print(np.vdot(a,b))

    '''numpy.inner() --> 数组的向量内积'''
    print('数组的内积：')
    print(np.inner([1,2,3],[0,1,0]))


    '''多维数组实例'''
    a3=np.array([[1,2],[3,4]])
    print(a3)
    b3=np.array([[11,12],[13,14]])
    print(b3)
    print('数组的内积')
    print(np.inner(a3,b3))


    '''numpy.matmul() --> 矩阵的乘积'''
    a4=np.array([[1,0],[0,1]])
    b4=np.array([[4,1],[2,2]])
    print(np.matmul(a4,b4))


    '''numpy.linalg.det() --> 矩阵的行列式'''
    a5=np.array([[1,2],[3,4]])
    print(np.linalg.det(a))

    a6=np.array([[6,1,1],[4,-2,5],[2,8,7]])
    print(a6)
    print(np.linalg.det(a6))
    print(6*(-2*7 - 5*8) - 1*(4*7 - 5*2) + 1*(4*8 - -2*2))


    '''numpy.linalg.solve() --> 求解矩阵线性方程'''


    '''numpy.linalg.inv() --> 计算矩阵的逆矩阵'''
    a7=np.array([[1,2],[3,4]])
    a8=np.linalg.inv(a7)
    print(a7)
    print(a8)
    print(np.dot(a7,a8))


    '''求解线性方程组'''
    print('a矩阵')
    a10=np.array([[1,1,1],[0,2,5],[2,5,-1]])
    print(a10)
    print('a的逆矩阵')
    a10_inv=np.linalg.inv(a10)
    print(a10_inv)

    print('b矩阵')
    b10=np.array([[6],[-4],[27]])
    print(b)

    print('求解线性方程组，x=a^(-1)b')
    print(np.linalg.solve(a10,b10))
