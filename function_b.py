# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    sum = 0

    while sum < 1000:
        input_int = int(input("Enter a number: "))
        if input_int == 0:
            break
        sum += input_int

    return sum

    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """


if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
