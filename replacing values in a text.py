## replacing values in a text

def replace_string(orig_string, old_string, new_string):
    return orig_string.replace(old_string, new_string)

orig_string = "Greetings, everybody!"
old_string = "everybody"
new_string = "friends"
result = Answer.replace_string(orig_string, old_string, new_string)