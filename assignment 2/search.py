
def search_array_with_window(arr, target_sum, window_size, cur = None, recursive = False):
    """
    Find all sub arrays of fixed size that sum to target value.

    Example:
    Input: arr = [1, 2, 3, 4, 5, 6], target_sum = 9, window_size = 3
    Output: [(1, 2, 6), (1, 3, 5), (2, 3, 4)]  # Starting indices of valid windows

    Args:
        arr (list): List of integers
        target_sum (int): Target sum to find
        window_size (int): Size of the sliding window
        cur (list): Current working list in recursion
        recursive (bool): If true, recursively search
    Returns:
        list: List of tuples containing valid window starting indices
    """
    size = len(arr)

    # res = []
    # window_size_copy = window_size
    # for i in range(size):
    #     cur = 0
    #     if i >= size - window_size:
    #         window_size = size - i
    #     for j in range(window_size):
    #         cur += arr[i + j]
    #         if cur == target_sum:
    #             if len(arr[i: i + j + 1]) < window_size_copy:
    #                 res.append(tuple(arr[i: i + j + 1] + [0] * (window_size_copy - len(arr[i: i + j + 1]))))
    #             else:
    #                 res.append(tuple(arr[i: i + j + 1]))
    # return res


    if not recursive:
        res = []
        arr.sort()

        if window_size == 1:
            for i in arr:
                if i == target_sum:
                    res.append((i,))
                    return res
        elif window_size == size:
            return [tuple(arr)] if sum(arr) == target_sum else list()
        elif window_size > size:
            return []

        i = 0
        while i <= size - window_size:
            for_cur = [arr[i]]
            if i > 0 and arr[i] == arr[i - 1]:
                i += 1
                continue
            else:
                search_array_with_window(arr[i + 1:], target_sum - arr[i], window_size - 1, for_cur, True)

            for j in range(1, len(for_cur)):
                if sum(for_cur[j]) == target_sum - for_cur[0]:
                    res.append(tuple([for_cur[0]] + for_cur[j]))
            i += 1
        return res
    else:
        if window_size == 1:
            for i in arr:
                if i == target_sum:
                    cur.append([i])
            return
        elif window_size == size:
            if sum(arr) == target_sum:
                cur.extend(arr)
                return
            else:
                return
        elif window_size > size:
            return
        i = 0
        while i <= size - window_size:
            for_cur = [arr[i]]
            search_array_with_window(arr[i + 1:], target_sum - arr[i], window_size - 1, for_cur, True)
            for j in range(1, len(for_cur)):
                if sum(for_cur[j]) == target_sum - for_cur[0]:
                    cur.append([for_cur[0]] + for_cur[j])
            i += 1
        return


def search_nested_dict(data, search_criteria):
    """
    Search through nested dictionary structure for values matching all criteria.

    Example:
    Input:
    data = {
        'user1': {'name': 'John', 'scores': {'math': 90, 'physics': 85}},
        'user2': {'name': 'Alice', 'scores': {'math': 95, 'physics': 90}},
    }
    search_criteria = {'scores.math': lambda x: x > 92, 'name': lambda x: 'i' in x.lower()}
    Output: ['user2']  # Only Alice matches both criteria

    Args:
        data (dict): Nested dictionary structure
        search_criteria (dict): Dictionary of path:predicate pairs
    Returns:
        list: Keys of matching entries
    """
    nested_data = list()
    for i in data:
        check = True
        for j in search_criteria:
            criteria = j.split('.')
            toCheck = data[i][criteria[0]]
            for k in range(1, len(criteria)):
                toCheck = toCheck.get(criteria[k])
            if not search_criteria[j](toCheck):
                check = False
        if check: nested_data.append(i)
    return nested_data


def search_sets_intersection(sets_list, min_common_elements):
    """
    Find all pairs of sets that share at least minimum number of common elements.

    Example:
    Input:
    sets_list = [{1, 2, 3}, {2, 3, 4}, {4, 5, 6}, {1, 2, 5}]
    min_common_elements = 2
    Output: [({1, 2, 3}, {1, 2, 5}), ({1, 2, 3}, {2, 3, 4})]

    Args:
        sets_list (list): List of sets
        min_common_elements (int): Minimum number of common elements required
    Returns:
        list: List of set pairs that meet the criteria
    """

    size = len(sets_list)
    res = list()
    for i in range(size):
        for j in range(i + 1, size):
            if len(sets_list[i].intersection(sets_list[j])) >= min_common_elements:
                res.append((sets_list[i], sets_list[j]))
    return res


