from check_arguments import check_arguments
import sys
import os


def get_file_stats(file, options):
    if file == "-" or file == " ":
        text = sys.stdin.read()
    else:
        f = open(file)
        text = f.read()

    stats = []
    max_len = -1

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

    return stats, max_len


def get_max_line_len(file):
    max_len = -1

    for line in file.split('\n'):
        if len(line) > max_len:
            max_len = len(line)

    return max_len


def get_total_stats(all_stats):
    col_nums = len(all_stats[0])
    total_stats = [0] * col_nums

    for row in all_stats:
        for i in range(col_nums):
            total_stats[i] += row[i]

    return total_stats


def process_files(files, options):
    all_stats = []
    overall_max = -1

    for file in files:
        stats, max_len = get_file_stats(file, options)
        all_stats.append(stats)
        
        if max_len > overall_max:
            overall_max = max_len

        if stats != []:
            print(*stats, "", end="")
        if options['-L']:
            print(max_len, "", end="")
        print(file)

    if len(files) > 1:
        total_stats = get_total_stats(all_stats)
        if total_stats != []:
            print(*total_stats, "", end="")
        if options['-L']:
            print(overall_max, "", end="")
        print("Total")


def main():
    options, files = check_arguments(sys.argv[1:])
    process_files(files, options)


if __name__ == '__main__':
    main()
