# range input 246540-787419
left = 246540
right = 787419


def answer():
    print("Task 1:", count_passwords(restrictions))
    print("Task 2:", count_passwords(improved_restrictions))


def count_passwords(criteria):
    count = 0
    for i in range(int(left), int(right)+1):
        if criteria(str(i)):
            count += 1
    return count


# TASK_1:
def restrictions(number):
    if len(number) != 6:
        return 0

    outcome = 0
    for i in range(len(number)-1):
        if number[i] == number[i+1]:
            outcome = 1
        if number[i] > number[i+1]:
            return 0
    return outcome


# TASK_2
def improved_restrictions(number):
    if len(number) != 6:
        return 0
    count_group = 1
    outcome = 0
    for i in range(len(number) - 1):
        if number[i] == number[i + 1]:
            count_group += 1
        elif number[i] != number[i+1]:
            if count_group == 2:
                outcome = 1
            count_group = 1
        if number[i] > number[i + 1]:
            return 0
    if count_group == 2:
        outcome = 1
    return outcome


answer()
