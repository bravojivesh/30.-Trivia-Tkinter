import question_model
import data
import quiz_brain
import ui


question_bank = []
for question in data.question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = question_model.Question(question_text, question_answer)
    #this will store variables "question_text" and "question_answer"
    # as "Question.text" and "Question.answer". These are callable attributes of Question object.
    # I have printed it-- see a few lines below.

    question_bank.append(new_question)
    #note: new_question is "an object". Therefore question_bank is a "list of objects.". So, when it will
    ## use "show_question" method (scroll below), each object will be using ".text" attribute behind the scenes.
    # db: print (question_bank,new_question.text)

quiz = quiz_brain.QuizBrain(question_bank)
#preparing the "quiz" object. See "quiz_brain" module for its attributes.

window1=ui.QuizInterface(quiz)
#feeding quiz object to the QuizInterface class.
#because of the mainloop inside the "QuizInterface" class, we can not have another while in this code.



#==============================================================================
# while quiz.still_has_questions():
#     quiz.show_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
#==============================================================================