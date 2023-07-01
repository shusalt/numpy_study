import numpy as np
'''numpy 字节交换'''
if __name__ == '__main__':
    a=np.array([1,256,8755],dtype=np.int16)
    print(a)
    print(map(hex,a))
    print(a.byteswap(True))
    print(map(hex,a))