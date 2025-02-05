def find_duplicates(outcomes):
    frequency = {}
    for outcome in outcomes:
        if outcome in frequency:
            frequency[outcome] += 1
        else:
            frequency[outcome] = 1
    duplicates = [outcome for outcome, count in frequency.items() if count == 2]
    
    return duplicates
outcomes = [123456, 234567, 123347, 456789, 567890, 678901, 789012, 890123, 901234, 112233, 223344, 334455, 789012, 222234, 123347]
result = find_duplicates(outcomes)
print(result)

#To solve this problem, I needed to identify the two duplicate outcomes in the given array. The array contains all unique outcomes from 0 to n-1,
#  but to a system error, two outcomes are repeated. tricky part is to find these two duplicates,
# the easiest way being python script.