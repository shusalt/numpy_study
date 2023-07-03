import numpy as np
'''numpy排序、条件筛选函数'''
if __name__ == '__main__':
    '''numpy.sort() --> 排序函数'''
    # a=np.array([[3,7],[9,1]])
    # print(a)
    # print(np.sort(a))
    # print(np.sort(a,axis=0))
    # dt=np.dtype([('name','S10'),('age',int)])
    # a=np.array(([('raju',21),('anil',25),('ravi',17),('amar',27)]),dtype=dt)
    # print(a)
    # print(np.sort(a,order='name'))

    '''numpy.sort() --> 返回数组值从小到大的索引'''
    # x=np.array([3,1,2])
    # print(x)
    # y=np.argsort(x)
    # print(y)
    # print(x[y])
    # print('\n')
    # for i in y:
    #     print(x[i],end=' ')


    '''numpy.lexsort() --> 对多个序列进行排序'''
    # nm=('raju','anil','ravi','amar')
    # dv=('f.y','s.y','s.y','f.y')
    # inv=np.lexsort((dv,nm))
    # print(inv)
    # print([nm[i]+':'+dv[i] for i in inv])


    '''numpy.sort_complex() --> 复数排序'''
    # print(np.sort_complex([5,3,6,2,1]))
    # print(np.sort_complex([1+2j,2-1j,2-1j,3-2j,3-3j,3+5j]))


    '''numpy.partition() -->  分区排序,指定一个数，对数组进行排序'''
    # a=np.array([3,4,2,1])
    # print(np.partition(a,3))
    # print(np.partition(a,(1,3)))


    '''numpy.argpartition() --> 可以通过关键字 kind 指定算法沿着指定轴对数组进行分区'''
    # arr=np.array([45,57,23,39,1,10,0,120])
    # print(arr[np.argpartition(arr,2)[2]])
    # print(arr[np.argpartition(arr,-2)[-2]])
    # print(arr[np.argpartition(arr,[2,3])[2]])
    # print(arr[np.argpartition(arr,[2,3])[3]])


    '''numpy.argmax、numpy.argmin() --> 分别沿给定轴返回最大和最小元素的索引'''
    # a=np.array([[30,40,70],[80,20,10],[50,90,60]])
    # print(a)
    # print(np.argmax(a))
    # print(a.flatten())
    # maxindex=np.argmax(a,axis=0)
    # print(maxindex)
    # minindex=np.argmin(a,axis=0)
    # print(minindex)
    # minindex=np.argmin(a,axis=1)
    # print(minindex)


    '''numpy.nozero() --> 返回输入数组中非零元素的索引'''
    # a=np.array([[30,40,0],[0,20,10],[50,0,60]])
    # print(a)
    # print('\n')
    # print(np.nonzero(a))

    '''numpy.where() --> 返回数组中满足给定条件的元素的索引'''
    # x=np.arange(9).reshape(3,3)
    # print(x)
    # y=np.where(x>3)
    # print(y)
    # print(x[y])


    '''numpy.extract() --> 返回满足条件的元素'''
    # x=np.arange(9.).reshape(3,3)
    # print(x)
    # condition=np.mod(x,2)==0
    # print(condition)
    # print(np.extract(condition,x))





