from Tkinter import Tk, Label, Button
import random
import time


class TypingGame:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.countdown(65))
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def countdown(self, t):
        while t:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat)
            time.sleep(1)
            t -= 1

    def grab_words(self):
        print("Reading words_alpha.txt...")

        f = open('words_alpha.txt', "r")
        lines = f.readlines()
        f.close()

        return lines

    def preset_words(self, w_list):
        print("Choosing words...")

        c_words = list()

        for i in range(50):
            c_words.append(w_list[random.randint(1, len(w_list) + 1)])

        return c_words

    def run_game(self):
        print("Started...")

        word_list = self.grab_words()
        chosen_words = self.preset_words(word_list)

        print(chosen_words)


root = Tk()
gui = TypingGame(root)
root.mainloop()
