import getopt


def parse_file_name(argv):
    if len(argv) == 1:
        opts, args = getopt.getopt(argv, "", "")
        file_name = args[0]
    else:
        file_name = input('file to parse:')
    print(file_name)
    return file_name
