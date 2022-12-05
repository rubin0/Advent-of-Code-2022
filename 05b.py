'''
[T] [V]                     [W]    
[V] [C] [P] [D]             [B]    
[J] [P] [R] [N] [B]         [Z]    
[W] [Q] [D] [M] [T]     [L] [T]    
[N] [J] [H] [B] [P] [T] [P] [L]    
[R] [D] [F] [P] [R] [P] [R] [S] [G]
[M] [W] [J] [R] [V] [B] [J] [C] [S]
[S] [B] [B] [F] [H] [C] [B] [N] [L]
 1   2   3   4   5   6   7   8   9 
'''
with open('input5.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    crates = [
        [],                                 #0
        ['T','V','J','W','N','R','M','S'],   #1
        ['V','C','P','Q','J','D','W','B'],  #2
        ['P','R','D','H','F','J','B'],      #3
        ['D','N','M','B','P','R','F'],      #4
        ['B','T','P','R','V','H'],          #5 
        ['T','P','B','C'],                  #6
        ['L','P','R','J','B'],              #7
        ['W','B','Z','T','L','S','C','N'],  #8
        ['G','S','L'],                      #9
    ]

    result = ""
    for line in lines:
        line = line.strip()

        if line:
            values = line.split(" ")

            quantity = int(values[1])
            from_crate = int(values[3])
            to_crate = int(values[5])

            temp = crates[from_crate][:quantity]
            crates[to_crate] = temp + crates[to_crate]
            crates[from_crate] = crates[from_crate][quantity:]
    
    for j in range(1,10):
        result += crates[j].pop(0)

    print(result)
