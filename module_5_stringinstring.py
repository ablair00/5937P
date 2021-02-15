userText = input("What is a funny word at least four characters long?\n");
def stringinsert(userText, word):
    return userText[:2] + word + userText[2:];
print(stringinsert(userText, 'Python'));
