import helpers
from functools import cmp_to_key

def compare(left, right):
    # retval of -1 means left is less than right
    # retval of 1 means left is greater than right
    # retval of 0 means they are equal

    if type(left) == int and type(right) == int:
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif type(left) == list and type(right) == list:
        
        i = 0
        while i < len(left) and i < len(right):
            cmp = compare(left[i], right[i])
            if cmp == -1:
                return cmp
            elif cmp == 1:
                return cmp
            i += 1
        
        if i == len(left) and i < len(right):
            return -1
        elif i < len(left) and i == len(right):
            return 1
        else:
            # not really specified what to do here..
            return 0

    elif type(left) == list and type(right) == int:
        return compare(left, [right])
    elif type(left) == int and type(right) == list:
        return compare([left], right)

    # shouldn't be making it here...
    return None

if __name__=='__main__':
    data = open('input.txt').read().strip()

    packets = [[[2]], [[6]]]
    for i, lists in enumerate(data.split('\n\n')):
        [l1, l2] = lists.split('\n')

        packets.append(eval(l1))
        packets.append(eval(l2))

    packets.sort(key=cmp_to_key(compare))

    for p in packets:
        print(p)

    print((packets.index([[2]])+1) * (packets.index([[6]])+1)) # 24180
    



