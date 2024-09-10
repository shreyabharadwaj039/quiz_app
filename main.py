import data_fechter as df
from quiz_model import *
from quiz_brain import *
from ui import QuizInterface
# Building question bank
question_bank = []
for question in df.question_data:
    text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(q_text=text, q_answer=answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)
quiz_ui=QuizInterface(quiz)

# while quiz.question_left_to_answer():
#     quiz.next_question()

print(f"your score is {quiz.self.score}/10") 