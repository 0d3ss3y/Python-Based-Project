# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 11:55:13 2025

@author: dell
"""       
    
def enter_age() -> int:
    age = input("Enter your age: ")
    if age.isdigit():
        return int(age)
    return 0


def enter_gender() -> str:
    accepted_genders = ["m","f"]
    gen = input("Enter your Gender: ").lower()[0]
    
    if gen in accepted_genders:
        return gen
    return "N"
    

def verify_number(num) -> bool:
    return int(num) in range(1,6) and num.isdigit()


def enter_hobbies() -> list:
    hobs = []
    
    num_of_hobbies = input("Number of Hobbies (Max = 5): ")
    flag = verify_number(num_of_hobbies)
    
    if flag:
        for i in range(int(num_of_hobbies)):
            hobby = input("Enter a hobby: ")
            
            if hobby not in hobs and hobby != "":
                hobs.append(hobby)
        
    else:
        print("Invalid Entry")
        return []


def enter_contact() -> list:
    category = ["email","phone number"]
    answer = []
    
    for cate in category:
        ans = input(f"Enter your {cate}: ")
        answer.append(ans)
        
    return answer


def main():
    user =  input("Enter your Name: ")
    age = enter_age()
    gender = enter_gender()
    hobbies = enter_hobbies()
    contact = enter_contact()
    


if __name__ == "__main__":
    main()