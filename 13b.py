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


with open("input13.txt") as f:
    s = [eval(s) for s in f.read().strip().split("\n") if s != ""]

pre = 0
middle = 0
post = 0
for x in s:
    if check(x, [[2]]) < 0:
        pre += 1
    elif check([[6]], x) < 0:
        post += 1
    else:
        middle += 1

print((pre+1) * (pre + 1 + middle + 1))
