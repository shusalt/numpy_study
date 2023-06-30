import numpy as np
'''
创建数组
'''
if __name__ == '__main__':
    '''实例1'''
    # a=np.empty([3,2],dtype=int)
    # print(a)

    '''实例2'''
    # x=np.zeros(5)
    # print(x)
    #
    # y=np.zeros((5,),dtype=int)
    # print(y)
    #
    # z=np.zeros((2,2),dtype=[('x','i4'),('y','i4')])
    # print(z)

    '''实例3'''
    # y=np.ones(5)
    # print(y)
    #
    # x=np.ones([2,2],dtype=int)
    # print(x)


    '''实例4   np.zeros_like(a,dtype,order,subok,shape)'''
    # arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
    # zeros_arr=np.zeros_like(arr)
    # print(zeros_arr)


    '''实例5 np.ones_like(a,dtype,order,subok,shape)'''
    arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
    ones_arr=np.ones_like(arr)
    print(ones_arr)
    

