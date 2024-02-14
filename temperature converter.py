m= str(input("A for Celsius, B for Fahrenheit: "))
if m == "A":
    temp= int(input("What is the temperature in Celsius? "))
    value= (temp * (9/5) +32)
    print(f"The temperature is {value} fahrenheit")
elif m == "B":
    wemp= int(input("What is the temperature in Fahrenheit? "))
    walue= ((wemp-32) * (5/9))
    print(f"The temperature is {walue} celsius")
else:
    print("this isn't a valid temperature")

#2

We= int(input("What is the grade?: "))
if We < 60:
    print("F")
elif We range(60, 69):
    print("D")
elif We range:(70, 79):
    print("C")
elif We range(80, 89):
    print("B")
elif We range(90, 100):
    print("A")