from Day17question_model import Question
from Day17data import question_data, logo
from Day17quiz_brain import QuizBrain

question_bank = []
for quest in range(0,len(question_data)-1):
    question = question_data[quest]['question']
    answer = question_data[quest]['correct_answer']
    x = Question(question, answer)
    question_bank.append(x)

print("Welcome to trivia!")
print(logo, "\n")
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f'You\'ve completed the quiz!\nYour final score was {quiz.score}/{quiz.question_number}')