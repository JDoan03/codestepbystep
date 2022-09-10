# Write a function named has_duplicate_value that accepts a dictionary from
# strings to strings as a parameter and returns True if any two keys map to
# the same value. For example, if a dictionary named m stores {'Marty':
# 'Stepp', 'Stuart': 'Reges', 'Jessica': 'Miller', 'Amanda': 'Camp', 'Meghan':
# 'Miller', 'Hal': 'Perkins'}, the call of has_duplicate_value(m) would return
# True because both 'Jessica' and 'Meghan' map to the value 'Miller'. Return
# False if passed an empty or one-element dictionary. Do not modify the dictionary
# passed in.


def has_duplicate_value(dict):
    unilist = list(dict.values())
    if len(dict) == 0 or len(dict) == 1:
        return False
    else:
        if len(set(unilist)) == len(dict):
            return False
        else:
            return True


has_duplicate_value({'Marty': 'Stepp', 'Stuart': 'Reges', 'Jessica': 'Miller', 'Amanda': 'Camp', 'Hal': 'Perkins'})  # False
has_duplicate_value({'Marty': 'Stepp', 'Stuart': 'Reges', 'Jessica': 'Miller', 'Amanda': 'Camp', 'Meghan': 'Miller', 'Hal': 'Perkins'})  #True
has_duplicate_value({'Kendrick': 'Perkins', 'Stuart': 'Reges', 'Jessica': 'Miller', 'Bruce': 'Reges', 'Hal': 'Perkins'})  # True
has_duplicate_value({'Mario': 'Mario'})  # False
has_duplicate_value({})  # False
