# coding: utf-8

import sys, os

from BitterBetty import BitterBetty

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
    # print(file_path)
    try:
        f= open(file_path, "r")
        content = f.readlines()
        # print(content)
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
        # print("Welcome to console inteaction !")
        poems = list_poems()
        print("Chose a poem to read:")
        for num, poem in zip(range(1, len(poems)+1), poems):
            print("{0}. {1} by {2}".format(num, poem['name'], poem['author']))
        user_choice = int(input("Number: "))
        # print(f"choice: {user_choice}")
        poem_path = "poems/" + poems[user_choice-1]['path']
        # print(f"poem path: {poem_path}")
        content = read_file(poem_path)
        try:
            betty = BitterBetty()
            for line in content:
                betty.speak(line)
        except FileNotFoundError as e:
            print(e)
            quit()
          

    def quit(self):
        quit()

class LoopInteraction:

    def __init__(self):
        self.consoleInteraction = ConsoleInteraction()

    def start(self):
        run = True
        while(run):
            try:
                self.consoleInteraction.start()
            except:
                print("An error as occured...")
                res = input("Would you like to continue ? (y/n)")
                if res is "n":
                    run = False
                


interactions = {
    "console": ConsoleInteraction,
    "loop" : LoopInteraction,
}

if __name__ == "__main__":
    inter = None
    try:
        inter = interactions[sys.argv[1]]()
    except:
        inter = interactions["loop"]()
    inter.start()
