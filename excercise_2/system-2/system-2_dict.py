# System 2 is not possible with brute force, because of time needed of 26614 years, 3 days, 44 minutes, 28 seconds

import hashlib
import time

# First try dictonary attack 1_000_000 Problem: Password not in dictonary
def check_password(hash, password):
    return hashlib.sha1(password.encode()).hexdigest() == hash
def dictonary_attack():
    start_time = time.time()
    hash_to_crack = "e39156538e3e7193fdf6356469fa7414d078f97e"

    with open(".\excercise_2\password_1_000_000.txt", "r") as file:
        dictionary = file.readlines()

    password_found = False
    for word in dictionary:
        if check_password(hash_to_crack, word):
            password_found = True
            break

    if password_found == True:
        print(f"Password found: {word}")
    else:
        print("Password not found in dictionary")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time} seconds")
#------------------------------------------------------------------------

#Second try rainbow attack

def main():
    dictonary_attack()
    print("\n")

if __name__ == "__main__":
    main()
