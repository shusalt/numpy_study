import re
if __name__ == '__main__':


    # def generate_regex():
    #     pattern = r'(.*)(广场|大厦)'
    #
    #     return pattern
    #
    #
    # user_input = 'a中心广场11号'
    #
    # regex = generate_regex()
    #
    # result = re.search(regex, user_input)
    #
    # print("匹配结果：", result.group(0))

    parent_str = "这是一个示例字符串，我们将从中提取不是子字符串的部分"

    sub_str = "一个示例"

    result = [part for part in parent_str.split(sub_str) if part not in sub_str]

    print(''.join(result))
