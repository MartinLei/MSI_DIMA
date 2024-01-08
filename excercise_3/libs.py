import time


def std_python(base, exponent, modolo):
    start_time = time.time_ns()   
    result = pow(base, exponent, modolo)
    end_time = time.time_ns()
    elapsed_time = (end_time - start_time) / 1_000_000_000 
    print(f"  {base}^{exponent} mod {modolo} = {result}. Elapsed time {elapsed_time} ms")


if __name__ == "__main__":
    print("Using python's pow function:")
    std_python(base=3, exponent=11, modolo=5)
    std_python(base=5, exponent=99, modolo=11)
    std_python(base=50, exponent=529, modolo=13)
    std_python(base=50, exponent=999, modolo=17)