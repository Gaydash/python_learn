
question_answer = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}

def ask_user():
    while True:
        user_say = input('Спроси меня что нибудь: ')
        if user_say == 'Хорошо':
            print('Good bay')
            break
        elif question_answer.get(user_say) != None:
            print(question_answer[user_say])
        else:
            print('Не говори ерунду')
            break

ask_user()

