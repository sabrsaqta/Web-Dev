def split_and_join(line):
    # write your code here
    lst = line.split(" ")
    string = "-".join(lst)
    return string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)