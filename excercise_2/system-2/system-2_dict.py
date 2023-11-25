# System 2 is not possible with brute force, because of time needed of 26614 years, 3 days, 44 minutes, 28 seconds

import hashlib
import time

hash_to_crack = "e39156538e3e7193fdf6356469fa7414d078f97e"
#hash_to_crack = "fb909c8945c54c067fbdfd7da802633fd12e6a2b"

def check_password(password):
    return hashlib.sha1(password.encode()).hexdigest() == hash_to_crack

def dictonary_attack(dictionary):
    start_time = time.time()
    number_of_checks = 0

    password_found = False
    for word in dictionary:
        word = word.replace("\n", "")
        if len(word) == 10:
            number_of_checks += 1
            if check_password(word):
                password_found = True
                break

    if password_found == True:
        print(f"Password found: {word}")
    else:
        print("Password not found in dictionary")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time} seconds for {number_of_checks} checks.\n")
#------------------------------------------------------------------------

#Second try rainbow attack

def main():
    with open("./system-2/password_1_000_000.txt", "r") as file:
        dictionary = file.readlines()
    dictonary_attack(dictionary)

    # Try to attack with the assumption that Mrs Stähle was too lazy and simply used the first password and after this just numbers
    with open("./system-2/password_system2_dict_FirstPasswordOnlyNumbers.txt", "r") as file:
        dictionary = file.readlines()
    dictonary_attack(dictionary)
    print("\n")

if __name__ == "__main__":
    main()
