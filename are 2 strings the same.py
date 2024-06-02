show_expected_result = False
show_hints = False

# Your code goes here
def check_strings(string1, string2):
    if string1 == string2:
        print(True)
        return True
    else:
        print(False)
    return False

string1 = "Apple"
string2 = "Orange"

check_strings(string1, string2)