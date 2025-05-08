import Lab3 as sort  # Adjust this based on your filename

def test_req01_ascending_sort():
    result = sort.bubble_sort([5, 2, 9, 1], sort.SORT_ASCENDING)
    assert result == [1, 2, 5, 9]

def test_req02_descending_sort():
    result = sort.bubble_sort([5, 2, 9, 1], sort.SORT_DESCENDING)
    assert result == [9, 5, 2, 1]

def test_req03_too_many_elements():
    result = sort.bubble_sort([1,2,3,4,5,6,7,8,9,10], sort.SORT_ASCENDING)
    assert result == 1

def test_req04_empty_list():
    result = sort.bubble_sort([], sort.SORT_ASCENDING)
    assert result == 0

def test_req05_non_integer_input():
    result = sort.bubble_sort([1, 2, 'a', 4], sort.SORT_ASCENDING)
    assert result == 2