import helpers
import math

class Monkey:
    monkey_num = None
    items = []
    inspect_operation = ''
    test = None
    true_test = None
    false_test = None
    inspect_count = 0
    lcm = 0 # least common multiple

    def __init__(self, monkey_num):
        self.monkey_num = monkey_num

    def inspect(self):
        to_monkeys = []
        self.inspect_count += len(self.items)

        for i, old in enumerate(self.items):
            self.items[i] = eval(self.inspect_operation) % self.lcm # (17*3*19*7*2*5*11*13))
            if self.items[i] % self.test == 0:
                to_monkeys.append(self.true_test)
            else:
                to_monkeys.append(self.false_test)

        return to_monkeys


if __name__ == '__main__':

    monkeys = []
    with open('input.txt', 'r') as f:
        for i, line in enumerate(f):
            if line.startswith('Monkey'):
                monkey_num = int(helpers.ParseLine('Monkey {}:', line)[0])
                monkeys.append(Monkey(monkey_num))

            if len(monkeys) > 0:
                if line.strip().startswith('Starting items'):
                    nums = line[line.index(':')+1:].strip().split(',')
                    int_nums = []
                    for num in nums:
                        int_nums += [int(num.strip())]
                    monkeys[-1].items = int_nums.copy()
            
                elif line.strip().startswith('Operation'):
                    monkeys[-1].inspect_operation = line[line.index('=')+1:].strip()

                elif line.strip().startswith('Test'):
                    monkeys[-1].test = int(helpers.ParseLine('divisible by {}\n', line)[0])
                
                elif line.strip().startswith('If true'):
                    monkeys[-1].true_test = int(line.strip().split()[-1])

                elif line.strip().startswith('If false'):
                    monkeys[-1].false_test = int(line.strip().split()[-1])


    lcm = 1
    for monk in monkeys:
        lcm = (lcm * monk.test) // math.gcd(lcm, monk.test)

    for monk in monkeys:
        monk.lcm = lcm

    for round in range(10000):
        for i, monkey in enumerate(monkeys):
            new_monkeys = monkey.inspect()

            for j, new_monkey in enumerate(new_monkeys):
                monkeys[new_monkey].items.append(monkey.items[j])

            # after inspecting, the monkey will no longer have any items
            monkey.items = []

    monkey_business = []
    for monkey in monkeys:
        monkey_business += [monkey.inspect_count]

    monkey_business.sort()
    print(monkey_business[-1] * monkey_business[-2]) # 25935263541