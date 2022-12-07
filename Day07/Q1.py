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


def GetDirectorySize(file_tree, file_name, accumulator, files_accumulated):

    for contained_file in file_tree[file_name]:
        if contained_file.name not in files_accumulated:
            #print(contained_file.name, files_accumulated)
            files_accumulated += [contained_file.name]

            if contained_file.size == 0:
                # size 0 means it's a directory
                GetDirectorySize(file_tree, contained_file.name, accumulator, files_accumulated)
            else:
                accumulator += [contained_file.size]

    return


def CreateAbsPath(parent, name):
    abs_path = ''
    if parent != '/':
        abs_path = parent + '/' + name
    else:
        abs_path = parent + name
    return abs_path

if __name__ == '__main__':
    file_tree = {}
    with open('input.txt', 'r') as f:
        parent = ''
        for line in f:
            input = line.strip().split()

            if input[0].startswith('$'):
                # command
                if input[1].startswith('cd'):
                    # change directory
                    if input[2].startswith('..'):
                        # go up one directory
                        parent = '/'.join(parent.split('/')[:-1])
                    elif input[2].startswith('/'):
                        # go to home
                        parent = '/'
                    else:
                        # go to listed dir
                        parent = CreateAbsPath(parent, input[2])
                elif input[1].startswith('ls'):
                    # list files
                    pass
                
            elif input[0].startswith('dir'):
                # directory
                new_file = file(CreateAbsPath(parent, input[1]), parent)

                if parent in file_tree:
                    file_tree[parent] += [new_file]
                else:
                    file_tree[parent] = [new_file]
            else:
                # file
                new_file = file(CreateAbsPath(parent, input[1]), parent, int(input[0]))

                if parent in file_tree:
                    file_tree[parent] += [new_file]
                else:
                    file_tree[parent] = [new_file]

    already_summed_files = []
    directory_sizes = []
    for parent_name, contained_files in file_tree.items():
        # list type indicates directory
        summed_files = [parent_name]
        file_sizes = [0]
        GetDirectorySize(file_tree, parent_name, file_sizes, summed_files)
        #print(sum(file_sizes), parent_name, summed_files)
        if sum(file_sizes) <= 100000:
            already_summed_files += summed_files
            directory_sizes += [sum(file_sizes)]



    print(sum(directory_sizes)) # 1490523

    # this is the problem: there can be duplicate folder names with different parent folders...
    # my current algorithm does not account for this....
    # me at 12:30 am: https://youtu.be/7hx4gdlfamo