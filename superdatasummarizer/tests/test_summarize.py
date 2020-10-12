"""Ensure that the data summarization works correctly."""

import math

from superdatasummarizer import summarize


def test_summarize_empty_number_list_mean():
    """Ensure that an empty list of numbers summarizes with mean correctly."""
    data_list_numbers = []
    mean = summarize.compute_mean(data_list_numbers)
    assert math.isnan(mean)


def test_summarize_pos_neg_number_list():
    """Ensure that a "cancel out" list of numbers summarizes correctly."""
    data_list_numbers = [-10, 10]
    mean = summarize.compute_mean(data_list_numbers)
    assert mean == 0.0


def test_summarize_equal_number_list():
    """Ensure that an equal number list of numbers summarizes correctly."""
    data_list_numbers = [10, 10]
    mean = summarize.compute_mean(data_list_numbers)
    assert mean == 10.0


def test_summarize_different_number_list():
    """Ensure that an equal number list of numbers summarizes correctly."""
    data_list_numbers = [5, 10]
    mean = summarize.compute_mean(data_list_numbers)
    assert mean == 7.5


def test_summarize_empty_number_list_median():
    """Ensure that an empty list of numbers summarizes with median correctly."""
    data_list_numbers = []
    median = summarize.compute_median(data_list_numbers)
    assert math.isnan(median)


def test_summarize_full_list_median_even():
    """Ensure that a full list of numbers summarizes with median correctly."""
    data_list_numbers = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    median = summarize.compute_median(data_list_numbers)
    assert median == 500.0


def test_summarize_full_list_median_odd():
    """Ensure that a full list of numbers summarizes with median correctly."""
    data_list_numbers = [100, 60, 70, 900, 100, 200, 475, 500, 503, 600, 1000]
    median = summarize.compute_median(data_list_numbers)
    assert median == 475.0


def test_compute_difference_empty_list():
    """Ensure that an empty list of numbers has a correct difference from mean."""
    data_list_numbers = []
    differences = summarize.compute_difference(data_list_numbers)
    assert len(differences) == 0


def test_summarize_compute_difference():
    """Ensure that the computing of the difference from the mean is correct."""
    data_list_numbers = [10, 10, 5, 5]
    mean = summarize.compute_mean(data_list_numbers)
    assert mean == 7.5
    differences_expected = []
    # directly compute the differences
    for number in data_list_numbers:
        differences_expected.append(float(number - mean))
    differences_actual = summarize.compute_difference(data_list_numbers)
    assert differences_actual == differences_expected


def test_summarize_full_list_variance_even():
    """Ensure that a full list of numbers summarizes with variance correctly."""
    data_list_numbers = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    variance = summarize.compute_variance(data_list_numbers)
    assert variance == 141047.35416666666


def test_summarize_full_list_standard_deviation_even():
    """Ensure that a full list of numbers summarizes with standard deviation correctly."""
    data_list_numbers = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    standard_deviation = summarize.compute_standard_deviation(data_list_numbers)
    assert standard_deviation == 141047.35416666666 ** 0.5
