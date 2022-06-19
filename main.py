from random import randint


class Market:
    def __init__(self, cash, id):
        if isinstance(cash, int):
            self.cash = cash
        else:
            self.cash = 0
            print("Not valid operand for self.cash (was set as 0)")
        if isinstance(id, int):
            self.id = id
        else:
            self.id = randint(0, 1000)
            print("Not valid operand for self.id (was set as " + str(self.id) + ")")
        # if isinstance(name, str):
        #     self.name = name
        # else:
        #     self.name = "default"
        #     print("Not valid operand for self.name (was set as 'default')")
        self.open = True

    def __eq__(self, other):
        if isinstance(other, Market):
            return self.id == other.id
        else:
            return "Not valid operand for comparison"

    def __bool__(self):
        return self.open

    def add_cash(self, other):
        self.cash += other
        return self

    def take_cash(self, other):
        if isinstance(other, int):
            self.cash -= other
        else:
            self.cash -= 100
        if self.cash <= 0:
            self.open = False
        return self


def market_simulation(markets, add_min, add_max, take, limit):
    left = len(markets)
    count = [0]*left
    while max(count) < limit and left > 0:
        for i in range(len(markets)):
            if markets[i]:
                markets[i].add_cash(randint(add_min, add_max))
                markets[i].take_cash(take)
                count[i] += 1
                if not markets[i]:
                    print("The market#", i + 1, " went bankrupt with the capital of ", markets[i].cash,
                          ", being open for ", count[i], " iteration", sep='', end='')
                    if count[i] > 1:
                        print("s")
                    else:
                        print("")
                    left -= 1
    if max(count) >= limit:
        print("The simulation was interrupted, because the counter of one of the markets crossed the limit")
    else:
        print("The simulation is over, as all markets went bankrupt")
    return


# CREATION OF THE LIST OF THE MARKETS
while True:
    print("Welcome to the market simulation.")
    print(
        "Enter \"manual\" if you want to create the list of markets yourself or \"random\" if you want to randomize it:")
    mode = input()
    if mode == "manual":
        print("Enter the number of markets:")
        markets_count = int(input())
        markets = []
        for i in range(markets_count):
            print("Enter the initial capital value and the id of the market#", i + 1, ", divided by spaces:", sep='')
            cash, ind = map(int, input().split())
            markets.append(Market(cash, ind))
        print("The list of markets:")
        for i in range(len(markets)):
            print("Market #", i + 1, ": id is ", markets[i].id, ", initial capital is ", markets[i].cash, sep='')
        break
    elif mode == "random":
        print("Enter the maximum number of markets:")
        markets_count = int(input())
        print("Enter the maximum value for initial capital:")
        cash_max = int(input())
        print("The creation of the list of markets has been started...")
        print("The list of markets:")
        markets = []
        for i in range(randint(1, markets_count)):
            markets.append(Market(randint(1, cash_max), i))
            print("Market #", i + 1, ": id is ", i, ", initial capital is ", markets[i].cash, sep='')
        break

# STARTING THE SIMULATION
while True:
    print("\nEnter \"manual\" if you want to set the simulation" +
          " parameters yourself or \"random\" if you want to randomize it:")
    mode = input()
    if mode == "manual":
        print("Enter the minimum and maximum values for adding cash, divided by spaces:")
        add_min, add_max = map(int, input().split())
        print("Enter the value for taking cash:")
        take = int(input())
        print("Enter the value for the iteration counter limit:")
        limit = int(input())
        break
    elif mode == "random":
        nums = [randint(0, 1000), randint(0, 1000), randint(0, 1000)]
        nums.sort()
        add_min = nums[0]
        add_max = nums[2]
        take = nums[1]
        limit = randint(500, 5000)
        print("The minimum and maximum values for adding cash are ", add_min, " and ", add_max,
              ", the value for taking cash is ", take, ", the value for the iteration counter limit is ", limit, sep='')
        break
while True:
    print("\nPress 'Enter' to start the simulation...")
    inp = input()
    if inp == "":
        break
print("The market simulation has been started...")
market_simulation(markets, add_min, add_max, take, limit)
