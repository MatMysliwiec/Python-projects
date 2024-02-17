import random


def coin_flip(records):
    results = []
    heads = 0
    tails = 0
    for i in range(0, records):
        result = random.randint(1, 2)
        if result == 1:
            results.append("Head")
            heads += 1
        elif result == 2:
            results.append("Tail")
            tails += 1
    return results, heads, tails


times = int(input("Hoe many times do you want to flip a coin?: "))
result, heads, tails = coin_flip(times)
print(f"Record outcomes:\n", result)
print(f"Heads: {heads} \nTails: {tails}")
