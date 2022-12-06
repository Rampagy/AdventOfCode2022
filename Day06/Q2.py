import helpers

if __name__ == '__main__':
    input = ''
    with open('input.txt', 'r') as f:
        for line in f:
            input = line.strip()
    
    for i in range(0, len(input)-13):
        test_string = input[i:i+14]
        if len(set(test_string)) == len(test_string):
            print(i+14, test_string) # 3217
            break