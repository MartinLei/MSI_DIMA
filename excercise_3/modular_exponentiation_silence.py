import numpy as np
import time

def modular_expo(base, exponent, modolo):
    expos = np.array([]) 
    exponent_bin = bin(exponent)[2:]  # Remove '0b' prefix and convert to string
    base_two_exponent = len(exponent_bin) -1
    for digit_bin in exponent_bin:
        number_exponent = int(digit_bin) * np.power(2, base_two_exponent)
    
        expos = np.append(expos, number_exponent)

        base_two_exponent -= 1

    squered_modolo_num = np.array([]) 
    index = 1
    squere_number = 1
    while squere_number <= expos[0]: # expos[0] - First Element has highes Exponent
        power = np.power(base, squere_number)
        residue = np.mod(power, modolo) 
        squered_modolo_num =  np.append(residue, squered_modolo_num)

        squere_number = np.power(2,index)
        index += 1

    product = 0
    for i in range(0, len(expos)):
        if expos[i] > 0:
            product += squered_modolo_num[i]

    result = np.mod(product, modolo)        
    return result   

def modular_expo_track_time(base, exponent, modolo):
    start_time = time.time_ns()   
    result = modular_expo(base, exponent, modolo)
    end_time = time.time_ns()
    elapsed_time = (end_time - start_time) / 1_000_000 
    print(f"  {base}^{exponent} mod {modolo} = {result}. Elapsed time {elapsed_time} ms")

if __name__ == "__main__":
    modular_expo_track_time(base=3, exponent=11, modolo=5)
    modular_expo_track_time(base=5, exponent=99, modolo=11)
    modular_expo_track_time(base=50, exponent=529, modolo=13)
    modular_expo_track_time(base=50, exponent=999, modolo=17)