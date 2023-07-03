import numpy as np
'''numpy副本和视图'''
if __name__ == '__main__':
    '''无复制'''
    # a=np.arange(6)
    # print('原始数组:')
    # print(a)
    # print('a数组的id',id(a))
    # b=a
    # print('b数组的id',id(b))
    # b.shape=3,2
    # print(b)
    # print(a)


    '''视图或浅拷贝'''
    # a=np.arange(6).reshape(3,2)
    # print('数组a:')
    # print(a)
    # b=a.view()
    # print('a的视图',b)
    # print('a的id',id(a))
    # print('b的id',id(b))
    # b.shape=2,3
    # print(b)
    # print(a)
    # print(a.T)

    '''使用切片创建视图修改数据会影响到原始数组：'''
    # arr = np.arange(12)
    # print('我们的数组：')
    # print(arr)
    # print('创建切片：')
    # a = arr[3:]
    # b = arr[3:]
    # a[1] = 123
    # b[2] = 234
    # print(arr)
    # print(id(a), id(b), id(arr[3:]))


    '''副本和深拷贝'''
    # a=np.array([[10,10],[2,3],[4,5]])
    #     # print('数组a:')
    #     # print(a)
    #     # print('创建a的深层副本')
    #     # b=a.copy()
    #     # print(b)
    #     # print(b is a)
    #     # b[0,0]=100
    #     # print(b)
    #     # print(a)

