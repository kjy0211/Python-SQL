def solution(str1, str2):
    result = ''
    for i in range(0, len(str1)):
        result += str1[i] + str2[i]
    return result