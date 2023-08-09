text = "习**近-平aaa十字弓，藏独，藏独"

new_text = text.replace("藏独", "*" * len("藏独"))

print(new_text)
