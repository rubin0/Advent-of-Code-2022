with open('input1.txt', 'r', encoding="utf-8") as f:
    calories = 0
    temp = 0
    lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        if line:
            temp += int(line)
        else:
            if temp > calories:
                calories = temp
            temp = 0    

    print(calories)