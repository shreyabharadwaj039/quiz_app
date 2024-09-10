from logging import disable
from tkinter import *
from quiz_brain import Quiz
from pandas.io.sas.sas_constants import column_label_length_length

THEME="#375362"

class QuizInterface:
     def __init__(self,quiz_brain:Quiz):
         self.quiz=quiz_brain
         self.window= Tk()
         self.window.title("Quizzler")
         self.window.config(padx=20,pady=20,bg=THEME)


         self.label=Label(text="Score: 0",fg="white",bg=THEME)
         self.label.grid(row=0,column=1)


         self.canvas=Canvas(width=300,height=250,bg="white")
         self.question_text=self.canvas.create_text(150,125,width=280,text="some text",fill=THEME,font="Arial,20,italic")
         self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

         self.true=Button(text="CORRECT",command=self.true_press)
         self.true.grid(row=2,column=0)

         self.false = Button(text="WRONG",command=self.false_press)
         self.false.grid(row=2, column=1)

         self.get_next_question()
         self.window.mainloop()

     def get_next_question(self):
         self.canvas.config(bg="white")
         if self.quiz.question_left_to_answer():
             self.label.config(text=f"Score: {self.quiz.score}")
             q_text=self.quiz.next_question()
             self.canvas.itemconfig(self.question_text,text=q_text)
         else:
             self.canvas.itemconfig(self.question_text,text="End of the Quiz")
             self.true.config(state="disabled")
             self.false.config(state="disabled")



     def true_press(self):
         is_right=self.quiz.check("True")
         self.feedback(is_right)
     def false_press(self):
         is_wrong=self.quiz.check("False")
         self.feedback(is_wrong)

     def feedback(self,is_right):
         if is_right:
             self.canvas.config(bg="green")
         else:
             self.canvas.config(bg="red")
         self.window.after(1000,self.get_next_question)