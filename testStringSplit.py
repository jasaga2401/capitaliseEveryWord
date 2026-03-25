
def to_jaden_case(string):

    string = string.split()
    x = 0

    for word in string:

        string[x] = word.capitalize()
        x += 1

    string = " ".join(string)

    return string

string = 'Hello you good people'
to_jaden_case(string)
