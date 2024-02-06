def secret_replace(text: str, **replaces) -> str:  # : tuple
    for old_letter, new_letter in replaces.items():
        counter = 0
        while old_letter in text:
            text = text.replace(old_letter, new_letter[counter], 1)
            counter += 1
            if counter == len(new_letter):
                counter = 0
    return text

print(secret_replace('a', a=('aa', 'aaa')))
result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))
print(result)
# result = 'Hehiy123, wzrhid!'
result = secret_replace(
    "ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),
)
# result = 'Z3X1-G!0Z371'
print(result)
