# A for Rock, B for Paper, and C for Scissors
# X means lose, Y means draw, and Z means win

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

            my_choice = ''
            if choices[1] == 'X':
                # lose
                my_choice = chr(((ord(choices[0]) - 65 - 1) % 3) + 88)
            elif choices[1] == 'Y':
                # draw
                my_choice = chr(((ord(choices[0]) - 65) % 3) + 88)
            elif choices[1] == 'Z':
                # lose
                my_choice = chr(((ord(choices[0]) - 65 + 1) % 3) + 88)

            score += get_winner(choices[0], my_choice)

    print(score) # 13448
