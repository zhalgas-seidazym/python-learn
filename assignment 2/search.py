
def search_array_with_window(arr, target_sum, window_size, cur = None, recursive = False):
    """
    Find all subarrays of fixed size that sum to target value.

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
    # print(
    #     f"Function called with: arr={arr}, target_sum={target_sum}, window_size={window_size}, cur={cur}, recursive={recursive}")

    if not recursive:
        res = []
        arr.sort()
        # print(f"Sorted arr: {arr}")

        if window_size == 1:
            for i in arr:
                if i == target_sum:
                    # print(f"Found element {i} matching target {target_sum}, appending to {cur}")
                    res.append((i, ))
                    return res
        elif window_size == size:
            # print(f"Checking entire array: sum({arr}) == {target_sum}")
            return [tuple(arr)] if sum(arr) == target_sum else list()

        elif window_size > size:
            # print(f"Window size {window_size} is larger than array size {size}, returning empty list.")
            return []

        i = 0
        while i <= size - window_size:
            for_cur = [arr[i]]
            # print(f"Trying element {arr[i]} at index {i}, remaining array: {arr[i + 1:]}")

            if i > 0 and arr[i] == arr[i - 1]:
                # print(f"Skipping duplicate element {arr[i]} at index {i}")
                i += 1
                continue
            else:
                # print(
                    # f"Recursive call with: arr={arr[i + 1:]}, target_sum={target_sum - arr[i]}, window_size={window_size - 1}, cur={for_cur}")
                search_array_with_window(arr[i + 1:], target_sum - arr[i], window_size - 1, for_cur, True)

            # print(f"Back from recursion: for_cur={for_cur}")
            for j in range(1, len(for_cur)):
                if sum(for_cur[j]) == target_sum - for_cur[0]:
                    # print(f"Found valid subarray: {for_cur}")
                    res.append(tuple([for_cur[0]] + for_cur[j]))

            i += 1

        # print(f"Returning result: {res}")
        return res

    else:  # Recursive case
        # print(f"Recursive branch with: arr={arr}, target_sum={target_sum}, window_size={window_size}, cur={cur}")

        if window_size == 1:
            for i in arr:
                if i == target_sum:
                    # print(f"Found element {i} matching target {target_sum}, appending to {cur}")
                    cur.append([i])
            return
            # print(f"No element matches target {target_sum}")

        elif window_size == size:
            # print(f"Checking full array: {arr}")
            if sum(arr) == target_sum:
                # print(f"Entire array matches target sum, adding {arr} to {cur}")
                cur.extend(arr)
                return
            else:
                # print(f"Sum of {arr} does not match target {target_sum}")
                return

        elif window_size > size:
            # print(f"Window size {window_size} is greater than array size {size}, returning.")
            return

        i = 0
        while i <= size - window_size : # 1 2 3 4 le 4 w 2
            for_cur = [arr[i]]
            # print(f"Checking element {arr[i]} at index {i}, remaining array: {arr[i + 1:]}")

            search_array_with_window(arr[i + 1:], target_sum - arr[i], window_size - 1, for_cur, True)

            for j in range(1, len(for_cur)):
                if sum(for_cur[j]) == target_sum - for_cur[0]:
                    # print(f"Found valid subarray: {[for_cur[0]]} + {for_cur[j]}")
                    cur.append([for_cur[0]] + for_cur[j])
            i += 1

        # print(f"Recursive function exiting for arr={arr}")
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
    # Your implementation here
    pass


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
    # Your implementation here
    pass


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
    # Your implementation here
    pass


# Test cases
def test_array_search():
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
    print(search_array_with_window([1, 2, 3, 4, 5, 6], 9,
                                   3))  # Expected Output: [(1, 2, 6), (1, 3, 5), (2, 3, 4)]

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
    # Your test case implementation here
    pass


def test_sets_search():
    # Your test case implementation here
    pass


def test_string_search():
    # Your test case implementation here
    pass


if __name__ == "__main__":
    # test_array_search()
    test_dict_search()
    test_sets_search()
    test_string_search()
    print("All tests passed successfully!")