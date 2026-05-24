
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)

def count_vowels(text):
    vowels = 'aiueoAIUEO'
    return sum(1 for char in text if char in vowels)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
