# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

def get_winner(player, me):
    score = 0
    if me == 'X':
        score += 1
    elif me == 'Y':
        score += 2
    elif me == 'Z':
        score += 3

    if ((player == 'A') and (me == 'Y')) or \
            ((player == 'B') and (me == 'Z')) or \
            ((player == 'C') and (me == 'X')):
        # me wins
        score += 6
    elif ((player == 'A') and (me == 'X')) or \
            ((player == 'B') and (me == 'Y')) or \
            ((player == 'C') and (me == 'Z')):
        # tie
        score += 3

    return score


if __name__ == '__main__':
    # read in text file
    score = 0
    with open('input.txt', 'r') as f:
        for line in f:
            choices = line.strip().split(' ')

            score += get_winner(choices[0], choices [1])

    print(score) # 13924
