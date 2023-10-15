mass = [1, 2, 13, 423, 12]
sort_mass = 1

while sort_mass < len(mass):
    for i in range(len(mass) - sort_mass):
        if mass[i] > mass[i + 1]:
            mass[i], mass[i + 1] = mass[i + 1], mass[i]
    sort_mass += 1
print(mass)


