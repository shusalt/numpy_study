import numpy as np
'''数组元素的添加与删除'''
if __name__ == '__main__':
    '''numpy.resize'''
    # a=np.array([[1,2,3],[4,5,6]])
    #
    # print('第一个数组:')
    # print(a)
    # print('\n')
    # print('第一个数组的形状')
    # print(a.shape)
    # print('\n')
    #
    # b=np.resize(a,(3,2))
    # print('第二个数组的形状')
    # print(b.shape)
    # print('\n')
    # # 要注意 a 的第一行在b中重复出现，因为尺寸变大了
    #
    # print('修改第二个数组的大小')
    # b=np.resize(a,(3,3))
    # print(b)


    '''numpy.appebd'''
    # a=np.array([[1,2,3],[4,5,6]])
    # print('第一个数组')
    # print(a)
    # print('\n')
    #
    # print('向数组添加元素：')
    # print(np.append(a,[7,8,9]))
    # print('\n')
    #
    # print('沿轴0(竖直)添加元素:')
    # print(np.append(a,[[7,8,9]],axis=0))
    # print('\n')
    #
    # print('沿轴1(水平)添加元素:')
    # print(np.append(a,[[5,5,5],[7,8,9]],axis=1))


    '''numpy.insert'''
    # a=np.array([[1,2],[3,4],[5,6]])
    # print('第一个数组')
    # print(a)
    # print('\n')
    #
    # print('未传递axis参数。在删除之前输入数组会被展开')
    # print(np.insert(a,3,[11,12]))
    # print('\n')
    # print('传递了axis参数，会广播数组来配输入数组')
    #
    # print('沿轴0广播，')
    # print(np.insert(a,1,[11],axis=0))
    # print('\n')
    #
    # print('沿轴1广播')
    # print(np.insert(a,1,11,axis=1))


    '''numpy.delete'''
    # a=np.arange(12).reshape(3,4)
    #
    # print('第一个数组:')
    # print(a)
    # print('\n')
    #
    # print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
    # print(np.delete(a,5))
    #
    # print('删除第二列:')
    # print(np.delete(a,1,axis=1))
    # print('\n')
    #
    # print('包含从数组中删除的替代值的切片：')
    # a=np.array([1,2,3,4,5,6,7,8,9,10])
    # print(np.delete(a,np.s_[::2]))


    '''numpy.unique'''
    a=np.array([5,2,6,2,7,5,6,8,2,9])

    print('第一个数组')
    print(a)
    print('\n')

    print('第一个数组的去重值:')
    u=np.unique(a)
    print(u)
    print('\n')

    print('去重数组的索引数组:')
    u,indices=np.unique(a,return_index=True)
    print(u)
    print(indices)
    print('\n')

    u,indices=np.unique(a,return_inverse=True)
    print(u)
    print(indices)
    print('\n')

    u,indices=np.unique(a,return_counts=True)
    print(u)
    print(indices)
    print('\n')