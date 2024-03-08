option = int(input("1 for Encoding & 2 for Decoding"))
if (option == 1):
    a=input("enter a string")
    if len(a)<=2:
        a=a[::-1]
        print(a)
    elif len(a)>2:
        add1=input("enter 3 alphabets to the start")
        add2=input("enter 3 alphabets to the end")
        modified=a[1:]+a[0]
        add=add1+modified+add2
        print(add)
    
elif (option == 2):
    b=input("enter the word to decode")
    if len(b)<=2:
        b=b[::-1]
        print(b)
    elif len(b)>2:
        modified = list(b)
        modified.pop(0)
        modified.pop(0)
        modified.pop(0)
        modified.pop(3)
        modified.pop(3)
        modified.pop(3)
        new = str(modified)
        new = new[::-1]
        print(new)
else:
    print("Go back And CHoose 1-2")
