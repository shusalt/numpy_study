import numpy as np
'''布尔索引'''
if __name__ == '__main__':
    '''实例1'''
    # x=np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
    # print(x)
    # print(x[x>5])

    '''实例2'''
    # a=np.array([np.nan,1,2,np.nan,3,4,5])
    # print(a[~np.isnan(a)])

    '''实例3'''
    a=np.array([1,2+6j,5,3.5+5j])
    print(a[np.iscomplex(a)])
    