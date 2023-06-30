import numpy as np
'''翻转数组'''
if __name__ == '__main__':
    '''numpy.tranpose --> 对换数组的维度'''
    # a=np.arange(12).reshape(3,4)
    # print(a)
    # print(np.transpose(a))


    '''ndarray.T  --> 对换数据的维度'''
    # a=np.arange(12).reshape(3,4)
    # print('原数组')
    # print(a)
    # print('\n')
    # print('转置数组')
    # print(a.T)

    '''numpy.rollaxis --> 向后滚动特定的轴到一个特定位置，格式如下:'''
    # a=np.arange(8).reshape(2,2,2)
    #
    # print('原数组')
    # print(a)
    # print('获取数组中一个值')
    # print(np.where(a==6))
    # print(a[1,1,0])
    #
    # # 将轴2滚动到轴0（宽度到深度）
    # print('调用rollaxis函数：')
    # b=np.rollaxis(a,2,0)
    # print(b)
    # print(np.where(b==6))
    # print('\n')
    #
    # # 将轴2滚动到轴1：（宽带到高度）
    # print('调用rollaxis函数:')
    # c=np.rollaxis(a,2,1)
    # print(np.where(c==6))
    # print('\n')

    '''numpy.swapaxes --> 交换数组的两个轴'''
    # import numpy as np
    # a=np.arange(8).reshape(2,2,2)
    #
    # print('原数组:')
    # print(a)
    # print('\n')
    #
    # # 现在交换轴0（深度方向）和轴2（宽带反向）
    # print('调用swapaxes函数后的数组:')
    # print(np.swapaxes(a,2,0))


