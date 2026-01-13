def add(a,b):
    return a+b

def divide(a,b):
    try:
        c = a/b 
    except ZeroDivisionError:
        raise ZeroDivisionError
    except ValueError:
        raise ValueError
    else: 
        return c 
    

