import hashlib
import time

# tries every word in the file with len(word) <= 10, if smaller than 10, adds numbers from to the end until len(word) == 10. Hallo -> Hallo12345
def decrypt(sha1_hash):
    with open(file_path, "r") as file:
        for word in file:
            word = word.strip() # remove \n
            if len(word) <= 10:
                for i in range(10 - len(word)):
                    word += str(i+1)
                hashed_password = hashlib.sha1(word.encode()).hexdigest()
                if hashed_password == sha1_hash:
                    return word


# Path to file
file_path = "wortliste.txt"
hash_value = "e39156538e3e7193fdf6356469fa7414d078f97e"
print(f"Starting to decrypt hash: '{hash_value}'")

start_time = time.time()
result = decrypt(hash_value)
end_time = time.time()

if result:
    print(f"Decrypted password: {result}")
else:
    print("Password not found.")

execution_time = end_time - start_time
