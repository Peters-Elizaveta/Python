def find_common_participants(participants_1, participants_2, delimiter=','):

    group_1 = participants_1.split(delimiter)
    group_2 = participants_2.split(delimiter)
    find = list(set(group_1).intersection(group_2))
    find.sort()
    return find


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
delim = '|'
result = find_common_participants(participants_second_group, participants_second_group, delim)
print(result)
