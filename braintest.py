from Questions import Question

question_prompts = [
    "1. What colour are apples ?\n (a)Red/Green\n  (b) Purple\n\n ",
    "2. What colour are Bananas ?\n (a)Blue\n (b) Yellow\n\n",
    "3. What colour are Oranges ?\n (a)White\n (b) Yellow\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
]


def test_function(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score = score + 1
    print('You got ' + str(score) + '/' + str(len(questions)) + 'correct\n')
    if score>2:
        print('Excellent!!')
    print('='*50)



