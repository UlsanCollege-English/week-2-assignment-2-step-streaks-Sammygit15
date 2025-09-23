from typing import List, Tuple, Optional

def max_window_sum(values: List[int], k: int) -> Optional[Tuple[int, int]]:
    """Return (start_index, window_sum) of the largest sum among all length-k windows.
    
    If k <= 0, raise ValueError. If k > len(values), return None.
    """
    if k <= 0:
        raise ValueError("k must be greater than 0.")
    if k > len(values):
        return None

    current_sum = sum(values[:k])
    max_sum = current_sum
    start_index = 0

    for i in range(1, len(values) - k + 1):
        # Slide the window by removing the leftmost and adding the new rightmost element
        current_sum = current_sum - values[i - 1] + values[i + k - 1]
        if current_sum > max_sum:
            max_sum = current_sum
            start_index = i

    return (start_index, max_sum)


def count_goal_windows(values: List[int], k: int, target_avg: float) -> int:
    """Return the number of length-k windows with average >= target_avg.
    
    If k <= 0, raise ValueError. If k > len(values), return 0.
    """
    if k <= 0:
        raise ValueError("k must be greater than 0.")
    if k > len(values):
        return 0

    count = 0
    current_sum = sum(values[:k])

    if current_sum / k >= target_avg:
        count += 1

    for i in range(1, len(values) - k + 1):
        current_sum = current_sum - values[i - 1] + values[i + k - 1]
        if current_sum / k >= target_avg:
            count += 1

    return count


def longest_rising_streak(values: List[int]) -> int:
    """Return the length of the longest strictly increasing consecutive streak.
    
    Empty list -> 0. Single element -> 1.
    """
    if not values:
        return 0

    max_streak = 1
    current_streak = 1

    for i in range(1, len(values)):
        if values[i] > values[i - 1]:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 1

    return max_streak
