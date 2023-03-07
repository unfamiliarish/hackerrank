# Enter your code here. Read input from STDIN. Print output to STDOUT


def format_split(output_type, input_word):
    if input_word == "":
        return ""

    if output_type == "M":
        input_word = input_word[:-2]

    words = []
    start_index = 0
    for i in range(1, len(input_word)):
        if input_word[i].isupper():
            word = input_word[start_index:i]
            words.append(word)
            start_index = i

    last_word = input_word[start_index : len(input_word) + 1]
    words.append(last_word)

    words = [word.lower() for word in words]

    return " ".join(words)


assert format_split("V", "") == ""
assert format_split("V", "b") == "b"
assert format_split("V", "oneT") == "one t"
assert format_split("V", "oneTwo") == "one two"
assert format_split("M", "FooBarB()") == "foo bar b"
assert format_split("M", "FooBarBaz()") == "foo bar baz"
assert format_split("C", "FooBarB") == "foo bar b"
assert format_split("C", "FooBarBaz") == "foo bar baz"


def format_combine(output_type, word):
    # list of words, lower and space delimited
    if word == "":
        return "" if output_type != "M" else "()"

    words = word.split()
    final_words = [word.capitalize() for word in words]
    if output_type != "C":
        final_words[0] = final_words[0].lower()

    combined = "".join(final_words)
    if output_type == "M":
        combined = combined + "()"

    return combined


assert format_combine("V", "") == ""
assert format_combine("V", "b") == "b"
assert format_combine("V", "mobile phone") == "mobilePhone"
assert format_combine("M", "white sheet of paper") == "whiteSheetOfPaper()"
assert format_combine("C", "coffee machine") == "CoffeeMachine"


def format(string):
    if not string:
        return ""

    string = string.strip()
    breakpoint
    task, output_type, word = string.split(";")

    if task == "S":
        # split case
        return format_split(output_type, word)
    elif task == "C":
        # combine case
        return format_combine(output_type, word)
    else:
        raise ValueError("malformed input")


assert format("S;V;pictureFrame") == "picture frame"
assert format("S;C;LargeSoftwareBook\n\r") == "large software book"
assert format("S;M;plasticCup()") == "plastic cup"
assert format("C;V;mobile phone text") == "mobilePhoneText"
assert format("C;C;coffee machine") == "CoffeeMachine"
assert format("C;C;coffee") == "Coffee"
assert format("C;M;white sheet of paper\n") == "whiteSheetOfPaper()"
