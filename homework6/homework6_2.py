tutors1 = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
groups1 = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
tutors2 = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
groups2 = [
    '9А', '7В', '9Б', '9В'
]


def result_list(tutors, groups):
    result = [(tutors[i], groups[i]) if i < len(groups) else (tutors[i], None) for i in range(len(tutors))]
    return result


print(result_list(tutors2, groups2))
