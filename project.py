# Quiz Game
print("Wellcome to quiz game !!")
print('NOTE: if your spelling is incorrect then it is considered as wrong answer')

question = {"In school, Albert Einstein failed most of the subjects, except for physics and math.": "True",
            "The first song ever sung in the space was Happy Birthday.": "True",
            " A male canary tends to have a better singing voice than a female canary.": "True",
            "Tea contains more caffeine than coffee and soda": "False",
            "Dogs have an appendix.": "False",
            "Bill Gates is the founder of Amazon.": "False",
            "Mice have more bones than humans.": "True",
            "The first product with a bar code was chewing gum": "True",
            "The Beatles is a famous rock band from Manchester, the United Kingdom": "True",
            "The star is the most common symbol used in all national flags around the world.": "True"}  # Pool of questions
import random

questionlist = []
while (len(questionlist) != 5):  # list of 5 questions
    i = random.choice(list(question.keys()))  # Choose Random question from question pool and make a list of it
    if (i not in questionlist):
        questionlist.append(i)  # make a list of random qustions
score = 0
print("""                
88888888     888    88     88    8888888
88         88   88  88 8 8 88    88   
88  8888  88  8  88 88  8  88    8888888
88  8 88  88     88 88  8  88    88     
88888888  88     88 88  8  88    8888888

                                                   """)
for i in questionlist:
    print("\n" + i)
    a = input("\nEnter True or False: ")
    if (a == question[i]):
        print("\nRight answer! +5 points")
        score += 5
    else:
        print("\nWrong answer!")
print("\nTotal Score is :", score)