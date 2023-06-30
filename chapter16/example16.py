import numpy as np
'''numpy算术函数'''
if __name__ == '__main__':
    '''add()、subtract()、multipy()、divide()'''
    # a=np.arange(9,dtype=np.float_).reshape(3,3)
    # print('第一个数组')
    # print(a)
    # print('\n')
    # print('第二个数组')
    # b=np.array([10,10,10])
    # print(b)
    # print('两个数据相加:')
    # print(np.add(a,b))
    # print('\n')
    # print('两个数组相减')
    # print(np.subtract(a,b))
    # print('\n')
    # print('两个数组乘')
    # print(np.multiply(a,b))
    # print('\n')
    # print('两个数组相除')
    # print(np.divide(a,b))


    '''numpy.reciprocal() --> 倒数'''
    # a=np.array([0.25,1.33,1,100])
    # print('我们的数组是:')
    # print(a)
    # print('\n')
    # print('调用 reciprocal函数：')
    # print(np.reciprocal(a))

    '''numpy.power() --> 幂函数'''
    # a=np.array([10,100,1000])
    # print(a)
    # print('\n')
    # print(np.power(a,2))
    # b=np.array([1,2,3])
    # print(b)
    # print('\n')
    # print('再次调用power函数')
    # print(np.power(a,b))


    '''numpy.mod() --> 取余函数'''
    a=np.array([10,20,30])
    b=np.array([3,5,7])
    print(a)
    print('\n')
    print(b)
    print('\n')
    print(np.mod(a,b))
    print(np.remainder(a,b))

