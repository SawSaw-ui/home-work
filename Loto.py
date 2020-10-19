import random


def loto(card):
    nums = []
    while len(nums) < 5:
        elem = str(random.randint(1, 90))
        if elem not in card:
            nums.append(elem)
            card.append(elem)
    nums = list(nums) + list(' ' * 16)
    random.shuffle(nums)
    return ' '.join(nums)


card = []
for _ in range(3):
    print(loto(card))
