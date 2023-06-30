import numpy as np
'''统计函数'''
if __name__ == '__main__':
    '''numpy.amin()、numpy.amax() --> 最大值、最小值'''
    # a=np.array([[3,7,5],[8,4,3],[2,4,9]])
    # print(a)
    # print(np.amin(a,1))
    # print(np.max(a,1))
    # print(np.amin(a,0))
    # print(np.amin(a,0))

    '''numpy.ptp() 最大值与最小值的差'''
    # a=np.array([[3,7,5],[8,4,3],[2,4,9]])
    # print(a)
    # print(np.ptp(a))
    # print(np.ptp(a,1))
    # print(np.ptp(a,0))

    '''numpy.percentile() --> 百分位数'''
    # a=np.array([[10,7,4],[3,2,1]])
    # print(a)
    #
    # print(np.percentile(a,50))
    #
    # print(np.percentile(a,50,0))
    #
    # print(np.percentile(a,50,1))


    '''numpy.median() --> 求中位数'''
    # a=np.array([[30,65,70],[80,95,10],[50,90,60]])
    # print(a)
    # print(np.median(a))
    # print(np.median(a,axis=0))
    # print(np.median(a,axis=1))

    '''numpy.mean() --> 算术平均值'''
    # a = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])
    # print(np.mean(a))
    # print(np.mean(a,1))
    # print(np.mean(a,0))

    '''numpy.average() --> 加权平均值'''
    # a=np.array([1,2,3,4])
    # print(a)
    # print('\n')
    # print(np.average(a))
    # print('\n')
    # wts=np.array([4,3,2,1])
    # print(np.average(a,weights=wts))
    # print('\n')
    # print(np.average([1,2,3,4],weights=[4,3,2,1],returned=True))
    #
    # b=np.arange(6).reshape(3,2)
    # wt=np.array([3,5])
    # print(np.average(b,axis=1,weights=wt))


    '''numpy.std() --> 标准差'''
    print(np.std([1,2,3,4]))

    '''numpy.var() --> 方差'''
    print(np.var([1,2,3,4]))
