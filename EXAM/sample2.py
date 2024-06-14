def is_greater_than_average(l):
  """
  This function creates a closure that checks if a number is greater than the average of the list `l`.

  Args:
      l: A list of numbers.

  Returns:
      A function that takes a number `x` and returns True if `x` is greater than the average of `l`.
  """
  average = sum(l) / len(l)

  def check(x):
    """
    This inner function checks if `x` is greater than the average.

    Args:
        x: A number to compare with the average.

    Returns:
        True if `x` is greater than the average, False otherwise.
    """
    return x > average

  return check

# Example usage
numbers = [5, 10, 2, 8]
check_above_average = is_greater_than_average(numbers)

# Test cases
print(check_above_average(7))  # True
print(check_above_average(3))  # False
