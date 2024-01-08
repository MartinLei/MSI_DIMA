import time


def std_python(base, exponent, modolo):
    start_time = time.time_ns()   
    result = pow(base, exponent, modolo)
    end_time = time.time_ns()
    elapsed_time = (end_time - start_time) / 1_000_000_000 
    print(f"  {base}^{exponent} mod {modolo} = {result}. Elapsed time {elapsed_time} ms")


def lecture(base, exponent, modolo):
    start_time = time.time_ns()
    
    result = 1
    base = base % modolo  # Reduce the base modulo modulus
    while exponent > 0:
        # If the least significant bit of exponent is 1, multiply the result with base
        if exponent % 2 == 1:
            result = (result * base) % modolo
        # Right shift the exponent (equivalent to integer division by 2)
        exponent = exponent >> 1
        # Square the base
        base = (base * base) % modolo

    end_time = time.time_ns()
    elapsed_time = (end_time - start_time) / 1_000_000_000 
    print(f"  {base}^{exponent} mod {modolo} = {result}. Elapsed time {elapsed_time} ms")


if __name__ == "__main__":
    print("Using python's pow function:")
    std_python(base=3, exponent=11, modolo=5)
    std_python(base=5, exponent=99, modolo=11)
    std_python(base=50, exponent=529, modolo=13)
    std_python(base=50, exponent=999, modolo=17)

    print("\n\nUsing algorithm from page 41 of the lecture")
    lecture(base=3, exponent=11, modolo=5)
    lecture(base=5, exponent=99, modolo=11)
    lecture(base=50, exponent=529, modolo=13)
    lecture(base=50, exponent=999, modolo=17)
