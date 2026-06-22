def password_strength(password):
    if len(password) < 8:
        return "weak"
    elif len(password)< 12:
        return "medium"
    else:
        return "strong"
password = input("Enter your password:")
strength = password_strength(password)
print("Password strength: ", strength) 