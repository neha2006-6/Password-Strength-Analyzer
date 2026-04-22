import getpass

def basic_check(password):
    result = {}
    result["length"] = len(password) >= 8
    
    common = ["123456", "password", "qwerty"]
    result["not_common"] = password not in common
    
    for key, value in result.items():
        status = "✅" if value else "❌"
        print(f"{status} {key}")


password = getpass.getpass("Enter your password: ")
basic_check(password)