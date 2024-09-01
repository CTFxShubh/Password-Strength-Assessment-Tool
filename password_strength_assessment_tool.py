# Password Strength Assessment Tool
# Written by: Shubh Patel
# Cyber Security Intern at Prodigy Infotech
# PRODIGY_CS_Task-03

def assess_password_strength(password):
    """Assess the strength of a given password."""
    criteria = {
        'length': len(password) >= 8,
        'uppercase': any(c.isupper() for c in password),
        'lowercase': any(c.islower() for c in password),
        'numbers': any(c.isdigit() for c in password),
        'special': any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for c in password)
    }
    
    score = sum(criteria.values())
    
    feedback = {
        0: "Very Weak: Password must include uppercase letters, lowercase letters, numbers, and special characters.",
        1: "Weak: Password is missing several criteria. Include more character types.",
        2: "Fair: Password meets some criteria but could be stronger.",
        3: "Good: Password meets most criteria but could be improved.",
        4: "Strong: Password meets all criteria. Good job!",
    }
    
    return feedback[score]

if __name__ == "__main__":
    password = input("Enter a password to assess: ")
    strength = assess_password_strength(password)
    print(strength)

# End of Code 
