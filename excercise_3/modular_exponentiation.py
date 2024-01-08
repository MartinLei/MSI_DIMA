import numpy as np
import time

def modular_expo(base, exponent, modulo):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulo   
        exponent //= 2
        base = (base * base) % modulo
    return result

def modular_expo_track_time(base, exponent, modulo):
    start_time = time.time_ns()   
    result = modular_expo(base, exponent, modulo)
    end_time = time.time_ns()
    elapsed_time = (end_time - start_time) / 1_000_000 
    print(f"  {base}^{exponent} mod {modulo} = {result}. Elapsed time {elapsed_time} ms")

if __name__ == "__main__":
    modular_expo_track_time(base=3, exponent=11, modulo=5)
    modular_expo_track_time(base=5, exponent=99, modulo=11)
    modular_expo_track_time(base=50, exponent=529, modulo=13)
    modular_expo_track_time(base=50, exponent=999, modulo=17)