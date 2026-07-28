#Given an list of strings, return another list containing all of its longest strings.
#Example For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
#solution(inputArray) = ["aba", "vcd", "aba"].

def longest_len(inputArray):
    max_len = 0
    for i in inputArray:
        if len(i) > max_len:
            max_len = len(i)
            
    result = []
    for i in inputArray:
        if len(i) == max_len:
            result.append(i)
            
    return result

input_list = ["aba", "aa", "ad", "vcd", "aba"]
print(longest_len(input_list))