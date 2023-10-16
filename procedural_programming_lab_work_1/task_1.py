numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38,
           -92, -45, 67, 53, 25]

# заменить значение пропущенного элемента средним арифметическим
only_numbers = numbers[0:4] + numbers[5:]
sum_of_numbers = sum(only_numbers)
len_of_numbers = len(numbers)
avarage_of_numbers = round(sum_of_numbers / len_of_numbers, 2)
numbers[4] = avarage_of_numbers

print("Измененный список:", numbers)
