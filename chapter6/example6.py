import numpy as np
'''
numpy从已有的数组创建数据
'''
if __name__ == '__main__':
    '''实例1'''
    # x=[1,2,3]
    # a=np.asarray(x)
    # print(a)

    '''实例2'''
    # x=(1,2,3)
    # a=np.asarray(x)
    # print(a)

    '''实例3'''
    # x=[(1,2,3),(4,5,6)]
    # a=np.asarray(x)
    # print(a)

    '''实例4'''
    # x=[1,2,3]
    # a=np.asarray(x,dtype=float)
    # print(a)

    '''实例5 numpy.frombuffer()'''
    # s=b'Hello word'
    # a=np.frombuffer(s,dtype='S1')
    # print(a)

    '''实例6 numpy.fromiter()'''
    list=range(5)
    it=iter(list)

    x=np.fromiter(it,dtype=float)
    print(x)



