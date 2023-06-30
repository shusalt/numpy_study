import numpy as np
'''花式索引'''
if __name__ == '__main__':
    '''实例1'''
    # x=np.arange(9)
    # print(x)
    # x2=x[[0,6]]
    # print(x2)
    # print(x2[0])
    # print(x2[1])

    '''实例2'''
    # x=np.arange(32).reshape((8,4))
    # print(x)
    # print(x[[4,2,1,7]])

    '''实例3'''
    # x=np.arange(32).reshape((8,4))
    # print(x)
    # print(x[[-4,-2,-1,-7]])

    '''实例4'''
    # x=np.arange(32).reshape((8,4))
    # print(x)
    # print(x[np.ix_([1,5,7,2],[0,3,1,2])])
