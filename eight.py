def index_of_second_max(nums):
    if len(nums) < 2:
        return None  # Not enough elements

    max_idx = 0
    second_max_idx = -1  # Initialize with a non-existent index

    for i in range(1, len(nums)):
        if nums[i] > nums[max_idx]:
            if second_max_idx == -1:
                second_max_idx = max_idx
            else:
                max_idx = i
        else:
            if second_max_idx == -1 or nums[i] > nums[second_max_idx]:
                second_max_idx = i

    return second_max_idx

# Example usage
numbers = [4, 9, 2, 10, 7, 8]
result_index = index_of_second_max(numbers)
print("The index of the second maximum number is:", result_index)

