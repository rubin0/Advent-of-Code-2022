def check(left, right):
    match left, right:
        case int(), int():
            return left - right
        case list(), list():
            for l, r in zip(left, right):
                diff = check(l, r)
                if diff:
                    return diff
            return len(left) - len(right)
        case list(), int():
            return check(left, [right])
        case int(), list():
            return check([left], right)


with open("input13b.txt") as f:
    s = f.read().strip().split("\n")

couples = [(eval(s[x]), eval(s[x+1])) for x in range(0, len(s), 3)]

index = 1
right_order = []
for couple in couples:
    left, right = couple

    if check(left, right) < 0:
        right_order.append(index)

    index += 1

print(sum(right_order))
