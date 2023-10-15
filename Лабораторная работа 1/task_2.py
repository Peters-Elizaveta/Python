pages_in_book = 100
lines_per_page = 50
characters_in_string = 25
bytes_per_character = 4
disk_capacity = 1.44

bytes_in_one_book = pages_in_book * lines_per_page * characters_in_string * bytes_per_character
megabytes_in_one_book = bytes_in_one_book / 1024 / 1024
books_on_disk = int(disk_capacity // megabytes_in_one_book)

print("Количество книг, помещающихся на дискету:", books_on_disk)
