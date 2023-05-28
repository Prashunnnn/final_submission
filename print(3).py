def div(a,b):
    try:
        result=a/b
    except ZeroDivisionError:
        print("cannot be divided by zero")
    else:
        print(f'{num1}divided by{num2}is:{result}')


div(10,5)



    
