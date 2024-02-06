def number_length(arg: int):
    return len([num for num in str(arg) if num.isdigit()])


print(number_length(-1232245))
