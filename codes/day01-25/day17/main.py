from data import question_data
import question_model
import quiz_brain

question_bank = []
for i in (question_data):
    question_text = i['text']
    question_answer = i['answer']
    new_question = question_model.Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = quiz_brain.QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    
    
print(f"You've complete the quiz\nYour final score was: {quiz.score} / {len(question_data)}")
