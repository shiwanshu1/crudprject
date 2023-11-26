def is_prime(num):
    if num <= 1:
        return False
    for divisor in range(2, int(num ** 0.5)+1):
        if num % divisor == 0:
            print(f"{num} is divided by {divisor}")
            return False
        return True

# Example
num = input()
if is_prime(int(num)):
    print(num,"is a p n")
else:
    print(num,"is nt a p n")