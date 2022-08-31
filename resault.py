res = {}
q1, q2, q3, q4, q5, q6, q7, q8, q9, q10 = [],[],[],[],[],[],[],[],[],[]
def resault():
    #
    with open('bd_file.txt') as r:
        for line in r:
            line = line.split('*')
            if len(line) == 3:
                user = line[0][1:]
                q = line[1]
                answer = line[2][0:-2]
                if user in res:
                    res[user][q] = answer
                else:
                    res[user] = {}
                    res[user][q] = answer
    for us in res.keys():
        try:
            q1.append(res[us]['1'])
            q2.append(res[us]['2'])
            q3.append(res[us]['3'])
            q4.append(res[us]['4'])
            q5.append(res[us]['5'])
            q6.append(res[us]['6'])
            q7.append(res[us]['7'])
            q8.append(res[us]['8'])
            q9.append(res[us]['9'])
            q10.append(res[us]['10'])
        except:
            pass
        

    
    with open('dict_resault.py', 'w') as dr:
        dr.write('ddd=')
        dr.write(str(res))
        dr.write('\n')
        dr.write('q1=')
        dr.write(str(q1))
        dr.write('\n')
        dr.write('q2=')
        dr.write(str(q2))
        dr.write('\n')
        dr.write('q3=')
        dr.write(str(q3))
        dr.write('\n')
        dr.write('q4=')
        dr.write(str(q4))
        dr.write('\n')
        dr.write('q5=')
        dr.write(str(q5))
        dr.write('\n')
        dr.write('q6=')
        dr.write(str(q6))
        dr.write('\n')
        dr.write('q7=')
        dr.write(str(q7))
        dr.write('\n')
        dr.write('q8=')
        dr.write(str(q8))
        dr.write('\n')
        dr.write('q9=')
        dr.write(str(q9))
        dr.write('\n')
        dr.write('q10=')
        dr.write(str(q10))
        dr.write('\n')
        dr.write('( ')
        dr.write('1.Страна проживания   ')
        count = f'Всего: {len(q1)}'
        dr.write(str(count))
        dr.write('  (')
        dr.write(str(q1))
        dr.write(')) ')
        dr.write('\n')



def view(mass, questions, var):
    count = len(mass)
    answer_ = []
    er = f'Всего: {count}'
    for i in var:
        count_i = mass.count(i)
        print(mass, i)
        per = count_i / count * 100
        d = (i,count_i, per)
        answer_.append(d)
    with open('dict_resault.py', 'a') as dr:
        dr.write('( ')
        dr.write(str(questions))
        dr.write('  ')
        dr.write(str(er))
        dr.write('  ')
        dr.write(str(answer_))
        dr.write(') ')
        dr.write('\n')
        
def view9(mass, questions, var):
    count = len(mass)
    answer_ = []
    answer9 = []
    er = f'Всего: {count}'
    for i in var:
        count_i = mass.count(i)
        print(mass, i)
        per = count_i / count * 100
        d = (i,count_i, per)
        answer_.append(d)
    for m in mass:
        if m not in var:
            answer9.append(m)
    with open('dict_resault.py', 'a') as dr:
        dr.write('( ')
        dr.write(str(questions))
        dr.write('  ')
        dr.write(str(er))
        dr.write('  ')
        dr.write(str(answer_))
        dr.write(') ')
        dr.write('\n')
        dr.write('( ')
        dr.write('9.Другие ответы:   [')
        dr.write(str(answer9))
        dr.write(']) ')
        dr.write('\n')
    

        

ninth1 = 'быстрые способы справиться с гневом'
ninth2 = 'техники релаксации с визуальным/аудио/видео сопровождением'
ninth3 = 'техники профилактики гнева'
ninth4 = 'возможность отслеживать свой прогресс и статистику'
ninth5 = 'свой вариант'
ninth = [ninth1, ninth2, ninth3, ninth4, ninth5]

resault()
view(q2, '2.Пол', ['M', 'Ж'] )
view(q3, '3.Возраст', ['21-30', '31-45', 'Старше 45'] )
view(q4, '4.Образование:', ['Высшее', 'Среднее специальное', 'Среднее', 'Другое'])
view(q5, '5.Как вы оцениваете уровень вашего взаимодействия с мобильными приложениями', ['1', '2','3','4','5','6','7','8','9','10'])
view(q6, '6.Какой мобильной операционной системой вы пользуетесь сейчас?', ['Android', 'iOS'])
view(q7, '7.Нужно ли вам время от времени такое приложение?', ['1.', '2.', '3.', '4.', '5.'])
with open('dict_resault.py', 'a') as dr8:
    dr8.write('( 8.Как бы вы поняли, что вам нужно скачать такое приложение?   ')
    count = f'Всего: {len(q8)}'
    dr8.write(str(count))
    dr8.write('  (')
    dr8.write(str(q8))
    dr8.write('))')
    dr8.write('\n')
view9(q9, '9.Что бы вы хотели видеть в таком приложении?', ninth)
view(q10, '10.Готовы ли вы оформить подписку на такое мобильное приложение', ['no_0', 'yes_10', 'yes_30'])
