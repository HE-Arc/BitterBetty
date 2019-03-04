# coding: utf-8

import sys, os

import BitterBetty

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
    print(file_path)
    try:
        f= open(file_path, "r")
        content = f.read()
        print(content)
        return content
    except Exception as e:
        print("error while reading file")
        print(e)
    finally:
        f.close()

class ConsoleInteraction:

    def __init__(self):
        pass

    def start(self):
        print("Welcome to console inteaction !")
        poems = list_poems()
        print("Chose a poem to read:")
        for num, poem in zip(range(1, len(poems)+1), poems):
            print("{0}. {1} by {2}".format(num, poem['name'], poem['author']))
        user_choice = int(input("Number: "))
        # print(f"choice: {user_choice}")
        poem_path = "poems/" + poems[user_choice-1]['path']
        # print(f"poem path: {poem_path}")
        text = read_file(poem_path)
        try:
            BitterBetty.BitterBetty().speak(text)
        except FileNotFoundError:
            print("Error")
            print("BitterBetty is not execute on the BeagleBone...")
        

        

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
