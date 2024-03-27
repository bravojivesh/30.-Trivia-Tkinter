import html
class Question:

    def __init__(self, q_text, q_answer):
        self.text = html.unescape(q_text) #ang did it in quiz_brain, but I am doing it here.
        self.answer = q_answer
