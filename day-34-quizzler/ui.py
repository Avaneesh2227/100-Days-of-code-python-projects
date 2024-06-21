from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.canvas=Canvas(height=250,width=300,bg='white')
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.question=self.canvas.create_text(150,125,text="Quiz",font=("Arial",20,"italic"),width=280)

        self.tick_img=PhotoImage(file="images/true.png")
        self.cross_img = PhotoImage(file="images/false.png")
        self.tick=Button(image=self.tick_img,highlightthickness=0,command=self.true_pressed)
        self.cross = Button(image=self.cross_img,highlightthickness=0,command=self.false_pressed)
        self.tick.grid(row=2,column=0)
        self.cross.grid(row=2, column=1)

        self.score=Label(text=f"Score: 0",bg=THEME_COLOR,fg='white')
        self.score.grid(row=0,column=1)

        self.get_next_question()



        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            question= self.quiz.next_question()
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question, text=question)
        else:
            self.canvas.itemconfig(self.question,text="Youve reached the end!")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))


    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)


