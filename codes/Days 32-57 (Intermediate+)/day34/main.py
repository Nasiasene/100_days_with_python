from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import ui

'''
Hint: i can define a datatype for an variable, so its gonna be immutable.
      as well, i can also declare what type of variable will return from a function

ex: age: int
    name: str

    def function(height: float) -> bool:
        (...)
        return True
'''


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = ui.QuizInterFace(quiz)

#while quiz.still_has_questions():
#   quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")