def count_passwords(restrictions):
    count = 0
    for i in range(int(left), int(right)+1):
        if restrictions(str(i)):
            count += 1
    return count

def restrictions(number):
    assert len(number) == 6
    outcome = 0
    for i in range(len(number)-1):
        if number[i] == number[i+1]:
            outcome = 1
        if number[i] > number[i+1]:
            return 0
    return outcome

def improved_restrictions(number):
    assert len(number) == 6
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

left = 246540
right = 787419
print("Task 1:", count_passwords(restrictions))
print("Task 2:", count_passwords(improved_restrictions))