import copy

"""
There are a few cases where you would prefer a deep copy over a shallow copy:
1. Deep copy is necessary when you have nested container objects that you need to modify independently of the original object.
2. If you need to ensure complete isolation of the copied data from the original data, a deep copy is required.
3. When you need to modify nested structures without affecting the original data, deep copy is the best choice.
4. Deep copies ensure that changes to the new object do not affect the original object, and vice versa.
"""

# Here are some common objects you might copy
# 1. List
original_list = [1, 2, 3, 4]

deep_copied_list = copy.deepcopy(original_list)
print('original_list:', original_list)
print('deep_copied_list:', deep_copied_list)
"""
Explanation:
Both shallow and deep copies are the same for flat lists without nested objects,
as there are no nested objects to recursively copy.
"""

# 2. Tuples in a List
original_tuple_list = [(1, 'Alice'), (2, 'Bob')]
deep_copied_tuple_list = copy.deepcopy(original_tuple_list)
print('original_tuple_list:', original_tuple_list)
print('deep_copied_tuple_list:', deep_copied_tuple_list)
"""
Explanation:
Tuples are immutable, so modifying a tuple within the original list would require
creating a new tuple. Therefore, shallow and deep copies behave similarly unless 
the tuples themselves are replaced.
"""

# 3. Lists in a list
original_list_list = [[1, 2], [3, 4]]
deep_copied_list_list = copy.deepcopy(original_list_list)
print('original_list_list:', original_list_list)
print('deep_copied_list_list:', deep_copied_list_list)
"""
Explanation:
Deep copy will recursively copy all nested lists, creating completely independent copies.
Changes to the nested lists in the deep copy will not affect the original lists.
"""

# 4. List in a dictionary
original_dictionary_list = [{'name': 'Wang', 'age': 30}, {'name': 'Bradshaw', 'age': 25}]
deep_copied_dictionary_list = copy.deepcopy(original_dictionary_list)
print('original_dictionary_list:', original_dictionary_list)
print('deep_copied_dictionary_list:', deep_copied_dictionary_list)
"""
Explanation:
Deep copy will create independent copies of each dictionary in the list.
Modifications to the dictionaries in the deep copy will not affect the original dictionaries.
"""
