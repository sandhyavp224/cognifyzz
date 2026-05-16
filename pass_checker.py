import string

def password_strength(password):
    
    strenght = 0
    if len(password) >= 8:
        strenght += 1
    
    for ch in password:
        if ch.lower():
            strenght += 1
            break
    for ch in password:
        if ch.upper():
            strenght += 1
            break
        
    for ch in password:
        if ch.isdigit():
            strenght += 1
            break
    
    for ch in password:
        if ch in string.punctuation:
            strenght += 1
            break
        
        
        if strenght == 5:
            return " very Strong Password"
        elif strenght == 4:
            return "strong Password"
        elif strenght == 3:
            return "Moderate Password"
        elif strenght == 2:
            return "Weak Password"
        else:
            return "Very Weak Password"
password = input("Enter a password to check its strength: ")
print(password_strength(password))
            
    
    
