import numpy as np
'''修改数组形状'''
if __name__ == '__main__':
    '''实例1,reshape()改变形状'''
    # a=np.arange(8)
    # print('原始数组:')
    # print(a)
    # print('\n')
    #
    # b=a.reshape(4,2)
    # print('修改后的数组')
    # print(b)

    '''实例2 numpy.ndarray.flat()数组元素迭代器'''
    # a=np.arange(9).reshape(3,3)
    # print('原始数组')
    # for row in a:
    #     print(row)
    #
    # # 对数组中每个元素都进行处理，可以使用flat属性,该属性是一个数组元素迭代器
    # print('迭代后的数组:')
    # for element in a.flat:
    #     print(element,end=', ')


    '''实例2：numpy.ndarray.flatten()'''
    # a=np.arange(8).reshape(2,4)
    # print('原数组:')
    # print(a)
    # print('\n')
    #
    # print(a.flatten())
    # print('\n')
    #
    # print('以F风格顺序展开的数组:')
    # print(a.flatten(order='F'))

    '''实例3：numpy.ndarray.ravel():展开数组'''
    a=np.arange(8).reshape(2,4)
    print('原数组:')
    print(a)
    print('\n')
    print('调用ravel函数之后')
    print(a.ravel())
    print('\n')
    print('以F风格顺序调用ravel函数之后:')
    print(a.ravel(order='F'))