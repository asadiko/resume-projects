nums = [2,7,11,15]
target = 9

result = []
# Dictionary to store the difference and its index
index_map = {}
# Loop for each element
for i, n in enumerate(nums):
    # Difference which needs to be checked
    difference = target - n
    if difference in index_map:
          result.append(i)
          result.append(index_map[difference])
          break
    else:
          index_map[n] = i
print(result)