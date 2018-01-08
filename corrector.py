from difflib import SequenceMatcher
from nltk.corpus import stopwords
import string
import pandas as pd




def similar(a, b):
    message1 = [x for x in a if x not in string.punctuation]
    clean_message1 = ''.join(message1)

    m1 = [q for q in clean_message1.split() if q not in stopwords.words('english')]

    message2 = [y for y in b if y not in string.punctuation]
    clean_message2 = ''.join(message2)

    m2 = [z for z in clean_message2.split() if z not in stopwords.words('english')]

    # return m1

    return SequenceMatcher(None, ''.join(m1), ''.join(m2)).ratio()



def get_student_solutions(df, student, question):
    l = []
    for i in df[-1:]:
        l.append(df[i][student])
    if question == "all":
        return(l)
    else:
        return(l[question])



def cla(student_ans, answerkey_ans):
    # CLA = Checks long answer
    # Checks long answer similarity between student and possible answer list
    # and produces a score on similarity

    key = answerkey_ans.split(' % ')
    best_score = 0
    for ans in key:
        sim = similar(student_ans, ans)
        if sim > best_score:
            best_score = sim
#     if best_score < 0.5:
#         best_score = 0

    return best_score



df2 = pd.read_csv('sample elem test 222.csv')



# ak1 = get_student_solutions(df2, 0, 'all')
# ak2 = get_student_solutions(df2, 2, 'all')

# ak3 = ak1.extend(ak2)

def grader(dataframe, answerkey,  student):
    scores = []
    total = 0
    print('Thinking...')
    for q in range(2, len(dataframe.columns)-1):

        # print(str(q) + ')')
        # print(get_student_solutions(df2, 0, q))
        # print(get_student_solutions(df2, 1, q))
        score = cla(get_student_solutions(df2, student, q), get_student_solutions(df2, answerkey, q))
        # print(score)
        scores.append(score)

        total = sum(scores)

    grade = 100*total/len(df2.columns)

    print('Grade: ')
    print(grade)



for student in range(0, 4):
    grader(df2, 0, student)
