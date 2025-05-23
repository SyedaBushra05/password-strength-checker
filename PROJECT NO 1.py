import re

def check_password_strength(password):
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1

    # Check for lowercase
    if re.search(r"[a-z]", password):
        score += 1

    # Check for uppercase
    if re.search(r"[A-Z]", password):
        score += 1

    # Check for numbers
    if re.search(r"[0-9]", password):
        score += 1

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Evaluate strength
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"

# Test it
user_input = input("Enter your password: ")
strength = check_password_strength(user_input)
print("Password Strength:", strength)
