temp_units = {
    "C" : "Celsius",
    "F" : "Fahrenheit",
    "K" : "Kelvin"
}

formulas = {
    "Celsius to Fahrenheit": lambda c: (c * 9/5) + 32,
    "Fahrenheit to Celsius": lambda f: (f - 32) * 5/9,
    "Celsius to Kelvin": lambda c: c + 273.15,
    "Kelvin to Celsius": lambda k: k - 273.15,
    "Fahrenheit to Kelvin": lambda f: (f - 32) * 5/9 + 273.15,
    "Kelvin to Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32
}

def validate_selection(initial,target):
    return initial in temp_units.keys() and target in temp_units.keys()
    

def convertor(unit_to,unit_from,temp):
    unit_to_name = temp_units.get(unit_to)
    unit_from_name = temp_units.get(unit_from)
    conversion = formulas[f"{unit_from_name} to {unit_to_name}"](temp)
    print(f"{temp}°{unit_from} is equal to {conversion}°{unit_to}")


def main():
    temperature = float(input(("Temperature: ")))
    initial = input("From Unit ['K','C','F']: ").upper()
    target = input("To Unit ['K','C','F']: ").upper()
    
    if initial == target:
        print(f"{temperature} {initial} is equal to {temperature} {target}")
    else:
        flag = validate_selection(initial,target)
        
        if not flag:
            print("Invalid Selection")
        else:
            convertor(target, initial, temperature)
            

if __name__ == '__main__':
    main()