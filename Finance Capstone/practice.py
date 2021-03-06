def reverse(string):
    if len(string) == 1:
        return string[0]
    if len(string) == 2:
        return string[-1] + string[0]
    else:
        return string[-1] + reverse(string[1:-1]) + string[0]

def is_palindrome(string):
    string = string.replace(" ", "") 
    string = string.replace("'", "")
    if len(string) == 1:
        return True
    else:
        if string[0] == string[-1]:
            return is_palindrome(string[1:-1])
        else:
            return False

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def reverse_list(lst):
    if len(lst) == 1:
        return [lst[0]]
    if len(lst) == 2:
        return [lst[-1]] + [lst[0]]
    else:
        return [lst[-1]] + reverse_list(lst[1:-1]) + [lst[0]]

def fibonacci(n):
    if n <= 1:
        return n
   # if n == 2:
    #    return n
    else:
        return (fibonacci(n-1) + fibonacci(n - 2))

def flatten_list(lst):
    