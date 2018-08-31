#https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers used for responses

#Easter Egg (Made by me)
# -o---o- ---o--- --ooo-- -ooooo- --ooo--
# -oo-oo- --o-o-- -o---o- ---o--- -o---o-
# -o-o-o- -o---o- -o----- ---o--- -o-----
# -o-o-o- -ooooo- -o-ooo- ---o--- -o-----
# -o---o- -o---o- -o---o- ---o--- -o-----
# -o---o- -o---o- -o---o- ---o--- -o---o-
# -o---o- -o---o- --oooo- -ooooo- --ooo--

# --ooo-- ------- -oooo-- ---o--- -o----- -o-----
# -o---o- ------- -o---o- --o-o-- -o----- -o-----
# -o---o- ------- -o---o- -o---o- -o----- -o-----
# --ooo-- -ooooo- -oooo-- -ooooo- -o----- -o-----
# -o---o- ------- -o---o- -o---o- -o----- -o-----
# -o---o- ------- -o---o- -o---o- -o----- -o-----
# --ooo-- ------- -oooo-- -o---o- -ooooo- -ooooo-

import random
import time

replies = ["It is certain.","It is decidedly so.","Without a doubt.",
    "Yes - definitely.","You may rely on it.","As I see it, yes.",
    "Most likely.","Outlook good.","Yes.","Signs point to yes.",
    "As I see it, yes.","Most likely.","Outlook good.","Yes.",
    "Signs point to yes.","Reply hazy, try again.","Ask again later.",
    "Better not tell you now.","Cannot predict now.",
    "Concentrate and ask again.","Don't count on it.","My reply is no.",
    "My sources say no.","Outlook not so good.","Very doubtful."]

def ball():
    print("What is your question? ~~It specializes in answering 'Yes/No' questions~~")
    input("")
    print("The ball is shaking.")
    for x in range(3):
        time.sleep(1)
        print("...")
    print(replies[random.randint(0,20)])
    end()

def end():
    time.sleep(1.5)
    print("Do you have more questions for it to answer?")
    cont = input("")
    if cont == "Yes" or cont == "YES" or cont == "yes" or cont == "y" or cont == "Y":
        print("Go for it.")
        ball()
    elif cont == "No" or cont == "NO" or cont == "no" or cont == "n" or cont == "N":
        print("It hopes to see you again.")
    else:
        print("It did not understand that. Try again.")
        end()
        
ball()

