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
        self.poems = list_poems()
        pass

    def _user_choose_(self):
        is_valid = False
        while(not is_valid):
            print("Chose a poem to read:")
            for num, poem in zip(range(1, len(self.poems)+1), self.poems):
                print("{0}. {1} by {2}".format(num, poem['name'], poem['author']))
            try:
                user_choice = int(input("Number: "))
                if user_choice > len(self.poems) or user_choice < 1:
                    raise ValueError
                is_valid = True
            except:
                continue
        # print(f"choice: {user_choice}")
        return user_choice

    def _read_selected_(self, user_choice):
        poem_path = "poems/" + self.poems[user_choice-1]['path']
        content = read_file(poem_path)
        betty = BitterBetty()
        for line in content:
            betty.speak(line)

    def start(self):
        user_choice = self._user_choose_()
        try:
            self._read_selected_(user_choice)
        except FileNotFoundError as e:
            print(e)
            quit()
          

    def quit(self):
        quit()

class LoopInteraction:

    def __init__(self, user_choice = 2):
        self.consoleInteraction = ConsoleInteraction()
        self.user_choice = user_choice

    def start(self):
        run = True
        while(run):
            try:
                print("Betty start to read...")
                self.consoleInteraction._read_selected_(self.user_choice)
            except FileNotFoundError as fnfe:
                print(fnfe)
                run = False
            except Exception as e:
                print("An error as occured...")
                print(e)
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
        if sys.argv[2]:
            inter = interactions[sys.argv[1]](sys.argv[2])
        inter = interactions[sys.argv[1]]()
    except:
        inter = interactions["loop"]()
    inter.start()
