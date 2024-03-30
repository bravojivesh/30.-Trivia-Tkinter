class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.color=""
        self.question_list = q_list
        #in main this will be a "list of objects"
        self.current_question = None

    def still_has_questions(self):
        # this method just compares the length. Nothing about OOP.
        return self.question_number < len(self.question_list)

    # ==============================================================================#==============================================================================
    # def show_question(self):
    #     #this method is specific to working on objects of "Question_model"'s "Question" class.
    #
    #     self.current_question = self.question_list[self.question_number]
    #     #this is pure OOP. current_question is "an object in the list", as question_list is a "list of objects".
    #     self.question_number += 1
    #
    #     user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
    #     ##jh: the part "current.text" does not make sense here in this module. But in "main" it will make sense.
    #     ## as current_question is an object of "Question" class of "Question_model" module. And it has an attribute called ".text"
    #
    #     self.check_answer(user_answer)
    # ==============================================================================#==============================================================================
    def show_question1(self):
        self.current_question = self.question_list[self.question_number]
        #stores an "object" of the "question_bank", which is a "list of objects".
        self.question_number += 1

        result_to_return= f"Q. {self.question_number}. {self.current_question.text} True/False"
        return result_to_return

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.color="Green"
            self.score += 1
            print("You got it right!")
        else:
            self.color="Red"
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
