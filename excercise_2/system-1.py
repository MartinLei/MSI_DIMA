import hashlib
import time

# Bruteforce methode
def brute_force(hash_value):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password_length = 5

    for c1 in characters:
        for c2 in characters:
            for c3 in characters:
                for c4 in characters:
                    for c5 in characters:
                        password = c1 + c2 + c3 + c4 + c5
                        hashed_password = hashlib.sha1(password.encode()).hexdigest()
                        if hashed_password == hash_value:
                            return password
    return None


# Example usage
hash_value = '7738d1909d7dee18196f733d0d508d871d05cc80'

start_time = time.time()
print(f"Starting to decrypt hash ({start_time}): {hash_value}")
password = decrypt_sha1_hash(hash_value)
end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")
if password:
    print(f"Decrypted password: {password}")
else:
    print("Password not found.")

# takes around 666.13 sec = ca. 11 min, Result= MsI42