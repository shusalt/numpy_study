import numpy as np
'''
numpy数据类型对象
'''
if __name__ == '__main__':
    '''实例1'''
    # dt=np.dtype(np.int32)
    # print(dt)

    '''实例二'''
    # dt=np.dtype('i4')
    # print(dt)

    '''实例三'''
    # dt=np.dtype('<i4')
    # print(dt)

    '''实例4'''
    # dt=np.dtype([('age',np.int8)])
    # print(dt)

    '''实例5'''
    # dt=np.dtype([('age',np.int8)])
    # a=np.array([(10,),(20,),(30)],dtype=dt)
    # print(a)

    '''实例6'''
    # dt=np.dtype([('age',np.int8)])
    # a=np.array([(10,),(20,),(30,)],dtype=dt)
    # print(a['age'])

    '''实例7，结构化数据类型'''
    # student=np.dtype([('name','S20'),('age','i1'),('marks','f4')])
    # print(student)

    '''实例8'''
    student=np.dtype([('name','S20'),('age','i1'),('marks','f4')])
    a=np.array([('abc',21,50),('xyz',18,75)],dtype=student)
    print(a['age'])
    