from Questions import Questions
from data import questions_list
from QuizBrain import QuizBrain


questions_blnak = []
 
for questions in questions_list:
    questions_text = questions["question"]
    questions_answer = questions["correct_answer"]
    new_questions = Questions(questions_text,questions_answer)
    questions_blnak.append(new_questions)
    
quiz = QuizBrain(questions_blnak)

while quiz.stil_has_questions:
    quiz.next_quesitons()

print('Quiz end Your score is {quiz.score}')
    
    
    
    
    
    
    
    
    
    
    
    