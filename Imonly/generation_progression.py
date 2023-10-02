def generate_sequence(n):
    sequence = list(range(1, n + 1))
    return sequence

# Задайте число n, до якого буде генеруватися послідовність
n = int(input("Введіть число n: "))

result = generate_sequence(n)
print("Послідовність цифр:", result)
