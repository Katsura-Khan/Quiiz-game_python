class QuizBrain:
    def __init__(self,questions_list):
        self.questions_list = questions_list
        self.score = 0
        self.questions_number = 0
    
    def stil_has_questions(self):
        return self.questions_number < len(self.questions_list)
        
    
    
    def next_quesitons(self):
        correct_answer = self.questions_list[self.questions_number]
        self.questions_number += 1
        user_answer = input(f"Q{self.questions_number}{correct_answer.answer} Write True/False")
        self.check_answer(user_answer, correct_answer.text)
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('You right')
        else:
            print('That wrong ') 
            print(f"Correct answer is {correct_answer} You score is {self.score}")
        
        