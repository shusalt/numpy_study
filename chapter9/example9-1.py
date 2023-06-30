import numpy as np
'''整数数值索引'''
if __name__ == '__main__':
    '''实例1'''
    # x=np.array([[1,2],[3,4],[5,6]])
    # y=x[[0,1,2],[0,1,0]]
    # print(y)

    '''实例2'''
    # x=np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
    # rows=np.array([[0,0],[3,3]])
    # cols=np.array([[0,2],[0,2]])
    # print(x[rows,cols])

    '''实例3'''
    a=np.array([[1,2,3],[4,5,6],[7,8,9]])
    b=a[1:3,1:3]
    c=a[1:3,[1,2]]
    d=a[...,1:]
    print(b)
    print(c)
    print(d)


