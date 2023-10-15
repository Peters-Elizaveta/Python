numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_missing_item = 4
sum_numbers = sum(numbers[index_missing_item + 1:])+sum(numbers[:index_missing_item])
numbers[index_missing_item] = sum_numbers / len(numbers)

print("Измененный список:", numbers)
