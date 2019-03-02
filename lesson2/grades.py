all_grades = [  {'school_class': '4a', 'scores': [1,2,3,4,5]},
                {'school_class': '5a', 'scores': [5,5,5,5,5]},
                {'school_class': '6a', 'scores': [3,3,3,3,3]},
                {'school_class': '7a', 'scores': [2,2,2,2,2]},
              ]

school_sum_grade = 0

for clas in all_grades:

    k = 0

    for i in clas['scores']:
        k = k + i

    average_grade = k / len(clas['scores'])
    c = clas ['school_class']
    print('Midle of grades in class ', c,  ' = ', average_grade)

    school_sum_grade = school_sum_grade + average_grade

average_school_grade = school_sum_grade / len(all_grades)
print(average_school_grade)
