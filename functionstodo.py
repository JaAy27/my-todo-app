## FROM ITS OWN PERSPECTIVE, THIS IS A SCRIPT
#FROM THE "MAIN" OR DAY 14 :)) , THIS IS A MODULE.
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
     to-do items.""" # doc-string
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines() # closes the file implicitly
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH): # default parameter is FIRST!
    """ Write to-do items list in the text file."""
    with open("todos.txt", 'w') as file_local:
        file_local.writelines(todos_arg) #doesn't need to return anything


## If you want to print only when this file is executed directly but not when imported
# print(__name__) ## prints __main__ : someone is running this script directly
#but when the file is run indiretly through import print(__name__) will print functionstodo


if __name__ == "__main__": #if run directly here so this file is called __main__ but if run indirectly, this file<s name will be functionstodo
    print("Hello")
    print(get_todos())

#used for web apps ^^

