# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

def check_first_and_last_same(numbers):
    # Ensure our list has at least two elements to compare
    if len(numbers) >= 2:
        return numbers[0] == numbers[-1]
    else:
        # If the list has less than two elements, return False
        return False

def main():
    # Example lists of number x and y
    numbers_x = [10, 20, 30, 40, 10]
    numbers_y = [75, 65, 35, 75, 30]

    # Check and print results for each list
    result_x = check_first_and_last_same(numbers_x)
    result_y = check_first_and_last_same(numbers_y)

    print(f"For numbers_x: [10, 20, 30, 40, 10], The result is {result_x}")
    print(f"For numbers_y: [75, 65, 35, 75, 30], The result is {result_y}")

if __name__ == "__main__":
    main()
