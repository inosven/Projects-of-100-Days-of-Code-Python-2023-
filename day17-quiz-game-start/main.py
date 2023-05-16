from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question_datum in question_data:
    question_bank.append(Question(question_datum["question"], question_datum["correct_answer"]))

# print(question_bank[0].text)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()


print("You've complete the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")