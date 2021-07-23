# Task 0.6

def maximum(num1, num2, num3):
    if num1 > num2 or num1 > num3:
        return num1
    elif num2 > num1 or num2 > num3:
        return num2
    else:
        return num3    
maximum(4,8,6)
