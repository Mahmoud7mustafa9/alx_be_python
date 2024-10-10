def safe_divide(numerator, denominator):
    try:
      if float(denominator)== 0:
        raise ZeroDivisionError
      x= float(numerator)/float(denominator)
      return f'The result of the division is {x}'
    except ZeroDivisionError:
      return f'Error: Cannot divide by zero.'
    except ValueError :
      return f'Error: Please enter numeric values only.'