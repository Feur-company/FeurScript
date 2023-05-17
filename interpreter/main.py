import argparse

def main():
    parser = argparse.ArgumentParser(description='Run FeurScript program.')
    parser.add_argument('-f','--file', help='Input FeurScript file', required=True)
    args = parser.parse_args()
    filename = args.file
    file = open(filename, 'r')
    code = file.read()
    code = code.replace(" ", "")
    code = code.splitlines()
    variables = {}
    for line in code:
        print(line)

if __name__ == '__main__':
    main()