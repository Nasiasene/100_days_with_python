class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number != len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q{self.question_number}: {question.text} (True/False): ").lower()
        self.check_answer(guess, question.answer)
        print("\n")

    def check_answer(self, user_guess, answer):
        while True:
            if user_guess != 'true' and user_guess != 'false':
                user_guess = input("Input a valid answer: ").lower()
                continue
            else:
                break
        
        if answer.lower() == user_guess:
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
            
        print(f"Your current score: {self.score} / {self.question_number}")