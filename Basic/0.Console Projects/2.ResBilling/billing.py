# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 18:49:32 2025

@author: dell
"""
def enter_subtotal() -> float:
    try:
        sub = float(input("Meal Subtotal: "))
        return sub
    except TypeError:
        print("Invalid input")


def enter_tax_rate(sub) -> float:
    try:
        rate = float(input("Tax Rate: "))
        
        if rate == 0.00:
            return sub
        else:
            return sub * float(rate/100)

    except TypeError:
        print("Invalid input")   


def select_tip_percent(sub) -> float:
    tip_option = [0,5,10,15,20]
    
    print()
    for opt in tip_option:
        print(f"{opt}%", end=" ")
        
    try:
        selected_opt = int(input("\nEnter Tip: ")) 
        
        if selected_opt == 0:
            return sub
        elif selected_opt in tip_option:
            return sub * float(selected_opt/100)
        
    except (ValueError,TypeError):
        print("Invalid Option")
    

def enter_party_size(total) -> float:
    try:
        party = int(input("\nParty Size: "))
        return float(total/party)
    except TypeError:
        print("Invalid input")
        

def bill(sub, tax, tip, total, per):
    print("""
Subtotal: {}
Tax: {}
Tip: {}
Total: {}
Each person owes: {}    
""".format(sub, tax, tip, total, per))


def main():
    print("__Billing__")
    
    sub = enter_subtotal()
    rate = enter_tax_rate(sub)
    tip = select_tip_percent(sub)
    total = sub + tip + rate
    per_person = enter_party_size(total)
    bill(sub,rate,tip,total,per_person)
    
    


if __name__ == "__main__":
    main()