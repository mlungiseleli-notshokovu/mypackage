from mypackage import recursion
from mypackage import sorting

''' Recursion Module'''
def test_sum_array():
    assert recursion.sum_array([10, 1, 12, 9, 2]) == 34,'Correct'
    assert recursion.sum_array([8, 3, 2, 7, 4]) == 24,'Correct'
    assert recursion.sum_array([8, 3, 2, 24, 4]) == 24,'Incorrect'

def test_fibonacci():
        assert recursion.fibonacci(8) == 21,'Correct'
        assert recursion.fibonacci(15) == 610,'Correct'

def test_factorial():
    assert recursion.factorial(5) == 120, 'Correct'
    assert recursion.factorial(8) == 40320, 'Correct'

def test_reverse():
        assert recursion.reverse('this is a longer sentence that you will need to reverse') == "esrever ot deen lliw uoy taht ecnetnes regnol a si siht", 'Correct'

''' Sorting Module'''
def test_bubble_sort():
    assert sorting.bubble_sort([8, 3, 2, 7, 4]) == [2, 3, 4, 7, 8], 'Correct'
    assert sorting.bubble_sort([19, 3, 2, 7, 4,45,9]) == [2, 3, 4, 7, 9, 19, 45], 'Correct'

def test_merge_sort():
        assert sorting.merge_sort([19, 3, 2, 7, 4,45,9]) == [2, 3, 4, 7, 9, 19, 45], 'Correct'

def test_quick_sort():
        assert sorting.quick_sort([19, 3, 2, 7, 4,45,9]) == [2, 3, 4, 7, 9, 19, 45], 'Correct'