from check_arguments import check_arguments
import sys


def main():
    options, files = check_arguments(sys.argv[1:])
    print(options)
    print(files)


if __name__ == '__main__':
    main()