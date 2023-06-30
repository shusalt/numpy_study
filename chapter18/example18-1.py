import numpy as np
'''numpy排序、条件筛选函数'''
if __name__ == '__main__':
    '''numpy.sort'''
    a=np.array([[3,7],[9,1]])
    print(a)
    print(np.sort(a))
    print(np.sort(a,axis=0))
    dt=np.dtype([('name','S10'),('age',int)])
    a=np.array(([('raju',21),('anil',25),('ravi',17),('amar',27)]),dtype=dt)
    print(a)
    print(np.sort(a,order='name'))