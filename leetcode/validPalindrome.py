import re


def isPalindrome(s: str) -> bool:
    pattern = r'[-=+, _{};#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]'

    pattern_result = re.sub(pattern, '', s).lower()
    first_s_list: list[str] = [char for char in pattern_result]
    first_s_list.reverse()
    reverse_s_list = ''.join(first_s_list)
    if pattern_result == reverse_s_list:
        return True
    return False

