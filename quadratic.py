def quadratic_formula(a, b, c):

    import math
    try:
        nn = (-b + math.sqrt((b**2 - (4*a*c))))/(2*a)
        aa = (-b - math.sqrt((b**2 - (4*a*c))))/(2*a)
        if aa == nn:
            new = "Only 1 root: " + str(round(nn, 3))
            return new
        else:
            new = "The roots are: " + str(round(nn, 3)) + " and " + str(round(aa, 3))
            return new
    except:
        return "No roots"

a, b, c = int(input("Input the a value: ")), int(input("Input the b value: ")), int(input("Input the c value: "))
print(quadratic_formula(a, b, c))