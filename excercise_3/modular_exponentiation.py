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