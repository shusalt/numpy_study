import numpy as np
'''Numpy IO'''
if __name__ == '__main__':
    '''numpy.save() --> 将数组保存到以.npy为扩展名的文件中'''
    # a=np.array([1,2,3,4,5])
    # np.save('../data/outfile.npf',a)

    '''numpy.load() --> 数组加载，加载.npy文件'''
    # print(np.load('../data/outfile.npf.npy'))

    '''numpy.savez --> 将多个数组保存到以npz为扩展名的文件中'''
    # a=np.array([[1,2,3],[4,5,6]])
    # b=np.arange(0,1.0,0.1)
    # c=np.sin(b)
    # print(a)
    # print(b)
    # print(c)
    # np.savez("runoob.npz",a,b,sin_array=c)
    # r=np.load("runoob.npz")
    # print(r.files)
    # print(r["arr_0"])
    # print(r["arr_1"])
    # print(r["sin_array"])


    '''
    numpy.savetxt() --> 以简单的文本文件格式存储数据
    numpy.loadtxt() --> 读取文本文件格式数据
    '''
    # a2=np.array([1,2,3,4,5])
    # np.savetxt('../data/out.txt',a2)
    # b=np.loadtxt('../data/out.txt')
    # print(b)

    '''
    使用delimiter参数
    '''
    # import numpy as np
    #
    # a=np.arange(0,10,0.5).reshape(4,-1)
    # np.savetxt('../data/out2.txt',a,fmt="%d",delimiter=",")
    # b=np.loadtxt('../data/out2.txt',delimiter=",")
    # print(b)
