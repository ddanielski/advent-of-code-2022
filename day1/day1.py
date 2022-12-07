with open('day1.txt') as f:
    lines = f.readlines()
    sum_cal = [0]
    tmp = 0
    for line in lines:
        if line.strip():
            tmp += int(line)
        else:
            sum_cal.append(tmp)
            tmp = 0

sum_cal.sort(reverse=True)

print("The number of calories of the first elf is: " + str(sum_cal[0]))
print("The total number of calories of the first three elves is: " +
      str(sum(sum_cal[0:3])))
