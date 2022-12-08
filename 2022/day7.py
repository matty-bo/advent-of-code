import re


class FileSystemObject:
    def __init__(self, name, size, parent=None):
        self.name = name
        self.size = size
        self.parent = parent

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class FileObject(FileSystemObject):
    def __init__(self, name, size, parent=None):
        super().__init__(name, size, parent)
        self.type = 'file'

    def __str__(self):
        return f"{self.name} ({self.type}, size={self.size})"

    def __repr__(self):
        return f"{self.name} (file, size={self.size})"


class DirObject(FileSystemObject):
    def __init__(self, name, size=0, parent=None):
        super().__init__(name, size, parent)
        self.type = 'dir'
        self.children = []

    def add_child(self, obj):
        if obj.name in (c.name for c in self.children):
            return False
        obj.parent = self
        self.children.append(obj)
        return True

    def __str__(self):
        return f"{self.name} ({self.type}, size={self.size})"

    def __repr__(self):
        return f"{self.name} ({self.type}, size={self.size})"


def main():
    filename = "inputs/input7"
    with open(filename) as file:
        terminal_output = file.read().splitlines()

    root_directory = None
    current_directory = None
    for line in terminal_output:
        cd_command_match = re.match(r'\$ cd (.+)', line)
        ls_command_match = re.match(r'\$ ls', line)
        dir_match = re.match(r'dir (.*)', line)
        file_match = re.match(r'(\d*) (.*)', line)
        if cd_command_match:
            next_directory_name = cd_command_match.group(1)
            if next_directory_name == '/':
                root_directory = DirObject('/', 0)
                current_directory = root_directory
            elif next_directory_name == '..':
                current_directory = current_directory.parent
            else:
                next_directory = [
                    c for c in current_directory.children
                    if c.name == next_directory_name
                ][0]
                current_directory = next_directory
        elif ls_command_match:
            pass
        elif dir_match:
            new_directory_name = dir_match.group(1)
            new_directory = DirObject(new_directory_name, 0)
            current_directory.add_child(new_directory)
        elif file_match:
            file_size, file_name = file_match.groups()
            file_size = int(file_size)
            new_file = FileObject(file_name, file_size)
            current_directory.add_child(new_file)

    ans1 = part1(root_directory)
    ans2 = part2(root_directory)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')


def calculate_directory_size(obj):
    if not obj:
        return 0
    elif isinstance(obj, FileObject):
        return obj.size
    elif isinstance(obj, DirObject):
        for child in obj.children:
            child_size = calculate_directory_size(child)
            obj.size += child_size
        return obj.size


def print_filesystem(root, level=0):
    if root:
        print(2 * level * ' ' + f"- {root}")
    if isinstance(root, FileObject):
        return
    for child in root.children:
        print_filesystem(child, level + 1)


def get_directory_sizes(root, sizes):
    if isinstance(root, DirObject):
        sizes.append(root.size)
        for child in root.children:
            get_directory_sizes(child, sizes)
    return sizes


def part1(root_directory):
    calculate_directory_size(root_directory)
    sizes = get_directory_sizes(root_directory, [])
    THRESHOLD = 100_000
    sizes_under_thresholds = filter(lambda size: size < THRESHOLD, sizes)
    ans = sum(sizes_under_thresholds)
    return ans


def part2(root_directory):
    TOTAL_SPACE = 70000000
    NEDEED_UNUSED_SPACE = 30000000
    currently_unused_space = TOTAL_SPACE - root_directory.size
    space_to_free = NEDEED_UNUSED_SPACE - currently_unused_space

    sizes = get_directory_sizes(root_directory, [])
    size_deltas = [(size, size - space_to_free) for size in sizes]
    directory_sizes_with_enough_space = [
        (size, delta) for size, delta in size_deltas
        if delta >= 0
    ]
    size_with_minimum_delta = min(directory_sizes_with_enough_space, key=lambda x: x[1])
    ans2 = size_with_minimum_delta[0]
    return ans2


if __name__ == '__main__':
    main()
