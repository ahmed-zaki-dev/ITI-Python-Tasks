#Given the string, check if it is a palindrome. 
#Example For inputString = "aabaa", the output should be solution(inputString) = true;
#For inputString = "abac", the output should be solution(inputString) = false;
#For inputString = "a", the output should be solution(inputString) = true.

while True:
    usr_input = input("Enter your String: ")
    print(usr_input == usr_input[::-1])