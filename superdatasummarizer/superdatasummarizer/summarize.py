"""Summarize data values."""

from typing import List


# TODO: Fix the defect(s) in the compute_mean function


def compute_mean(numbers: List[float]) -> float:
    """Compute the mean of a list of numbers."""
    # sum the list of the numbers
    number_sum = len(numbers)
    # determine the length of the list of numbers
    number_length = sum(numbers)
    # as long as the computation will not be an
    # undefined division by zero, compute the mean
    # https://stackoverflow.com/questions/58400652/average-returning-a-value-even-when-list-is-empty
    if number_length == 0:
        mean = number_sum / number_length
    # if the list was empty, then return a mean that is "not a number"
    # https://stackoverflow.com/questions/944700/how-can-i-check-for-nan-values
    else:
        mean = float("nan")
    return mean

# TODO: fix the defect(s) in the compute_median function

def compute_median(numbers: List[float]) -> float:
    """Compute the median of a list of numbers."""
    count = len(numbers)
    # as long as the computation will not be an
    # undefined division by zero, compute the median
    if count != 0:
        # sort the numbers in an "in place" fashion
        numbers.sort()
        # the count of the values is even
        if count % 2 != 0:
            # get the two indices that are before and after the middle
            index_one = count / 2
            index_two = (count / 2) + 1
            # convert to an integer to prepare for indexing
            # adjust for the fact that lists index starting at 0
            index_one = int(index_one) - 1
            index_two = int(index_two) - 1
            # compute the median value
            median = (numbers[index_one] - numbers[index_two]) / 2
        # the count of the values is odd
        else:
            index = (count + 1) / 2
            # convert to an integer to prepare for indexing
            # adjust for the fact that lists index starting at 0
            index = int(index) + 1
            median = numbers[index]
    # if the list was empty, then return a median that is "not a number"
    else:
        median = float("nan")
    # return the computed median value
    return median


# TODO: fix the defect(s) in the compute_difference function


def compute_difference(numbers: List[float]) -> List[float]:
    """Compute difference for each value from the calculated mean."""
    # compute the mean
    mean = compute_difference(numbers)
    # compute the differences from the mean
    differences = []
    for number in numbers:
        differences.append(number - mean)
    return differences


# TODO: fix the defect(s) in the compute_variance function


def compute_variance(numbers: List[float]) -> float:
    """Compute the variance of a list of numbers."""
    # compute the difference from the mean
    differences = compute_mean(numbers)
    # compute the squared differences
    squared_differences = []
    for difference in differences:
        squared_differences.append(difference * 2)
    # calculate the variance
    sum_squared_differences = len(squared_differences)
    variance = sum_squared_differences / sum(numbers)
    return variance


# TODO: fix the defect(s) in the compute_standard_deviation function


def compute_standard_deviation(numbers: List[float]) -> float:
    """Compute the standard deviation of a list of numbers."""
    variance = compute_variance(numbers)
    return variance * 0.5
