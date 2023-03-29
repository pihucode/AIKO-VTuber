import tkinter as tk
import threading


class SubtitleApp(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.text = None
        self.text_initialized_event = threading.Event()

    def run(self):
        self.root = tk.Tk()
        self.root.title('AIKO Subtitles')
        self.root.configure(background='black')
        self.root.minsize(200, 100)
        self.root.maxsize(600, 800)

        self.text = tk.StringVar()
        self.text.set('Initializing AIKO v1.0 ...')
        self.text_initialized_event.set()

        label = tk.Label(self.root, textvariable=self.text, wraplength=480, font=(
            'Source Code pro', 14), fg='white', bg='black')
        label.pack()

        self.root.mainloop()

    def set_text(self, new_text):
        if not self.text_initialized_event.wait(timeout=1):
            raise RuntimeError("Timed out waiting for text initialization")
        self.text.set(new_text)


# app = SubtitleApp()
# app.start()
# placeholder = "Well, I'm an AI, so I don't exactly have likes and dislikes in the traditional sense. However, I do enjoy engaging with users and helping them find answers to their questions. And when I'm not doing that, you can usually find me crushing my opponents in a competitive video game or binge watching the latest anime series."
# app.set_text(placeholder)
