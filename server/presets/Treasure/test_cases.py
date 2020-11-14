import random
def gen(amount=50000):
    testcases = []
    for o in range(amount): 
        case = []
        units = random.choice([10, 100])
        for i in range(5):
            case.append(random.randint(1, units))
        testcases.append(case)
    return testcases

cases = gen(amount=100)
