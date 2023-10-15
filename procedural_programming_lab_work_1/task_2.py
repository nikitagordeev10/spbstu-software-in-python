diskette_memory_size = 1.44  # Мб
number_of_pages_in_book = 100
number_of_lines_per_page = 50
number_of_characters_in_line = 25
single_character_memory = 4  # байта

# Найдите количество книг, которое можно разместить на дискете
one_book_size_in_bytes = (number_of_pages_in_book * \
                          number_of_lines_per_page * \
                          number_of_characters_in_line * \
                          single_character_memory)
one_book_size_in_mb = one_book_size_in_bytes / 1024 / 1024
number_of_books_per_diskette = diskette_memory_size // one_book_size_in_mb

print("Количество книг, помещающихся на дискету:",
      int(number_of_books_per_diskette))
