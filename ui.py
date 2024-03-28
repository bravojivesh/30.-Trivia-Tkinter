from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,text1):
        self.window=Tk()
        self.window.title("Jose Quiz")
        self.window.config(pady=20, padx=20,background=THEME_COLOR)
        # self.text1=""
        # self.window.minsize(width=400,height=500)

        self.label1 = Label(text="Score:", fg="white", background=THEME_COLOR,
                            font=("Arial",20,"italic"))
        self.label1.grid(row=0, column=2)

        self.canvas= Canvas(width=300, height=250,background="white",)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text=text1,
                                                     fill="black",
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=2,column=1,columnspan=2,pady=30)

        true_image=PhotoImage(file="images/true.png")
        self.true_button=Button(image=true_image,highlightthickness=0)
        self.true_button.grid(row=3, column=1)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=3, column=2)

        self.window.mainloop()

    def start_q(self):
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="@@@",
                                                     fill="black",
                                                     font=("Arial", 20, "italic"))







