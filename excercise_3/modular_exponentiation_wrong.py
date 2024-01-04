import numpy as np
import time

def modular_expo(base, exponent, modolo):
    expos = np.array([]) 
    print(f"1. Deconstruct {base}^{exponent} to therms of power two:")
    exponent_bin = bin(exponent)[2:]  # Remove '0b' prefix and convert to string
    print(f"- The binary representation of {exponent} is: {exponent_bin}")
    base_two_exponent = len(exponent_bin) -1
    for digit_bin in exponent_bin:
        number_exponent = int(digit_bin) * np.power(2, base_two_exponent)
        print(f"  {digit_bin} * 2^{base_two_exponent} = {number_exponent}")

        expos = np.append(expos, number_exponent)

        base_two_exponent -= 1

    # expos[expos != 0] filter out zeros
    print(f"- All neccesary therms of power two to construct {base}^{exponent} ->", expos[expos != 0])  

    squered_modolo_num = np.array([]) 
    print(f"2. Successvley squaring base {base}:")  
    index = 1
    squere_number = 1
    while squere_number <= expos[0]: # expos[0] - First Element has highes Exponent
        power = np.power(base, squere_number) # Buffoverlof to high numbers
        residue = np.mod(power, modolo) 
        print(f"  {base}^{squere_number} mod {modolo} = {residue}")
        squered_modolo_num =  np.append(residue, squered_modolo_num)

        squere_number = np.power(2,index)
        index += 1

    print(f"3. Calculate product:")  
    product = 1
    for i in range(0, len(expos)):
        if expos[i] > 0:
            product *= squered_modolo_num[i]
        print(f"  expos:{expos[i]} squerd_modolo:{squered_modolo_num[i]} => product {product}")

    print(f"4. Modolo Product:")  
    result = np.mod(product, modolo)        
    print(f"  {product} mod {modolo} = {result}\n")
    return result   

def modular_expo_track_time(base, exponent, modolo):
    start_time = time.time_ns()   
    result = modular_expo(base, exponent, modolo)
    end_time = time.time_ns()
    elapsed_time = (end_time - start_time) / 1_000_000 
    print(f"  {base}^{exponent} mod {modolo} = {result}. Elapsed time {elapsed_time} ms")

if __name__ == "__main__":
    # Right
    modular_expo_track_time(base=3, exponent=11, modolo=5)
    # Wrong because of -> np.power(base, squere_number)
    modular_expo_track_time(base=5, exponent=99, modolo=11)
    modular_expo_track_time(base=50, exponent=529, modolo=13)
    modular_expo_track_time(base=50, exponent=999, modolo=17)