with open('input1.txt', 'r', encoding="utf-8") as f:
    calories = []
    temp = 0
    lines = f.readlines()
    
    for line in lines:
        if line.strip():
            temp += int(line)
        else:
            calories.append(temp);
            temp = 0

    calories.sort(reverse=True)

    print(calories[0] + calories[1] + calories[2])