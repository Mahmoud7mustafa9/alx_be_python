

def perform_operation(number1,number2,operate):
    if operate == "add":
        return number1 + number2
    elif operate == "subtract":
        return number1 - number2
    elif operate == "multiply":
        return number1 * number2
    elif operate == "divide":
        if number2 == 0:
            return "you can not divide those numbers"
        else :
            return number1 / number2 
