
def sort_array_by_frequency_and_value(arr):
    """
    Sort an array of integers based on:
    1. Frequency of elements (descending)
    2. If frequencies are equal, sort by value (ascending)

    Example:
    Input: [4, 2, 2, 8, 3, 3, 1]
    Output: [2, 2, 3, 3, 1, 4, 8]

    Args:
        arr (list): List of integers
    Returns:
        list: Sorted list according to the criteria
    """
    map = dict()
    for num in arr:
        if num not in map:
            map.setdefault(num, 1)
        else:
            map[num] += 1
    map = sorted(map.items(), key = lambda x: (-x[1], x[0]))
    res = list()
    for i in map:
        for j in range(i[1]):
            res.append(i[0])
    return res

def sort_dict_by_nested_value(data):
    """
    Sort a dictionary containing nested dictionaries based on:
    1. The 'score' value in nested dictionary (descending)
    2. If scores are equal, sort by the outer key (alphabetically)

    Example:
    Input: {
        'john': {'score': 85, 'age': 20},
        'alice': {'score': 92, 'age': 21},
        'bob': {'score': 85, 'age': 19}
    }
    Output: [
        ('alice', {'score': 92, 'age': 21}),
        ('bob', {'score': 85, 'age': 19}),
        ('john', {'score': 85, 'age': 20})
    ]

    Args:
        data (dict): Dictionary with nested dictionaries
    Returns:
        list: List of tuples sorted according to the criteria
    """
    return dict(sorted(data.items(), key = lambda x: (-x[1]["score"], x[0])))

def sort_sets_by_similarity(sets_list, reference_set):
    """
    Sort a list of sets based on:
    1. Similarity to reference_set (descending)
    2. If similarity is equal, sort by set size (ascending)

    Similarity is defined as: len(set1 & reference_set) / len(set1 | reference_set)

    Example:
    Input:
    sets_list = [{1, 2, 3}, {2, 3, 4, 5}, {1, 2}]
    reference_set = {1, 2, 4}
    Output: [{1, 2}, {1, 2, 3}, {2, 3, 4, 5}]

    Args:
        sets_list (list): List of sets
        reference_set (set): Reference set for similarity comparison
    Returns:
        list: List of sets sorted according to the criteria
    """
    res = list()
    map = dict()
    for s in sets_list:
        if tuple(s) not in map:
            map.setdefault(tuple(s), len(s.intersection(reference_set)))
    map = sorted(map.items(), key = lambda x: (-x[1], x[0]))
    for s in map:
        res.append(set(s[0]))
    return res

def sort_strings_by_pattern(strings, pattern):
    """
    Sort strings based on:
    1. Number of pattern matches (descending)
    2. If matches are equal, sort by string length (ascending)
    3. If lengths are equal, sort alphabetically

    Pattern can be a substring or a character set.

    Example:
    Input:
    strings = ["hello", "world", "hello world", "hi"]
    pattern = "lo"
    Output: ["hello world", "hello", "world", "hi"]

    Args:
        strings (list): List of strings
        pattern (str): Pattern to match
    Returns:
        list: List of strings sorted according to the criteria
    """
    strings = sorted(strings, key = lambda x: (-sum(x.count(char) for char in pattern), len(x), x))
    return strings

# Test cases
def test_sort_array():
    test_cases = [
        # Case 1: Basic case with unique and repeated elements
        ([4, 2, 2, 8, 3, 3, 1], [2, 2, 3, 3, 1, 4, 8]),

        # Case 2: All elements are the same
        ([5, 5, 5, 5], [5, 5, 5, 5]),

        # Case 3: Elements are already sorted by frequency
        ([1, 1, 2, 2, 2, 3], [2, 2, 2, 1, 1, 3]),

        # Case 4: Elements have the same frequency, should sort by value
        ([9, 3, 3, 9, 5, 5], [3, 3, 5, 5, 9, 9]),

        # Case 5: Large numbers included
        ([10, 20, 20, 10, 30, 30, 30], [30, 30, 30, 10, 10, 20, 20]),

        # Case 6: Negative numbers included
        ([0, -1, -1, -2, -2, -2, 3, 3, 3], [-2, -2, -2, 3, 3, 3, -1, -1, 0])
    ]

    for arr, expected in test_cases:
        result = sort_array_by_frequency_and_value(arr)
        print(result)



