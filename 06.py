with open('input6.txt', 'r', encoding="utf-8") as f:
    line = f.readline()

    count = 1
    char_list = []

    for chr in line:
        char_list.append(chr)

        if len(set(char_list)) == 4:
            print(count)
            break
        else:
            if len(char_list) > 3:
                char_list.pop(0)
            count += 1
