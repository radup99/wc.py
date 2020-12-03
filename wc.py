from check_arguments import check_arguments
import sys
import os


def get_file_stats(file, options):
    f = open(file)
    text = f.read()
    stats = []

    if options['-l']:
        line_count = text.count('\n')
        stats.append(line_count)

    if options['-w']:
        word_count = len(text.split())
        stats.append(word_count)

    if options['-c']:
        byte_count = os.path.getsize(file)
        stats.append(byte_count)

    if options['-m']:
        char_count = len(text)
        stats.append(char_count)

    if options['-L']:
        max_len = get_max_line_len(text)
        stats.append(max_len)

    return stats


def get_max_line_len(file):
    max_len = -1

    for line in file.split('\n'):
        if len(line) > max_len:
            max_len = len(line)

    return max_len


def process_files(files, options):
    all_stats = []

    for file in files:
        stats = get_file_stats(file, options)
        all_stats.append(stats)
        print(*stats, file)


def main():
    options, files = check_arguments(sys.argv[1:])
    all_stats = []

    process_files(files, options)


if __name__ == '__main__':
    main()