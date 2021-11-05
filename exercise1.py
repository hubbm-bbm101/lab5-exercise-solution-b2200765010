N = int(input("Number: "))


def sum_of_odds(number):
    odd_numbers = []

    for i in range(1, number + 1):
        if i % 2 != 0:
            odd_numbers.append(i)

    return sum(odd_numbers)


def average_of_evens(number):
    even_numbers = []

    for i in range(1, number + 1):
        if i % 2 == 0:
            even_numbers.append(i)

    return sum(even_numbers) / len(even_numbers)


def return_all(N):
    return f"Sum of odd numbers is :{sum_of_odds(N)}, Average of even numbers is :{average_of_evens(N)}"


print(return_all(N))
