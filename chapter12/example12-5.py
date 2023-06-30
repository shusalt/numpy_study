import numpy as np
'''分割数组'''
if __name__ == '__main__':
    '''numpy.split --> 将一个数组分割为多个子数组'''
    # a = np.arange(9)
    #
    # print('第一个数组：')
    # print(a)
    # print('\n')
    #
    # print('将数组分为三个大小相等的子数组：')
    # b = np.split(a, 3)
    # print(b)
    # print('\n')
    #
    # print('将数组在一维数组中表明的位置分割：')
    # b = np.split(a, [4, 7])
    # print(b)

    # a = np.arange(16).reshape(4, 4)
    # print('第一个数组：')
    # print(a)
    # print('\n')
    # print('默认分割（0轴）：')
    # b = np.split(a, 2)
    # print(b)
    # print('\n')
    #
    # print('沿水平方向分割：')
    # c = np.split(a, 2, 1)
    # print(c)
    # print('\n')
    #
    # print('沿水平方向分割：')
    # d = np.hsplit(a, 2)
    # print(d)

    '''numpy.hsplit --> 水平切分'''
    # harr=np.floor(10*np.random.random((2,6)))
    # print('原array')
    # print(harr)
    #
    # print('拆分后')
    # print(np.hsplit(harr,3))


    '''numpy.vsplit --> 竖直切分'''
    a=np.arange(16).reshape(4,4)

    print('第一个数组:')
    print(a)
    print('\n')

    print('竖直分割')
    b=np.vsplit(a,2)
    print(b)
