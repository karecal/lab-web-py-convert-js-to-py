words  = ["mystery", "brother", "aviator", "crocodile", "pearl", "orchard", "crackpot"]
words2 = ["machine", "subset", "trouble", "starting", "matter", "eating", "truth", "disobedience"]
numbers  = [6, 12, 1, 18, 13, 16, 2, 1, 8, 10]
numbers2 = [2, 6, 9, 10, 7, 4, 1, 9]


def max_of_two_numbers(a, b):
    return a if a >= b else b


def find_longest_word(words):
    if not words:
        return None
    return max(words, key=len)


def sum_numbers(numbers):
    return sum(numbers)


def average_numbers(numbers):
    if not numbers:
        return None
    return sum_numbers(numbers) / len(numbers)


def does_word_exist(words, word):
    if not words:
        return None
    return word in words


if __name__ == "__main__":
    print(max_of_two_numbers(4, 7))           # 7
    print(find_longest_word(words))            # crocodile
    print(sum_numbers(numbers))               # 87
    print(average_numbers(numbers2))          # 6.0
    print(does_word_exist(words2, "truth"))   # True
    print(does_word_exist(words2, "coding"))  # False
