import re

def check_password_strength(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    score = sum(criteria.values())

    print("\n🔍 Password Analysis:")
    for key, passed in criteria.items():
        symbol = "✅" if passed else "❌"
        print(f"{symbol} {key.capitalize()}")

    if score == 5:
        strength = "🟢 STRONG"
    elif 3 <= score < 5:
        strength = "🟠 MEDIUM"
    else:
        strength = "🔴 WEAK"

    print(f"\n🧠 Strength Score: {score}/5 → {strength}")
    return score, criteria

def suggest_improvements(criteria):
    suggestions = {
        "length": "Increase password length to at least 8 characters.",
        "uppercase": "Add at least one UPPERCASE letter (A-Z).",
        "lowercase": "Add at least one lowercase letter (a-z).",
        "digit": "Include at least one number (0-9).",
        "special": "Add a special character (e.g. @, #, !, $, %)."
    }

    print("\n💡 Suggestions to Improve:")
    for key, passed in criteria.items():
        if not passed:
            print(f"- {suggestions[key]}")

def main():
    print("🔐 Password Strength Checker - SkillCraft Internship")
    password = input("Enter your password: ")

    score, criteria = check_password_strength(password)

    if score < 5:
        suggest_improvements(criteria)

if __name__ == "__main__":
    main()
