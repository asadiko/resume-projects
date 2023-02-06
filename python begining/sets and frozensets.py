fruits = {"Apple", "Banana", "Cherry", "Apple", "Kiwi"}
basket = frozenset(fruits)

print('Unique elements:', basket)

# Add new fruit throws an error!
fruits.add("Orange")
print('After adding new element:', fruits)
numbers1 = frozenset([1, 2, 3, 4, 5])
numbers2 = frozenset([2, 3, 4, 5])
# combinin both sets to one using '|' or using union()
combined = numbers1.union(numbers2)
print('combininng of two sets: ', combined )
# Selecting common elements using "&" operator
# You can also use intersection() method
common = numbers1.intersection(numbers2)
print('common numbers: ', common)
# Selecting elements which are not common using "-" operator
# You can also use difference() method
not_common = numbers1.difference(numbers2)
print('not common: ', not_common)
# Membership testing
# It returns True if sets (frozenset) have no common items otherwise False
Disjoint = numbers1.isdisjoint(numbers2)
print("Disjoint:", Disjoint)
# It returns True if all the items of a set (frozenset) are common in another set (frozenset)
Subset = numbers1.issubset(numbers2)
print("Subset:", Subset)
# It returns True if a set (frozenset) has all items present in another set (frozenset)
Superset = numbers1.issuperset(numbers2)
print("Superset:", Superset)
