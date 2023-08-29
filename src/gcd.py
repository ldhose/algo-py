# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def find_gcd(num1, num2):
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    q = num1 // num2
    while q > 0:
        remainder = num1%num2
        if remainder == 0:
            return num2
        else:
            num1 = num2
            num2 = remainder
    raise Exception("No gcd for thes combo")        
