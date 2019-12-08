import math


def answer():
    with open("day1_data.txt") as file:
        data = file.read()
    data = data.split()
    print("Task 1:", calculate_total_fuel(data))
    print("Task 2:", calculate_total_fuel_fuel(data))


def calculate_module_fuel(mass):
    return math.floor(mass / 3) - 2


def calculate_total_fuel(data):
    total_mass = 0
    for mass in data:
        total_mass += calculate_module_fuel(int(mass))
    return total_mass


def calculate_fuel_fuel(mass):
    current_fuel = math.floor(mass / 3) - 2
    if current_fuel <= 0:
        return 0
    else:
        return current_fuel+calculate_fuel_fuel(current_fuel)


def calculate_total_fuel_fuel(data):
    total_mass = 0
    for mass in data:
        total_mass += calculate_fuel_fuel(int(mass))
    return total_mass


answer()
