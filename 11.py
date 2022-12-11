import re
from operator import mul

class Monkey():

    item_inspected = 0

    def __init__(self, starting_items, operation, test, test_true, test_false) -> None:
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.test_true = test_true
        self.test_false = test_false

    def inspect(self, monkeys):
        for worry_level in self.starting_items:
            operator, operand = self.operation

            if operand == "old":
                operand = worry_level
            else:
                operand = int(operand)

            if operator == "+":
                worry_level += operand
            if operator == "*":
                worry_level *= operand

            worry_level //= 3

            next_monkey = self.test_true if worry_level % self.test == 0 else self.test_false
    
            monkeys[next_monkey].starting_items.append(worry_level)

            self.item_inspected += 1

        self.starting_items = []


with open('input11.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    monkeys = []

    i = 0

    starting_items = None
    operation = None
    test = None
    testTrue = None
    testFalse = None
    
    for line in lines:
        line = line.strip()
        
        if i == 7:
            i = 0

        if i == 0:
            pass
        if i == 1:
            starting_items = [int(s) for s in re.findall(r'\d+', line)]
        if i == 2:
            operation = line.split(" ")[-2:]
        if i == 3:
            test = int(line.split(" ")[-1])
        if i == 4:
            testTrue = int(line.split(" ")[-2:].pop())
        if i == 5:
            testFalse = int(line.split(" ")[-2:].pop())
            monkeys.append(Monkey(starting_items, operation,
                           test, testTrue, testFalse))
        if i == 6:
            pass
        i += 1

    for i in range(20):
        for monkey in monkeys:
            monkey.inspect(monkeys)

    a,b = sorted(monkeys, key=lambda x: x.item_inspected, reverse=True)[:2]
    print(a.item_inspected * b.item_inspected)
