from preprocessing import preprocess_text
with open("input.txt", "r") as file:
    text = file.read()

tokens = preprocess_text(text)

with open("output.txt", "w") as file:
    file.write("Tokenized Output:\n")
    file.write(str(tokens))

print("Processing complete! Check output.txt for results.")