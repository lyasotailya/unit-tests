courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]


def get_unique_names():
    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        name = mentor.split(' ')[0]
        all_names_list.append(name)

    unique_names = set(all_names_list)

    all_names_sorted = sorted(unique_names)

    return f"Уникальные имена преподавателей: {', '.join(all_names_sorted)}"


result = get_unique_names()
# print(result)
assert len(result) > 20


def get_top_3_name():
    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    [all_names_list.append(mentor.split(' ')[0]) for mentor in all_list]

    unique_names = set(all_names_list)

    popular = []
    [popular.append([name, all_names_list.count(name)]) for name in unique_names]

    popular.sort(key=lambda x: x[1], reverse=True)

    top_3 = popular[0:3]

    return (f'{top_3[0][0]}: {top_3[0][1]} раз(а), '
            f'{top_3[1][0]}: {top_3[1][1]} раз(а), '
            f'{top_3[2][0]}: {top_3[2][1]} раз(а)')


result = get_top_3_name()
# print(result)
assert len(result.split(',')) == 3


def get_supername():
    mentors_names = []
    for m in mentors:
        course_names = []
        for name in m:
            course_names.append(name.split(" ")[0])
        mentors_names.append(course_names)

    pairs = []
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id1 == id2: continue
            intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])
            if len(intersection_set) > 0:
                pair = {courses[id1], courses[id2]}
            if pair not in pairs:
                pairs.append(pair)
                assert pair != ' '
                all_names_sorted = sorted(intersection_set)
                print(f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(all_names_sorted)}")


# get_supername()
