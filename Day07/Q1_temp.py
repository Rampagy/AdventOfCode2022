import helpers

class file:
    def __init__(self, name, parent, size=0):
        self.size = size
        self.name = name
        self.parent = parent

    def __repr__(self):
        if self.size == 0:
            return '{} (dir)'.format(self.name)
        else:
            return '{} (file, size={})'.format(self.name, self.size)


def GetDirectorySize(file_tree, file_name, accumulator, files_accumulated):
    for contained_file in file_tree[file_name]:
        if contained_file.size == 0:
            # size 0 means it's a directory
            files_accumulated += [contained_file.name]
            accumulator += GetDirectorySize(file_tree, contained_file.name, accumulator, files_accumulated)
        else:
            files_accumulated += [contained_file.name]
            accumulator += contained_file.size
    return accumulator

if __name__ == '__main__':
    file_tree = {}
    with open('test0.txt', 'r') as f:
        parent = '/'
        for line in f:
            input = line.strip().split()

            if input[0].startswith('$'):
                # command
                if input[1].startswith('cd'):
                    # change directory
                    if input[2].startswith('..'):
                        # go up one directory
                        parent = file_tree[parent][-1].parent
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

    already_summed_files = []
    directory_sizes = []
    for parent_name, contained_files in file_tree.items():
        if isinstance(file_tree[parent_name], list):
            # list type indicates directory
            summed_files = []
            file_size = GetDirectorySize(file_tree, parent_name, 0, summed_files)
            if file_size <= 100000 and parent_name not in already_summed_files:
                already_summed_files += summed_files
                directory_sizes += [file_size]

    print(sum(directory_sizes))