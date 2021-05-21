def adding_all_digits_until_one(n):
    if len(str(n)) > 1:
        first = 0
        for _ in str(n):
            _ = int(_)
            second = _
            second = first + _
            first = _
            if len(str(second)) > 1:
                 return adding_all_digits_until_one(int(second)) # If the result contains more than one digit, then it is going to get passed into the function again.
            if str(_) == str(n)[-1]:
                return second # If the iterated item is the last digit of the passed number, the loop is going to stop.
        else:
            return n 
def is_square(n):
    if str(n)[:1] == 0 or 1 or 4 or 5 or 6 or 9:
        return True
    else:
        return False

print(adding_all_digits_until_one(99))
