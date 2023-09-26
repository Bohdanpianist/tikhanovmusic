import random

# Кількість 4-значних чисел, які потрібно згенерувати
кількість = 1  # Змініть на бажану кількість

for _ in range(кількість):
    random_number = random.randint(1000, 9999)
    print("Випадкове 4-значне число:", random_number)