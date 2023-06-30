import numpy as np
if __name__ == '__main__':
    '''实例1 numpy.aranage()'''
    # x=np.arange(5)
    # print(x)

    '''实例2'''
    # x=np.arange(5,dtype=float)
    # print(x)

    '''实例3'''
    # x=np.arange(10,20,2)
    # print(x)

    '''实例4 numpy.linspace()等差数列'''
    # a=np.linspace(1,10,10)
    # print(a)

    '''实例5'''
    # a=np.linspace(1,1,5)
    # print(a)


    '''实例6'''
    # a=np.linspace(10,20,5,endpoint=False)
    # print(a)

    '''实例7 restep显示间距'''
    # a=np.linspace(1,10,10,retstep=True)
    # print(a)

    '''实例8'''
    # a=np.linspace(1,10,10).reshape([10,1])
    # print(a)

    '''实例9 numpy.logspace'''
    # a=np.logspace(1.0,2.0,num=10)
    # print(a)

    '''实例10'''
    a=np.logspace(0,9,10,base=2)
    print(a)
