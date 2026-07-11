import hashlib
def option_selection():
    while True:
        while True:
            try:
                user_choice = int(input("""
========== FILE HASH CHECKER ==========

1. Generate File Hash
2. Exit:
            """))
            except ValueError:
                print("Please only enter a number not any other thing")
            else:
                break
        if user_choice < 1 or user_choice > 2:
            print("Please enter a valid choice")
            continue
        else:
            break
    return user_choice
def generate_hash():
    while True:
        try:
            path = input("Enter the path of file you want to generate hash for")
            with open(path,"rb") as file:
                binary_content = file.read()
        except FileNotFoundError:
            print("Please enter a valid path")
        else:
            break
    while True:
        try:
            option = int(input("""
Chose one Choose algorithm:

1. MD5
2. SHA1
3. SHA256:       """))
        except ValueError:
            print("Please enter only option number")
        else:
            if option < 1 or option > 3:
                print("Please enter a valid option")
                continue
            else:
                if option == 1:
                    md5hash = hashlib.md5()
                    md5hash.update(binary_content)
                    print(f"Your md5 hash is {md5hash.hexdigest()}")
                elif option == 2:
                    sha1hash = hashlib.sha1()
                    sha1hash.update(binary_content)
                    print(f"Your md5 hash is {sha1hash.hexdigest()}")
                elif option == 3:
                    sha256hash = hashlib.sha256()
                    sha256hash.update(binary_content)
                    print(f"Your md5 hash is {sha256hash.hexdigest()}")
                break
def hash_generator():
    while True:
        user_choice=option_selection()
        if user_choice == 1:
            generate_hash()
        elif user_choice == 2:
            print("Goodbye!")
            break
hash_generator()
