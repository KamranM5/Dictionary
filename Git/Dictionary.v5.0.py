import random
from time import sleep
from colorama import init, Fore, Back
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[2].id)
init(autoreset=True)

words = {}
with open('Text.txt', 'r', encoding='utf-8') as file:  # open file
    for line in file:  # go through the lines of the file
        # splitting the string into arts (keys and values)
        key, *value = line.split()
        for i in range(0, len(line)):
            if line[i] == "=":
                i = i - 1
                key = line[:i]  # correct len of key
                i = i + 3
                value = line[i:-1:]  # correct len of value
                words[key] = value

print(Fore.YELLOW + "Maximum word count: " + str(len(words)))

count2 = int(input("Word count: "))

answer = input("Do you want to voice the results ( Yes / No )? ")

count = 0  # number of words entered

correct_answers = 0  # number of correct answers

mistakes = 0  # number of mistakes

backup = []  # list where words will be stored for verification

backup2 = []  # list where words will be stored to add to the file

for key, value in words.items():
    while count < count2:
        # words_translation = words in English
        words_translation = random.choice(list(words.keys()))

        # checking if a value( word in English ) is in the backup list
        if words_translation not in backup:
            # words_key = words in Russian
            words_key = words[words_translation]

            q = input(words_key.capitalize() + "\n" + "Translation:____")

            if q == words_translation or q == words_translation.capitalize():
                backup.append(words_translation)

                words_translation = words_translation + ' ' * 100

                words_translation = list(words_translation)

                words_translation[50:1] = ' ' * 5 + "! ! ! Well ! ! !"

                words_translation = ''.join(words_translation)

                backup2.append(words_translation)

                print(Back.GREEN + Fore.WHITE + " Well ")

                correct_answers += 1
                count += 1

                print(Fore.GREEN + " " * 10 + str(count) + "/" + str(count2))

            elif q != words_translation or q == words_translation.capitalize():
                backup.append(words_translation)

                words_translation = words_translation + ' ' * 100

                words_translation = list(words_translation)

                words_translation[50:1] = ' ' * 5 + "! ! ! Mistake ! ! !"

                words_translation = ''.join(words_translation)

                backup2.append(words_translation)

                print(Fore.RED + " Mistake! ")
                print(Back.YELLOW + Fore.BLACK + "Correct answer:")
                print(Back.GREEN + Fore.WHITE + " " + str(words_translation) +
                      " ")

                mistakes += 1
                count += 1

                print(Fore.GREEN + " " * 10 + str(count) + "/" + str(count2))
        elif words_translation in backup:
            continue

    backup_file = open('Text2.txt', 'w', encoding='utf-8')  # open file
    for i in range(0, count2):
        # write words to backup_file
        backup_file.write(backup2[i] + "\n")

    result = round(((correct_answers / count2) * 100), 2)

    print(Back.BLUE + Fore.BLACK + " " * 5 + "THE END!!!" + " " * 5)
    print("Correct answers: " + Fore.GREEN + str(correct_answers))
    print("Mistakes: " + Fore.RED + str(mistakes))

    if result >= 80:
        print("Efficiency: " + Fore.GREEN + str(result) + "%")

    if 60 <= result < 80:
        print("Efficiency: " + Fore.YELLOW + str(result) + "%")

    if result < 60:
        print("Efficiency: " + Fore.RED + str(result) + "%")

    # voice output of results
    if answer == "Yes":
        engine.say("Correct answers")
        sleep(0.1)

        engine.say(str(correct_answers))
        sleep(0.1)

        engine.say("Mistakes")
        sleep(0.2)

        engine.say(str(mistakes))
        sleep(0.1)

        engine.say("Efficiency ")
        sleep(0.3)

        engine.say(str(result) + "%")

        engine.runAndWait()
        sleep(1.5)
        break

    if answer != "Yes":
        sleep(1.5)
        break
