import sys

default_options = {
    "-l": True,
    "-w": True,
    "-c": True,
    "-m": False,
    "-L": False,
}

long_options = {
    "--lines": "-l",
    "--words": "-w",
    "--bytes": "-c",
    "--chars": "-m",
    "--max-line-length": "-L"
}


def check_arguments(args):
    options = {
        "-l": False,
        "-w": False,
        "-c": False,
        "-m": False,
        "-L": False,
    }
    option_count = 0

    files = []
    files_count = 0

    for arg in args:
        if arg.startswith("--"):
            if arg not in long_options:
                print(f"wc: unrecognized option \'{arg}\'")
                return -1, -1
            else:
                options[long_options[arg]] = True
                option_count += 1

        elif arg.startswith("-"):
            if arg not in options:
                print(f"wc: invalid option -- \'{arg[1:]}\'")
                return -1, -1
            else:
                options[arg] = True
                option_count += 1

        elif arg == "-":
            files.append("-")
            files_count += 1

        else:
            if is_file_valid(arg):
                files.append(arg)
                files_count += 1
            else:
                return -1, -1

    if option_count == 0:
        options = default_options

    if files_count == 0:
        files = ["-"]

    return options, files


def is_file_valid(arg):
    try:
        f = open(arg)
    except FileNotFoundError:
        print(f"wc: {arg}: No such file or directory")
        return False
    else:
        return True


def main():
    print(check_arguments(sys.argv[1:]))


if __name__ == '__main__':
    main()
