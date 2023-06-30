import numpy as np
if __name__ == '__main__':
    '''实例1 slice函数'''
    # a=np.arange(10)
    # s=slice(2,7,2)
    # print(a[s])

    '''实例2 冒号分隔切片参数--->start:stop:step'''
    # a=np.arange(10)
    # print(a[2:7:2])

    '''实例3'''
    # a=np.arange(10)
    # print(a[5])
    # print(a[2:])
    # print(a[2:6])


    '''实例4,使用省略号...进行索引和切片'''
    a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
    print(a[...,1])
    print(a[1,...])
    print(a[...,1:])
