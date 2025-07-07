input = 20


def find_prime_list_under_number(number):
    prime = [True for i in range(input + 1)]

    for i in range(2, int(input ** 0.5) + 1):
        if prime[i]:
            j = 2
            while i * j <= input:
                prime[i * j] = False
                j += 1

    arr = []
    for i in range(2, input + 1):
        if prime[i]:
            arr.append(i)

    return arr

result = find_prime_list_under_number(input)
print(result)
