import pytest
from src.goals import max_window_sum, count_goal_windows, longest_rising_streak


def test_max_window_sum_basic():
    assert max_window_sum([1, 9, 10, 2, 1], 3) == (1, 21)
    assert max_window_sum([5, 5, 5], 3) == (0, 15)
    assert max_window_sum([2, 1], 3) is None


def test_max_window_sum_bad_k():
    with pytest.raises(ValueError):
        max_window_sum([1, 2, 3], 0)


def test_count_goal_windows():
    assert count_goal_windows([1, 9, 10, 2, 1], 3, 5.0) == 2  # windows [1,9,10]=20, [9,10,2]=21
    assert count_goal_windows([2, 2], 3, 2.0) == 0
    assert count_goal_windows([5, 5, 5, 5], 2, 5.0) == 3


def test_count_goal_windows_bad_k():
    with pytest.raises(ValueError):
        count_goal_windows([1, 2], 0, 1.0)


def test_longest_rising_streak():
    assert longest_rising_streak([]) == 0
    assert longest_rising_streak([7]) == 1
    assert longest_rising_streak([1, 2, 3, 2, 3, 4, 1]) == 3
    assert longest_rising_streak([3, 2, 1]) == 1