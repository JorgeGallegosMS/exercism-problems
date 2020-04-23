# Manage a game player's High Score list.

# Your task is to build a high-score component of the classic Frogger game, one of the highest selling and addictive
# games of all time, and a classic of the arcade era. Your task is to write methods that return the highest score
# from the list, the last added score and the three highest scores.

# Test inputs:
# Good: [30, 20, 40, 50]
# Unusual: [45, 17.9, 20.33]
# Edge: ['35', 19, 1, '64']

# Assuming I can't just use sort()

def latest(scores):
    return scores[-1]


def personal_best(scores):
    highest = 0

    for index in range(len(scores)):
        if highest > scores[index]:
            continue

        highest = scores[index]

    return highest


def personal_top_three(scores):
    if len(scores) >= 3:
        num_results = 3
    else:
        num_results = len(scores)

    top_three = []

    for _ in range(num_results):
        highest_index = 0

        for index in range(len(scores)):
            if scores[highest_index] > scores[index]:
                continue

            highest_index = index

        top_three.append(scores[highest_index])
        scores.pop(highest_index)

    return top_three

    
