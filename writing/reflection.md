# Reflection by Add Your Name Here

## Using a fenced code block, please display two correct outputs from running your program

TODO: Please provide a fenced code block that shows the output from running your program

## Using a fenced code block, please display the passing output from running the tests with `poetry run pytest -v`

TODO: Please provide a fenced code block that shows the output from running the test suite

## What is the purpose of the following function in the context of the `display` module?

```
def transform_string_to_number_list(data_text: str) -> List[float]:
    """Transform a string of (date, float) values to a list of floats."""
    data_number_list = []
    # iterate through each line of the data set
    for line in data_text.splitlines():
        # extract the ordered pair this line
        # the ordered pair has the format:
        # (Date, population count in thousands of persons)
        ordered_pair = line.split(",")
        # convert the population count to a float and store it
        # in the data_number_list
        data_number_list.append(float(ordered_pair[1]))
    # return the data_number_list
    return data_number_list
```

TODO: please explain the source code segment in the above fenced code block.

## What is the purpose of the following function in the context of the `summarize` module?

```
def compute_difference(numbers: List[float]) -> List[float]:
    """Compute difference for each value from the calculated mean."""
    # compute the mean
    mean = compute_mean(numbers)
    # compute the differences from the mean
    differences = []
    for number in numbers:
        differences.append(number - mean)
    return differences
```

TODO: please explain the source code segment in the above fenced code block.

## What was the greatest technical challenge that you faced and how did you overcome it?

TODO: please provide a response to this question.

## After completing this assignment, what is one task that you want to practice more? Why?

TODO: please provide a response to this question.

## After completing this assignment, what is one experience for which you are grateful?

TODO: please provide a response to this question.

## Although it is not required, you may provide any additional insights about this assignment

TODO: please provide a response to this question.