def search_string_patterns(text, pattern_rules):
    """
    Find all substrings that match a set of pattern rules.
    Rules can include: length, character set, prefix/suffix, etc.

    Example:
    Input:
    text = "The quick brown fox jumps over lazy dogs"
    pattern_rules = {
        'min_length': 4,
        'must_contain': ['o', 'r'],
        'must_start_with': ['b', 'f'],
        'must_end_with': ['n', 'x']
    }
    Output: ['brown', 'fox']

    Args:
        text (str): Input text to search
        pattern_rules (dict): Dictionary of rules to match
    Returns:
        list: All matching substrings
    """
    words = text.split()
    matching_words = []

    for word in words:
        if 'min_length' in pattern_rules and len(word) < pattern_rules['min_length']:
            continue

        if 'must_contain' in pattern_rules:
            if not all(char in word for char in pattern_rules['must_contain']):
                continue

        if 'must_start_with' in pattern_rules:
            if not any(word.startswith(prefix) for prefix in pattern_rules['must_start_with']):
                continue

        if 'must_end_with' in pattern_rules:
            if not any(word.endswith(suffix) for suffix in pattern_rules['must_end_with']):
                continue

        matching_words.append(word)

    return matching_words


# Test cases
def test_array_search():
    # test_cases = [
    #     # Basic case with a simple target sum
    #     ([1, 2, 3, 4, 5], 5, 3, [(2, 3, 0), (5, 0, 0)]),
    #
    #     # Case where subarray is at the beginning
    #     ([1, 2, 3, 7, 5], 12, 3, [(2, 3, 7), (7, 5, 0)]),
    #
    #     # Case where the sum is found multiple times
    #     ([1, 2, 3, 4, 2, 3], 6, 3, [(1, 2, 3), (4, 2, 0)]),
    #
    #     # Edge case with a single-element array
    #     ([5], 5, 1, [(5,)]),
    #
    #     # Case where no subarray meets the sum
    #     ([1, 1, 1, 1], 10, 2, []),
    #
    #     # Case with negative numbers
    #     ([-1, -2, -3, 4, 6], 4, 3, [(4, 0, 0)]),
    #
    #     # Case where the sum is found at the end of the array
    #     ([2, 4, 6, 8, 10], 18, 3, [(4, 6, 8), (8, 10, 0)])
    # ]
    #
    # for arr, target_sum, window_size, expected in test_cases:
    #     result = search_array_with_window(arr, target_sum, window_size)
    #     print(result)

    # Test Case 1
    print(search_array_with_window([5, 3, 4, 6, 1], 9, 2))  # Expected Output: [(3, 6), (4, 5)]

    # Test Case 2
    print(search_array_with_window([1, 1, 1, 1, 1], 10, 3))  # Expected Output: []

    # Test Case 3
    print(search_array_with_window([2, 3, 4, 5], 14, 4))  # Expected Output: [(2, 3, 4, 5)]

    # Test Case 4
    print(search_array_with_window([7, 1, 2, 3, 4, 5], 7, 1))  # Expected Output: [(7)]

    # Test Case 5
    print(search_array_with_window([3, 5, 2], 10, 5))  # Expected Output: []

    # Test Case 6
    print(search_array_with_window([1, 2, 3, 4, 5, 6], 9, 3))  # Expected Output: [(1, 2, 6), (1, 3, 5), (2, 3, 4)]

    # Test Case 7
    print(search_array_with_window([5, 3, 4, 6, 1, 2, 7, 8, 9, 10], 20, 5))
    # Expected Output: [(5, 3, 4, 6, 2), (3, 4, 6, 1, 6), (4, 6, 1, 2, 7)]

    # Test Case 8
    print(search_array_with_window([10, 2, 3, 1, 5, 8, 7, 4, 6, 9, 11, 13], 30, 7))
    # Expected Output: [(1, 2, 3, 4, 5, 6, 9), (1, 2, 3, 4, 5, 7, 8)]

    # Test Case 9
    print(search_array_with_window([1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40], 50, 7))
    # Expected Output: [(1, 2, 3, 4, 5, 10, 25), (1, 2, 3, 4, 5, 15, 20)]


def test_dict_search():
    # Test Case 1: Basic matching criteria
    data1 = {
        'user1': {'name': 'John', 'scores': {'math': 90, 'physics': 85}},
        'user2': {'name': 'Alice', 'scores': {'math': 95, 'physics': 90}},
    }
    criteria1 = {'scores.math': lambda x: x > 92, 'name': lambda x: 'i' in x.lower()}
    print(search_nested_dict(data1, criteria1)) #['user2']

    # Test Case 2: No matches
    criteria2 = {'scores.math': lambda x: x > 100}
    print(search_nested_dict(data1, criteria2)) #[]

    # Test Case 3: Partial matches (one condition failing)
    criteria3 = {'scores.physics': lambda x: x < 90, 'name': lambda x: 'J' in x}
    print(search_nested_dict(data1, criteria3)) #['user1']

    # Test Case 4: Complex nesting with missing key
    data2 = {
        'user1': {'name': 'Tom', 'details': {'age': 30, 'location': {'city': 'NY'}}},
        'user2': {'name': 'Jerry', 'details': {'age': 25, 'location': {'city': 'LA'}}},
    }
    criteria4 = {'details.location.city': lambda x: x == 'LA'}
    print(search_nested_dict(data2, criteria4)) #['user2']

    # Test Case 5: Numeric condition on deeper level
    data3 = {
        'emp1': {'name': 'Bob', 'salary': {'base': 50000, 'bonus': 5000}},
        'emp2': {'name': 'Alice', 'salary': {'base': 70000, 'bonus': 7000}},
    }
    criteria5 = {'salary.base': lambda x: x > 60000}
    print(search_nested_dict(data3, criteria5)) #['emp2']

    # Test Case 6: String condition with case insensitivity
    criteria6 = {'name': lambda x: x.lower().startswith('b')}
    print(search_nested_dict(data3, criteria6)) #['emp1']


