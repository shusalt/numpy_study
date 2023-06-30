import numpy as np
'''连接数组'''
if __name__ == '__main__':
    '''numpy.concatenate --> 连接现有轴的数组序列'''
    # a=np.array([[1,2],[3,4]])
    #
    # print('第一个数组')
    # print(a)
    # print('\n')
    # b=np.array([[5,6],[7,8]])
    #
    # print('第二个数组:')
    # print(b)
    # print('\n')
    #
    # print('沿轴1连接两个数组:')
    # print(np.concatenate((a,b),axis=1))

    '''numpy.stack --> 沿着新轴连接数组序列'''
    # a=np.array([[1,2],[3,4]])
    # print('第一个数组:')
    # print(a)
    # print('\n')
    #
    # b=np.array([[5,6],[7,8]])
    # print('第二个数组:')
    # print(b)
    #
    # print('沿轴0堆叠两个数组')
    # print(np.stack((a,b)))
    # print('\n')
    #
    # print('沿轴1堆叠两个数组')
    # print(np.stack((a,b),1))

    '''numpy.hstack --> 水平堆叠数组'''
    # a=np.array([[1,2],[3,4]])
    #
    # print('第一个数组:')
    # print(a)
    # print('\n')
    # b=np.array([[5,6],[7,8]])
    #
    # print('第二个数组')
    # print(b)
    # print('\n')
    #
    # print('水平堆叠')
    # c=np.hstack((a,b))
    # print(c)

    '''numpy.vstack --> 垂直堆叠来生成数组'''
    a=np.array([[1,2],[3,4]])

    print('第一个数组:')
    print(a)
    print('\n')
    b=np.array([[5,6],[7,8]])

    print('第二个数组')
    print(b)
    print('\n')

    print('竖直堆叠')
    c=np.vstack((a,b))
    print(c)

