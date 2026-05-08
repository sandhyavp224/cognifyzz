temp = float(input("Enter temperture value : "))
unit = input("Enter uniit(C/F): ").upper()

if unit == "C":
    fahr = (9 / 5) * temp + 32
    print(f"{temp} in {unit} to  Fahrenheit: ", round(fahr, 2))
elif unit == "F":
    cels = (5/9) * (temp - 32)
    print(f"{temp} in {unit} to Celsius: ", round(cels, 2))
else:
    print("Invalid unit. Please enter C or F")
    