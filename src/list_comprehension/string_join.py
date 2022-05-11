
def join_string_imp(strings: list) -> str:
    string = ""
    for s in strings:
        string = string + " " + s
    return string.strip()  # strips away leading and trailing whitespaces


def join_string_functional(strings: list) -> str:
    return " ".join(strings)


def main():
    string_list = ['Python', 'is', 'awesome']
    print(join_string_imp(string_list))
    print(join_string_functional(string_list))


if __name__ == '__main__':
    main()
