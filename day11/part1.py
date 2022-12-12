class Monkey:
    monkeys = list()

    def inspect(n):
        for i in range(n):
            for m in Monkey.monkeys:
                m.inspect_items()

    def get_monkey_business():
        l = sorted([m.inspections for m in Monkey.monkeys], reverse=True)
        return l[0] * l[1]


    def __init__(self, items, op_n, op_op, test, test_true, test_false):
        self.items = items
        self.op_n = op_n
        self.op_op = op_op
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.inspections = 0

        Monkey.monkeys.append(self)


    def operation(self, n):
        if self.op_op == "*":
            if self.op_n == 0:
                return n * n
            else:
                return n * self.op_n

        else:
            if self.op_n == 0:
                return n + n
            else:
                return n + self.op_n


    def inspect_items(self):
        while len(self.items) > 0:
            n = self.items.pop(0)
            self.inspections += 1

            n = self.operation(n) // 3
            
            if n % self.test == 0:
                Monkey.monkeys[self.test_true].items.append(n)
            else:
                Monkey.monkeys[self.test_false].items.append(n)


def main():
    with open("input") as f:
        for m in f.read().strip().split("\n\n"):
            monkey_s, items_s, op_s, test_s, t_s, f_s = m.split("\n")

            items = [int(x) for x in items_s.split(":")[1].split(",")]

            op_data = op_s.split(":")[1].split("=")[1].split()

            op_op = op_data[1]
            op_n = op_data[2]

            if op_n == "old":
                op_n = 0
            else:
                op_n = int(op_n)

            test = int(test_s.split(":")[1].split()[2])

            t = int(t_s.split(":")[1].split()[3])
            f = int(f_s.split(":")[1].split()[3])

            Monkey(items, op_n, op_op, test, t, f)

    Monkey.inspect(20)
    print(Monkey.get_monkey_business())

if __name__ == "__main__":
    main()
