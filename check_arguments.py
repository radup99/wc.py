import sys

default_options = {  # if no options are specified through command line
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
        # first checks if the argument is a double dash command
        if arg == "--help":
            help_text = open("help.txt").read()
            print(help_text)
            return -1, -1

        elif arg.startswith("--files0-from="):
            count = get_files_from_txt(arg, files)
            if count != -1:
                files_count += count
            else:
                return -1, -1

        elif arg.startswith("--"):
            if arg not in long_options:
                print(f"wc: unrecognized option \'{arg}\'")
                return -1, -1
            else:
                options[long_options[arg]] = True
                option_count += 1

        # checks if it's a single dash command
        elif arg == "-":
            files.append("-")
            files_count += 1

        elif arg.startswith("-"):
            if arg not in options:
                print(f"wc: invalid option -- \'{arg[1:]}\'")
                return -1, -1
            else:
                options[arg] = True
                option_count += 1

        # if it's not either type of command, the argument is considered a file
        else:
            if is_file_valid(arg):
                files.append(arg)
                files_count += 1
            else:
                return -1, -1

    # selects the default options since no options were specified by the user
    if option_count == 0:  
        options = default_options

    if files_count == 0:
        files = [" "]  # keyboard input instead of files

    return options, files


def is_file_valid(arg):
    try:
        open(arg)
    except FileNotFoundError:
        print(f"wc: {arg}: No such file or directory")
        return False
    else:
        return True


def get_files_from_txt(arg, files):
    source_file = arg[14:]
    count = 0

    if source_file == "-":
        source = sys.stdin.read()
    else:
        try:
            source = open(source_file)
        except FileNotFoundError:
            print(f"wc: cannot open '{source_file}' for reading: "
                  "No such file or directory")
            return -1

    for file in source.read().split("\n"):
        if is_file_valid(file):
            files.append(file)
            count += 1
        else:
            return -1

    return count
