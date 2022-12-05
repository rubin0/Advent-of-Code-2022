with open('input2.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    score = 0

    value_dict = {
        'X': 0, #lose
        'Y': 3, #draw
        'Z': 6  #win
    }

    score_dict = {
        'A': {'X': 3, 'Y': 1, 'Z': 2}, #rock        (1)
        'B': {'X': 1, 'Y': 2, 'Z': 3}, #paper       (2)
        'C': {'X': 2, 'Y': 3, 'Z': 1}  #scissors    (3) 
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
