import copy

"""
There are a few cases that you would prefer shallow copy over deep copy.
1. Shallow copy is commonly used when either you don't have 
nested container objects, or if you wont need to change them.
2. If memory is a concern, shallow copy is a better option.  It does not 
create another copy of the same data, but rather, it creates a new object
that references the original data.
3. If you are only going to read the data in the new object, there is no reason
to create a deep copy, as it would just be a waste of memory.
4. Shallow copies are more performant, if there is no need to keep a copy of the
original data, and the limitations of shallow copy are not a concern.
"""

# Here are some common object you might copy
# 1. List
original_list = [1, 2, 3, 4]

shallow_copied_list = copy.copy(original_list)
print('original_list:', original_list)
print('shallow_copied_list:', shallow_copied_list)
"""
Explanation:
Both shallow and deep copies are the same for flat lists without nested objects,
as there are no nested objects to recursively copy.
"""

# 2. Tuples in a List
original_tuple_list = [(1, 'Alice'), (2, 'Bob')]
shallow_copied_tuple_list = copy.copy(original_tuple_list)
print('original_tuple_list:', original_tuple_list)
print('shallow_copied_tuple_list:', shallow_copied_tuple_list)
"""
Explanation:
Tuples are immutable, so modifying a tuple within the original list would require
creating a new tuple. Therefore, shallow and deep copies behave similarly unless 
the tuples themselves are replaced.
"""

# 3. Lists in a list
original_list_list = [[1, 2], [3, 4]]
shallow_copied_list_list = copy.copy(original_list_list)
print('original_list_list:', original_list_list)
print('shallow_copied_list_list:', shallow_copied_list_list)
"""
Explanation:
Shallow copy will only copy the outer list. Changes to nested lists will affect both
the original and the shallow copy. Deep copy will recursively copy all nested lists,
creating completely independent copies.
"""

# 4. List in a dictionary
original_dictionary_list = [{'name': 'Wang', 'age': 30}, {'name': 'Bradshaw', 'age': 25}]
shallow_copied_dictionary_list = copy.copy(original_dictionary_list)
print('original_dictionary_list:', original_dictionary_list)
print('shallow_copied_dictionary_list:', shallow_copied_dictionary_list)
"""
Explanation:
Shallow copy will copy the list structure but not the nested dictionaries.
Modifications to the dictionaries will affect both the original and the shallow copy.
Deep copy will create independent copies of each dictionary in the list.
"""