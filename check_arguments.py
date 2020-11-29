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
    "--bytes": "-b",
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

    for arg in args:
        if arg.startswith("--"):
            if arg not in long_options:
                return -1, -1
            else:
                options[long_options[arg]] = True
                option_count += 1

        elif arg.startswith("-"):
            if arg not in options:
                return -1, -1
            else:
                options[arg] = True
                option_count += 1

    if option_count == 0:
        return default_options, []
    return options, []


def main():
    print(check_arguments(sys.argv[1:]))


if __name__ == '__main__':
    main()
