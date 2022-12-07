import helpers
import sys

class file:
    def __init__(self, name, parent, size=0):
        self.size = size
        self.name = name
        self.parent = parent

    def __eq__(self, other):
        # hmm I wonder if recursion will work here....
        return self.size == other.size and self.name == other.name and self.parent == other.parent

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        if self.size == 0:
            return '{} (dir)'.format(self.name)
        else:
            return '{} (file, size={})'.format(self.name, self.size)


def GetDirectorySize(file_tree, file_name, accumulator):
    for contained_file in file_tree[file_name]:
        print(contained_file.name)
        if contained_file.size == 0:
            # size 0 means it's a directory
            accumulator += GetDirectorySize(file_tree, contained_file.name, accumulator)
        else:
            accumulator += contained_file.size
    return accumulator


if __name__ == '__main__':
    file_tree = {}
    with open('input.txt', 'r') as f:
        parent = '/'
        for line in f:
            input = line.strip().split()

            if input[0].startswith('$'):
                # command
                if input[1].startswith('cd'):
                    # change directory
                    if input[2].startswith('..'):
                        # go up one directory
                        parent = file_tree[parent][0].parent
                    elif input[2].startswith('/'):
                        # go to home
                        parent = '/'
                    else:
                        parent = input[2]
                elif input[1].startswith('ls'):
                    # list files
                    pass
                
            elif input[0].startswith('dir'):
                # directory
                if parent in file_tree:
                    file_tree[parent] += [file(input[1], parent)]
                else:
                    file_tree[parent] = [file(input[1], parent)]
            else:
                # file
                if parent in file_tree:
                    file_tree[parent] += [file(input[1], parent, int(input[0]))]
                else:
                    file_tree[parent] = [file(input[1], parent, int(input[0]))]

    directory_sizes = []
    for parent_name, contained_files in file_tree.items():
        # list type indicates directory
        file_size = GetDirectorySize(file_tree, parent_name, 0)
        if file_size <= 100000:
            directory_sizes += [file_size]

    print(sum(directory_sizes))

    # this is the problem: there can be duplicate folder names with different parent folders...
    # my current algorithm does not account for this....
    # me at 12:30 am: https://youtu.be/7hx4gdlfamo