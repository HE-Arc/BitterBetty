# coding: utf-8

import sys, os

poems_dir = "poems"

def list_poems():
    poems_filepath = [fn for fn in os.listdir(poems_dir)]
    path_names_writers = []
    for fpath in poems_filepath:
        fn = os.path.splitext(fpath)[0]
        [name, author] = fn.split('_')
        path_names_writers.append({'path': fpath, 'name':name, 'author':author})
    return path_names_writers

def read_file(file_path):
    try:
        content = os.read(file_path)
        print(content)
        return(content)
    except:
        print("error while reading file")

class ConsoleInteraction:

    def __init__(self):
        pass

    def start(self):
        print("Welcome to console inteaction !")
        poems = list_poems()
        print("Chose a poem to read:")
        for num, poem in zip(range(1, len(poems)+1), poems):
            print(f"{num}. {poem['name']} by {poem['author']}")
        user_choice = int(input("Number: "))
        print(f"choice: {user_choice}")
        read_file("poems\" + poems[user_choice-1]['path'])
        

    def quit(self):
        quit()

interactions = {
    "console": ConsoleInteraction,
}

if __name__ == "__main__":
    inter = None
    try:
        inter = interactions[sys.argv[1]]()
    except:
        inter = interactions["console"]()
    inter.start()
