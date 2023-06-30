import pandas as pd
import cn2an
'''中文数字转换成阿拉伯数字'''
def function2(st):
    output=cn2an.transform(st,'cn2an')
    return output

if __name__ == '__main__':
    a='十三栋'
    b=function2(a)
    print(b)


