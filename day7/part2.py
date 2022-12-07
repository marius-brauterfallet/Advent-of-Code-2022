class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.dirs = dict()
        self.files = set()

    def add_dir(self, dirname):
        new_dir = Dir(dirname, self)
        self.dirs[dirname] = new_dir
        return new_dir

    def add_file(self, filename, size):
        self.files.add(File(filename, size))

    def check_size(self, sizes):
        size = 0

        for d in self.dirs.values():
            size += d.check_size(sizes)

        for f in self.files:
            size += f.size

        sizes.append(size)

        return size

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)


def main():
    root = Dir("/")
    current_dir = root

    with open("test_input") as f:
        for line in f:
            data = line.strip().split()

            if data[0] == "$":
                if data[1] == "cd":
                    if data[2] == "..":
                        current_dir = current_dir.parent

                    elif data[2] == "/":
                        current_dir = root

                    elif data[2] in current_dir.dirs:
                        current_dir = current_dir.dirs[data[2]]

                    else:
                        current_dir = current_dir.add_dir(data[2])

            elif data[0] == "dir":
                current_dir.add_dir(data[1])

            else:
                current_dir.add_file(data[1], data[0])

    sizes = list()
    used_space = root.check_size(sizes)

    free_space = 70000000 - used_space
    needed_space = 30000000 - free_space

    res = min([x for x in sizes if x > needed_space])
    print(res)

if __name__ == "__main__":
    main()
