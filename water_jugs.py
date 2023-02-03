from sys import exit as exit_
max_m = int(input("Enter max capacity of Jug M: "))
max_n = int(input("Enter max capacity of Jug N: "))
jug_m = 0
jug_n = 0
target = int(input("Enter target capacity: "))
# jug m is the smaller jug
# jug n is the larger jug, or the target jug
def get_gcd(m, n):
    if m < n:
        s = m
    else:
        s = n
    for i in range(1, s):
        if(m%i == 0 and n%i == 0):
            gcd = i
    return gcd
    
def fill(jug_m, max_m):
    if jug_m != 0:
        return jug_m
    jug_m = max_m
    return jug_m

def pour(jug_m, jug_n, max_n):
    #pour m into n while n isn't full
    if jug_n == max_n:
        return max_n, jug_m
    if jug_n < max_n:
        for i in range(1,jug_m+1):
            jug_m -= 1
            jug_n += 1
            if jug_m == 0 or jug_n == max_n:
                return jug_n, jug_m
    return jug_n, jug_m

def check(jug_n, target_capacity, jug_m, steps):
    if jug_n == target_capacity:
        print("\nSolution found")
        print("n: "+str(jug_n))
        print("m: "+str(jug_m))
        print("Number of iterations: " + str(steps))
        exit_(0)
    #print_arrow()

def empty():
    pass

def print_arrow():
    print("""   🡻""")

def iterate(jug_m, jug_n, max_m, max_n, target):
    j = 0
    print(f"Goal condition is ({target}, n)")
    print(f"({jug_n, jug_m})")
    steps = 1
    while j<100:
        print_arrow()
        jug_m = fill(jug_m, max_m)
        steps += 1
        print(f"({jug_n, jug_m})")
        print_arrow()
        jug_n, jug_m = pour(jug_m, jug_n, max_n)
        steps += 1
        print(f"({jug_n, jug_m})")
        check(jug_n, target, jug_m, steps)
        j += 1
        if jug_n == max_n:
            jug_n = 0
    print("Solution not found")

gcd = get_gcd(max_m, max_n)

print("\nGCD: " + str(gcd))

print("\ntarget '%' gcd: " + str(target%gcd))

if target % gcd != 0:
    print("\nSolution does not exist")
    exit_(0)

if target > max_n:
    print("\nSolution does not exist")
    exit_(0)

iterate(jug_m, jug_n, max_m, max_n, target)