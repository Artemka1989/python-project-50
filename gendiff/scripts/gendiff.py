import argparse


def main():
    parser = argparse.ArgumentParser('Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    args = parser.parse_args()
    print(args.first_file)


if __name__ == '__main__':
    main()