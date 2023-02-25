



def calc_average():
    Score1=int(input('Enter score 1: '))
    Score2=int(input('Enter score 2: '))
    Score3=int(input('Enter score 3: '))
    Score4=int(input('Enter score 4: '))
    Score5=int(input('Enter score 5: '))
    avg=Score1+Score2+Score3+Score4+Score5/5
    print()
    print("Score		Numeric Grade	   Letter Grade")
    print("----------------------------------------------------")
    print('Score 1: ', f'{Score1:>8}', f'{determine_grade(Score1):>17}')
    print('Score 2: ', f'{Score2:>8}', f'{determine_grade(Score2):>17}')
    print('Score 3: ', f'{Score3:>8}', f'{determine_grade(Score3):>17}')
    print('Score 4: ', f'{Score4:>8}', f'{determine_grade(Score4):>17}')
    print('Score 5: ', f'{Score5:>8}', f'{determine_grade(Score5):>17}')
    print('Average Score: ', avg)

    



    

def determine_grade(number_grade):
    if number_grade<0 or number_grade>100:
        return('Invalid grade!')
    elif number_grade>=90:
        return('A')
    elif number_grade>=80:
        return('B')
    elif number_grade>=70:
        return('C')
    elif number_grade>=60:
        return('D')
    else:
        return('F')

 

    


calc_average()



