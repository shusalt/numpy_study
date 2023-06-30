import re
if __name__ == '__main__':

    str1 = "这是一个测试字符串，包含区字符。"

    pattern = r"区(.*)"

    result = re.search(pattern, str1)

    if result:

        print(result.group(1))

    else:

        print("未找到匹配项")
