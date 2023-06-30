import numpy as np
'''
迭代数组
'''
if __name__ == '__main__':
    '''实例1'''
    # a=np.arange(6).reshape(2,3)
    # print("原始数组是：")
    # print(a)
    # print('\n')
    # print('迭代输出元素:')
    # for x in np.nditer(a):
    #     print(x,end=', ')
    # print('\n')

    '''实例2'''
    # a=np.arange(6).reshape(2,3)
    # print(a.T)
    # for x in np.nditer(a.T):
    #     print(x,end=', ')
    # print('\n')
    #
    # for x in np.nditer(a.T.copy(order='C')):
    #     print(x,end=', ')
    # print('\n')

    '''实例3'''
    # a=np.arange(0,60,5)
    # a=a.reshape(3,4)
    # print('原始数组:')
    # print(a)
    # print('\n')
    # print('原始数组的转置:')
    # print(a.T)
    # c=a.copy(order='C')
    # print('c风格数组')
    # print(c)
    # for x in np.nditer(c):
    #     print(x,end=', ')
    # print('\n')
    # f=a.copy(order='F')
    # print('f风格数组')
    # print(f)
    # for x in np.nditer(f):
    #     print(x,end=', ')

    '''实例4'''
    # a=np.arange(0,60,5)
    # a=a.reshape(3,4)
    # print('原始数组是：')
    # print(a)
    # print('\n')
    # print('以c风格进行遍历')
    # for x in np.nditer(a,order='C'):
    #     print(x,end=', ')
    # print('\n')
    # print('以f风格进行遍历')
    # for x in np.nditer(a,order='F'):
    #     print(x,end=', ')


    '''实例5'''
    # a=np.arange(0,60,5)
    # a=a.reshape(3,4)
    # print(a)
    # print('\n')
    # for x in np.nditer(a,op_flags=['readwrite']):
    #     x[...]=2*x
    # print('修改后的数组是:')
    # print(a)

    '''实例6'''
    # a=np.arange(0,60,5)
    # a=a.reshape(3,4)
    # print('原始数组')
    # print(a)
    # print('\n')
    # print('修改后的数组是:')
    # for x in np.nditer(a,flags=['external_loop'],order='F'):
    #     print(x,end=', ')

    '''实例7'''
    # a=np.arange(0,60,5)
    # a=a.reshape(3,4)
    # print('第一个数组为:')
    # print('第二个数组为:')
    # b=np.array([1,2,3,4],dtype=int)
    # print(b)
    # print('\n')
    # print('修改后的数据为:')
    # for x,y in np.nditer([a,b]):
    #     print('{0}:{1}'.format(x,y),end=', ')

    
