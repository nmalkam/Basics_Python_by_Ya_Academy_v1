file_in, file_out = input(), input()
data = []
with open(file_in, "r") as file:
    for string in file:
        data.append(string.strip().replace("\t", "").split())
data = [item for item in data if any(item)]
with open(file_out, "w") as file:
    for string in data:
        print(" ".join(string), file=file)


file_in = input()
file_out = input()

with open(file_in, encoding="UTF-8") as file_in:
    text = file_in.read()

while text.find("\t") + 1:
    text = text.replace("\t", "")
while text.find("  ") + 1:
    text = text.replace("  ", " ")

text = "\n".join(string.strip() for string in text.split("\n") if string)

with open(file_out, "w", encoding="UTF-8") as file_out:
    file_out.write(text)
