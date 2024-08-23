import cmath

def calculate_quadratic_roots():
    a = float(input('Enter coefficient a: '))
    b = float(input('Enter coefficient b: '))
    c = float(input('Enter coefficient c: '))

    d = (b**2) - (4*a*c)

    if d >= 0:
        sol_1 = (-b - d**0.5) / (2*a)
        sol_2 = (-b + d**0.5) / (2*a)
        print('The real solutions are', sol_1, 'and', sol_2)
    else:
        sol1 = (-b - cmath.sqrt(d)) / (2*a)
        sol2 = (-b + cmath.sqrt(d)) / (2*a)
        print('The complex solutions are', sol_1, 'and', sol_2)

if __name__ == "__main__":
    calculate_quadratic_roots()