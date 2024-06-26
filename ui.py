from tkinter import *
from tkinter import messagebox

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain_obj:QuizBrain):
        #defining the "quiz_brain_obj" like this will allow us to use its attributes
        # and methods in this module. See "start_q" method.

        self.text_for_question = ""
        self.quiz_brain_obj_1=quiz_brain_obj
        self.window=Tk()
        self.window.title("Jose Quiz")
        self.window.config(pady=20, padx=20,background=THEME_COLOR)

        # self.window.minsize(width=400,height=500) ## no need to define the window. We can directly start using
        ## "canvas" and use "grid"

        self.label_score = Label(text="Score: 0", fg="white", background=THEME_COLOR,
                                 font=("Arial",20,"italic"))
        self.label_score.grid(row=0, column=2)

        self.canvas= Canvas(width=300, height=250,background="white",)
        self.canvas.grid(row=2,column=1,columnspan=2,pady=30)
        self.question_text_in_cavas = self.canvas.create_text(150, 125,
                                                              text="",width=280,fill="black",font=("Arial", 12, "italic"))

        true_image=PhotoImage(file="images/true.png")
        self.true_button=Button(image=true_image,highlightthickness=0,command=self.true_button_log)
        self.true_button.grid(row=3, column=1)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,command=self.false_button_log)
        self.false_button.grid(row=3, column=2)

        self.start_q()

        self.window.mainloop()

    def start_q(self):
        if self.quiz_brain_obj_1.still_has_questions() == False:
            messagebox.showinfo("INFO", "ALL QUESTIONS ATTEMPTED! BYE")
            self.window.destroy()
            ##if there are no more questions. Show a message with OK button and close the window-- I came up with this :)
        else:
            self.text_for_question=self.quiz_brain_obj_1.show_question1()
            self.canvas.itemconfig(self.question_text_in_cavas,text=self.text_for_question)


    def change_color_and_next_question(self):
        self.canvas.config(bg=self.quiz_brain_obj_1.color) ##the color comes from quiz_brain module
        self.window.after(500,lambda:self.canvas.config(bg="White"))
        self.window.after(800,lambda :self.start_q())
        ##NOTE: need to put double the time for start_q, because "after()" function is non-blocking. So without the double time
        ## it schedules the canvas color change operation and then immediately calls self.start_q().

    def true_button_log(self):
        self.quiz_brain_obj_1.check_answer("True")
        self.change_color_and_next_question()
        self.label_score.config(text=f"Score: {self.quiz_brain_obj_1.score}")

    def false_button_log(self):
        self.quiz_brain_obj_1.check_answer("False")
        self.change_color_and_next_question()
        self.label_score.config(text=f"Score: {self.quiz_brain_obj_1.score}")



