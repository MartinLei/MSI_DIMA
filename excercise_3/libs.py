import time


def std_python(base, exponent, modulo):
    start_time = time.time_ns()   
    result = pow(base, exponent, modulo)
    end_time = time.time_ns()
    elapsed_time = (end_time - start_time) / 1_000_000_000 
    print(f"  {base}^{exponent} mod {modulo} = {result}. Elapsed time {elapsed_time} ms")


def lecture(base, exponent, modulo):
    start_time = time.time_ns()
    
    result = 1
    base = base % modulo  # Reduce the base modulo modulus
    while exponent > 0:
        # If the least significant bit of exponent is 1, multiply the result with base
        if exponent % 2 == 1:
            result = (result * base) % modulo
        # Right shift the exponent (equivalent to integer division by 2)
        exponent = exponent >> 1
        # Square the base
        base = (base * base) % modulo

    end_time = time.time_ns()
    elapsed_time = (end_time - start_time) / 1_000_000_000 
    print(f"  {base}^{exponent} mod {modulo} = {result}. Elapsed time {elapsed_time} ms")


if __name__ == "__main__":
    print("Using python's pow function:")
    std_python(base=3, exponent=11, modulo=5)
    std_python(base=5, exponent=99, modulo=11)
    std_python(base=50, exponent=529, modulo=13)
    std_python(base=50, exponent=999, modulo=17)

    print("\n\nUsing algorithm from page 41 of the lecture")
    lecture(base=3, exponent=11, modulo=5)
    lecture(base=5, exponent=99, modulo=11)
    lecture(base=50, exponent=529, modulo=13)
    lecture(base=50, exponent=999, modulo=17)
