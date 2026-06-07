# Password strength checker

pw = input("Write your password: ")

print("\n--- PASSWORD CHECK RESULTS ---\n")

# Check conditions
if len(pw) <= 5:
    print("❌ Invalid: Password must be at least 6 characters long")

if not any(char.isdigit() for char in pw):
    print("❌ Add at least one number to your password")

if not any(char.islower() for char in pw):
    print("❌ Add lowercase character to your password")

if not any(char.isupper() for char in pw):
    print("❌ Add uppercase character to your password")

if not any(char in '!@#$%^&*' for char in pw):
    print("❌ Add special characters (!@#$%^&*)")

# If all conditions pass
if (len(pw) > 5 and
    any(char.isdigit() for char in pw) and
    any(char.islower() for char in pw) and
    any(char.isupper() for char in pw) and
    any(char in '!@#$%^&*' for char in pw)):
    print("\n✅ SUCCESS: Your password is strong and valid!")
else:
    print("\n⚠️ Please fix the issues above to create a secure password.")