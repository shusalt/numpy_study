import numpy as np
'''舍入函数'''
if __name__ == '__main__':
    '''numpy.around --> 四舍五入函数'''
    # a=np.array([1.0,5.55,  123,  0.567,  25.532])
    # print('原数组')
    # print(a)
    # print('\n')
    # print('舍入后')
    # print(np.around(a))
    # print(np.around(a,decimals=1))
    # print(np.around(a,decimals=-1))

    '''floor --> 向下取整'''
    # a=np.array([-1.7,1.5,-0.2,0.6,10])
    # print('提供的数组')
    # print(a)
    # print('\n')
    # print(np.floor(a))


    '''ceil --> 向上取整'''
    a=np.array([-1.7,1.5,-0.2,0.6,10])
    print('提供的数组')
    print(a)
    print('\n')
    print('修改后的数组')
    print(np.ceil(a))

