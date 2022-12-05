with open('input2.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    score = 0

    value_dict = {
        'X': 1, #rock
        'Y': 2, #paper
        'Z': 3  #scissors
    }

    score_dict = {
        'A': {'X': 3, 'Y': 6, 'Z': 0}, #rock
        'B': {'X': 0, 'Y': 3, 'Z': 6}, #paper
        'C': {'X': 6, 'Y': 0, 'Z': 3}  #scissors
    }

    for line in lines:
        line = line.strip()
        if line:
            splitted_lines = line.split(" ")

            my_guess_score = int(value_dict[splitted_lines[1]])
            outcome_score = int(score_dict[splitted_lines[0]][splitted_lines[1]])

            score = score + my_guess_score 
            score = score + outcome_score
        else:
            break
    print(score)
