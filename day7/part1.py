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

    def check_size(self):
        size = 0
        res = 0

        for subdir in self.dirs.values():
            dir_size, tot_size = subdir.check_size()
            size += dir_size
            res += tot_size

        if size > 100000:
            return size, res

        for f in self.files:
            size += f.size

        if size > 100000:
            return size, res

        return size, res + size


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)


def main():
    root = Dir("/")
    current_dir = root

    with open("input") as f:
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

    print(root.check_size()[1])

if __name__ == "__main__":
    main()
