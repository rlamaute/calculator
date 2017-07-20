#this only does integers and rounds up because i'm trash like that
def multiply(a,b):
    return round(a * b, 3)
def divide(a,b):
    if b == 0:
        return "you can't divide by zero you idiot"
    else:
        return round(a/b, 3)
