import numpy as np
'''修改数组维度'''
if __name__ == '__main__':
    '''broadcast --> 模仿广播状态'''
    # x=np.array([[1],[2],[3]])
    # y=np.array([4,5,6])
    #
    # # 对 y 广播 x
    # b=np.broadcast(x,y)
    # # 它拥有 iterator 属性，基于自身组件的迭代器元组
    # print('对 y 广播 x：')
    # r,c=b.iters
    #
    #
    # # Python3.x 为 next(context) ，Python2.x 为 context.next()
    # print(next(r),next(c))
    # print(next(r),next(c))
    # print('\n')
    # # shape 属性返回广播对象的形状
    #
    # print('广播对象的形状')
    # print(b.shape)
    # print('\n')
    # # 手动使用broadcast将x与y相加
    # b=np.broadcast(x,y)
    # c=np.empty(b.shape)
    #
    # print('手动使用broadcast将x与y相加：')
    # print(c.shape)
    # print('\n')
    # c.flat=[u+v for (u,v) in b]
    #
    # print('调用flat函数')
    # print(c)
    # print('\n')
    # # 获得了和Numpy内建的广播支持相同的结果
    #
    # print('x与y的和:')
    # print(x+y)

    '''broadcast_to --> 将数字广播到新形状'''
    # a = np.arange(4).reshape(1, 4)
    #
    # print('原数组：')
    # print(a)
    # print('\n')
    #
    # print('调用 broadcast_to 函数之后：')
    # print(np.broadcast_to(a, (4, 4)))

    '''expand_dims --> 在指定位置插入新的轴来扩展数组形状 '''
    # x=np.array([[1,2],[3,4]])
    #
    # print('数组x:')
    # print('\n')
    # y=np.expand_dims(x,axis=0)
    #
    # print('数组y:')
    # print(y)
    # print('\n')
    #
    # print('数组x和y的形状：')
    # print(x.shape,y.shape)
    # print('\n')
    # y=np.expand_dims(x,axis=1)
    #
    # print('在位置1插入轴之后的数组y:')
    # print(y)
    # print('\n')
    #
    # print('x.ndim 和 y.dim:')
    # print(x.ndim,y.ndim)
    # print('\n')
    #
    # print('x.shape 和 y.shape')
    # print(x.shape,y.shape)


    '''numpy.squeeze --> 从给定数组的形状中删除一维的条目'''
    # x=np.arange(9).reshape(1,3,3)
    # print('数组x:')
    # print(x)
    # print('\n')
    # y=np.squeeze(x)
    #
    # print('数组y:')
    # print(y)
    # print('\n')
    #
    # print('数组x和y的形状:')
    # print(x.shape,y.shape)

