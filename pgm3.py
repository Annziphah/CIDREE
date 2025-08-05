"""3. Data Structures & Time Complexity
You have a list of 1 million integers and need to check if any two numbers sum to a given target.
Task: Explain an efficient solution and implement it in Python.  """
import random
def has_pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return True
        seen.add(num)
    return False
arr = random.sample(range(1, 10000000), 1000000)
target = 15000000 
result = has_pair_with_sum(arr, target)
print("Pair found:" if result else "No such pair found.")
