import numpy as np
'''字符串函数'''

if __name__ == '__main__':
    '''numpy.char.add() --> 进行字符串连接'''
    # print('连接两个字符串')
    # print(np.char.add(['hello'],['xyz']))
    # print('\n')
    #
    # print('连接示例')
    # print(np.char.add(['hello','hi'],['abc','xyz']))

    '''numpy.char.multiply() --> 执行多重连接'''
    # print(np.char.multiply('Runoob ',3))

    '''numpy.char.center() --> 字符串居中,并使用指定字符在左右填充'''
    # print(np.char.center('Runoob',20,fillchar='*'))

    '''numpy.char.capitalize() --> 将字符串的第一个字符转换位大写'''
    # print(np.char.capitalize('runoob'))

    '''numpy.char.title --> 将每个单词首字符转换成大写'''
    # print(np.char.title('i like runoob'))

    '''numpy.char.lower --> 将字符串转换为小写'''
    # print(np.char.lower(['RUNOOB','GOOGLE']))

    '''numpy.char.upper() --> 将字符串转换为大写'''
    # print(np.char.upper('runoob'))

    '''numpy.char.split(str,sep) --> 分割字符'''
    # print(np.char.split('i like runoob'))
    # print(np.char.split('www.runoob.com',sep='.'))

    '''numpy.char.splitlines() --> 以换行符作为分割符，对字符串进行分割'''
    # print(np.char.splitlines('i\nlike runnoob'))

    '''numpy.char.strip() --> 剔除字符串的首或者尾的特定字符'''
    # print(np.char.strip('ashok arunooba','a'))
    # print(np.char.strip(['arunooba','admin','java'],'a'))

    '''numpy.char.join() --> 指定字符来连接数组中的元素或者字符串'''
    # print(np.char.join(':','runoob'))
    # print(np.char.join([':','-'],['runoob','google']))

    '''numpy.char.replace --> 使用新字符串替换字符串中的子字符串'''
    # print(np.char.replace('i like runoob','oo','cc'))

    '''numpy.char.encode() --> 对字符进行编码'''
    a=np.char.encode('ruuoob','cp500')
    print(a)

    '''numpy.char.decode() --> 对字符进解码'''
    print(np.char.decode(a,'cp500'))