def test_sets_search():
    # Test Case 1: Basic case with two matching pairs
    sets_list1 = [{1, 2, 3}, {2, 3, 4}, {4, 5, 6}, {1, 2, 5}]
    min_common_elements1 = 2
    print("Test Case 1:", search_sets_intersection(sets_list1, min_common_elements1))

    # Test Case 2: No matching pairs
    sets_list2 = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
    min_common_elements2 = 2
    print("Test Case 2:", search_sets_intersection(sets_list2, min_common_elements2))

    # Test Case 3: All sets have at least min_common_elements in common
    sets_list3 = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}, {4, 5, 6, 7}]
    min_common_elements3 = 2
    print("Test Case 3:", search_sets_intersection(sets_list3, min_common_elements3))

    # Test Case 4: Only one valid pair
    sets_list4 = [{10, 20, 30}, {20, 30, 40}, {50, 60, 70}]
    min_common_elements4 = 2
    print("Test Case 4:", search_sets_intersection(sets_list4, min_common_elements4))

    # Test Case 5: Minimum common elements set to 1 (matches multiple pairs)
    sets_list5 = [{100, 200, 300}, {200, 300, 400}, {300, 400, 500}, {400, 500, 600}]
    min_common_elements5 = 1
    print("Test Case 5:", search_sets_intersection(sets_list5, min_common_elements5))

    # Test Case 6: All sets are identical
    sets_list6 = [{5, 10}, {5, 10}, {5, 10}]
    min_common_elements6 = 2
    print("Test Case 6:", search_sets_intersection(sets_list6, min_common_elements6))

    # Test Case 7: Large sets with high min_common_elements
    sets_list7 = [
        set(range(1, 10)),
        set(range(15, 25)),
        set(range(15, 35)),
        set(range(10, 15))
    ]
    min_common_elements7 = 5
    print("Test Case 7:", search_sets_intersection(sets_list7, min_common_elements7))

    # Test Case 8: Edge case with empty sets
    sets_list8 = [set(), set(), {1, 2, 3}]
    min_common_elements8 = 1
    print("Test Case 8:", search_sets_intersection(sets_list8, min_common_elements8))


def test_string_search():
    test_cases = [
        ("The quick brown fox jumps over lazy dogs",
         {'min_length': 4, 'must_contain': ['o', 'r'], 'must_start_with': ['b', 'f'], 'must_end_with': ['n', 'x']},
         ['brown']),
        ("hello world python programming",
         {'min_length': 5, 'must_contain': ['o'], 'must_start_with': ['p'], 'must_end_with': ['n']}, ['python']),
        ("apple banana cherry date",
         {'min_length': 5, 'must_contain': ['a'], 'must_start_with': ['b', 'c'], 'must_end_with': ['y', 'e']}, []),
        ("car cat dog cart", {'min_length': 3, 'must_contain': ['c'], 'must_start_with': ['c'], 'must_end_with': ['t']},
         ['cat', 'cart']),
        ("abcdefg hijklmnop qrstuv",
         {'min_length': 7, 'must_contain': ['h', 'i'], 'must_start_with': ['h'], 'must_end_with': ['p']},
         ['hijklmnop']),
        ("fast furious fox fish",
         {'min_length': 4, 'must_contain': ['f'], 'must_start_with': ['f'], 'must_end_with': ['t']}, ['fast']),
        ("green garden gorilla grape",
         {'min_length': 5, 'must_contain': ['g'], 'must_start_with': ['g'], 'must_end_with': ['e']}, ['grape'])
    ]

    for text, pattern_rules, expected in test_cases:
        result = search_string_patterns(text, pattern_rules)
        print(result, expected)
        assert result == expected, f"Failed for: {text}. Expected: {expected}, Got: {result}"


if __name__ == "__main__":
    # test_array_search()
    test_dict_search()
    # test_sets_search()
    # test_string_search()
    print("All tests passed successfully!")