import helpers

if __name__ == '__main__':
    input = ''
    with open('input.txt', 'r') as f:
        for line in f:
            input = line.strip()
    
    for i in range(0, len(input)-3):
        test_string = input[i:i+4]
        if len(set(test_string)) == len(test_string):
            print(i+4, test_string) # 1175
            break