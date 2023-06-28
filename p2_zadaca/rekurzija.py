def print_string_recursive(string):
    if len(string) == 0:
        return
    else:
        print(string[0], end="")
        print_string_recursive(string[1:])

string = "Antonio! "

print_string_recursive(string)