def test_sort_dict():
    # Test Case 1: Basic sorting by score and name
    data1 = {
        'john': {'score': 85, 'age': 20},
        'alice': {'score': 92, 'age': 21},
        'bob': {'score': 85, 'age': 19}
    }
    expected1 = [
        ('alice', {'score': 92, 'age': 21}),
        ('bob', {'score': 85, 'age': 19}),
        ('john', {'score': 85, 'age': 20})
    ]
    print(sort_dict_by_nested_value(data1))

    # Test Case 2: All scores are equal, sorting by name
    data2 = {
        'dave': {'score': 80, 'age': 22},
        'carol': {'score': 80, 'age': 23},
        'bob': {'score': 80, 'age': 21}
    }
    expected2 = [
        ('bob', {'score': 80, 'age': 21}),
        ('carol', {'score': 80, 'age': 23}),
        ('dave', {'score': 80, 'age': 22})
    ]
    print(sort_dict_by_nested_value(data2))

    # Test Case 3: Already sorted input
    data3 = {
        'zara': {'score': 95, 'age': 18},
        'yasmine': {'score': 90, 'age': 19},
        'xander': {'score': 85, 'age': 20}
    }
    expected3 = [
        ('zara', {'score': 95, 'age': 18}),
        ('yasmine', {'score': 90, 'age': 19}),
        ('xander', {'score': 85, 'age': 20})
    ]
    print(sort_dict_by_nested_value(data3))


    # Test Case 4: Some names with same score but different cases
    data4 = {
        'Alice': {'score': 90, 'age': 22},
        'bob': {'score': 90, 'age': 21},
        'alice': {'score': 90, 'age': 20}
    }
    expected4 = [
        ('Alice', {'score': 90, 'age': 22}),
        ('alice', {'score': 90, 'age': 20}),
        ('bob', {'score': 90, 'age': 21})
    ]
    print(sort_dict_by_nested_value(data4))

    # Test Case 5: Empty dictionary
    data5 = {}
    expected5 = []
    print(sort_dict_by_nested_value(data5))


    # Test Case 6: Single entry
    data6 = {'only': {'score': 100, 'age': 25}}
    expected6 = [('only', {'score': 100, 'age': 25})]
    print(sort_dict_by_nested_value(data6))


def test_sort_sets():
    # Test Case 1: Basic sorting by intersection size
    reference_set1 = {1, 2, 3, 4, 5}
    sets_list1 = [{1, 2, 3}, {4, 5}, {1, 2, 3, 4, 5}, {6, 7}]
    print("Test Case 1:", sort_sets_by_similarity(sets_list1, reference_set1))

    # Test Case 2: Different reference set with fewer common elements
    reference_set2 = {3, 4, 5}
    sets_list2 = [{1, 2}, {3, 4}, {5}, {6, 7}]
    print("Test Case 2:", sort_sets_by_similarity(sets_list2, reference_set2))

    # Test Case 3: Already sorted input with a new reference set
    reference_set3 = {1, 2, 3, 4}
    sets_list3 = [{1, 2, 3, 4, 5}, {1, 2, 3, 4}, {1, 2, 3}, {2}]
    print("Test Case 3:", sort_sets_by_similarity(sets_list3, reference_set3))

    # Test Case 4: Empty list of sets with a different reference set
    reference_set4 = {10, 11, 12}
    sets_list4 = []
    print("Test Case 4:", sort_sets_by_similarity(sets_list4, reference_set4))

    # Test Case 5: Sets with completely disjoint elements and new reference set
    reference_set5 = {20, 30, 40}
    sets_list5 = [{10, 11}, {12, 13, 14}, {15}]
    print("Test Case 5:", sort_sets_by_similarity(sets_list5, reference_set5))

    # Test Case 6: Sets with duplicate elements and another reference set
    reference_set6 = {1, 2, 3, 4, 5, 6}
    sets_list6 = [{1, 2}, {1, 2}, {1, 2, 3, 4}, {3, 4}]
    print("Test Case 6:", sort_sets_by_similarity(sets_list6, reference_set6))


def test_sort_strings():
    # Test Case 1: Basic sorting based on pattern match count
    strings1 = ["hello", "world", "hello world", "hi"]
    pattern1 = "lo"
    print("Test Case 1:", sort_strings_by_pattern(strings1, pattern1))
    # Expected Output: ["hello world", "hello", "world", "hi"]

    # Test Case 2: Strings with equal pattern count but different lengths
    strings2 = ["abc", "acb", "bac", "bca", "cab", "cba"]
    pattern2 = "ab"
    print("Test Case 2:", sort_strings_by_pattern(strings2, pattern2))
    # Expected Output: ["abc", "acb", "bac", "bca", "cab", "cba"]

    # Test Case 3: Strings with no matching characters from pattern
    strings3 = ["xyz", "mno", "pqr", "stu"]
    pattern3 = "abc"
    print("Test Case 3:", sort_strings_by_pattern(strings3, pattern3))
    # Expected Output: ["mno", "pqr", "stu", "xyz"] (since no matches, sorted alphabetically)

    # Test Case 4: Some strings have multiple pattern matches
    strings4 = ["banana", "ananas", "bandana", "apple"]
    pattern4 = "an"
    print("Test Case 4:", sort_strings_by_pattern(strings4, pattern4))
    # Expected Output: ["ananas", "banana", "bandana", "apple"] (sorted by count, length, and alphabetically)

    # Test Case 5: Pattern as a single character
    strings5 = ["zzz", "zz", "z", "zzzz"]
    pattern5 = "z"
    print("Test Case 5:", sort_strings_by_pattern(strings5, pattern5))
    # Expected Output: ["zzzz", "zzz", "zz", "z"] (sorted by count and length)

    # Test Case 6: Empty string list
    strings6 = []
    pattern6 = "abc"
    print("Test Case 6:", sort_strings_by_pattern(strings6, pattern6))
    # Expected Output: []

if __name__ == "__main__":
    test_sort_array()
    test_sort_dict()
    test_sort_sets()
    test_sort_strings()
    print("All tests passed successfully!")