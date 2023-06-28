def reverseString(s):
    stack = []
    result_list = []
    for element in s:
        stack.append(element)
    for _ in range(len(stack)):
        result_list.append(stack.pop())
    return result_list

reverseString(["H","a","n","n","a","h"])

