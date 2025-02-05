from math import gcd
from functools import reduce

def can_organize_books(shelf):
    frequency = {}
    for book in shelf:
        if book in frequency:
            frequency[book] += 1
        else:
            frequency[book] = 1
    freq_values = list(frequency.values())
    def compute_gcd_of_list(numbers):
        return reduce(gcd, numbers)
    
    overall_gcd = compute_gcd_of_list(freq_values)
    if overall_gcd > 1:
        return "YES"
    else:
        return "NO"
shelf = [1234567, 1234567, 2345678, 2345678, 3456789, 3456789, 1234567, 2345678, 3456789, 4567890, 4567890, 5678901, 5678901, 6789012, 6789012, 1234567, 2345678, 3456789, 4567890, 5678901, 4567890, 5678901]

result = can_organize_books(shelf)
print(result)

#To solve this One I had to use my high school maths, I needed to find out if it possible to put the books into one or more sets such that each set has exactly x copies of the same book,
#where x > 1. This means that the number of copies of each book must be divided by some common integer x > 1.
#Python script above to shows if the books can be organized into valid sets correctly.