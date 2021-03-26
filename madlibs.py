import random


def coding():
    print('Coding')
    print('Please give some inputs for the madlib')
    input('> ')
    adj = input('Adjective: ')
    noun = input('Noun: ')
    adj2 = input('Adjective: ')
    place = input('A place: ')
    adj3 = input('Adjective: ')
    adj4 = input('Adjective: ')
    noun2 = input('Noun: ')
    noun3 = input('Noun: ')
    print()
    print(f'''Coding is very {adj}, and it reminds me of {noun}. 
Coding can get tedious, but it's still very {adj2}.
Python is popular in {place}, I hope {adj3} Frank knows it.
C# is good for game design, my favorite game is {adj4} {noun2}.
My favorite IDE is Py{noun3}.''')


def the_sea():
    print('The Sea')
    print('Please give some inputs for the madlib')
    input('> ')
    adj = input('Adjective: ')
    noun = input('Noun: ')
    adj2 = input('Adjective: ')
    adj3 = input('Adjective: ')
    noun2 = input('Noun: ')
    noun3 = input('Noun: ')
    print()
    print(f'''The sea is {adj} and very {adj2}. It has cool shells
and {noun}s. If you are near a sea you are near a beach 
and a {adj3} {noun2}. {noun3}s can be found in the sea, but
not on the land of course.''')


def mcdonalds():
    print("McDonald's")
    print('Please give some inputs for the madlib')
    input('> ')
    adj = input('Adjective: ')
    adj2 = input('Adjective: ')
    adj3 = input('Adjective: ')
    adj4 = input('Adjective: ')
    adj5 = input('Adjective: ')
    adj6 = input('Adjective: ')
    noun = input('Noun: ')
    noun2 = input('Noun: ')
    print()
    print(f'''McDonald's is {adj} and {adj2}. There rival is
the {adj3} burger king, the {noun} kisser. Big Ronald once fought
the BK, but {adj4} Wendy stopped them before it got too bad.
McDonald's burgers are {adj5} and so yummy. My favorite
burger is the {adj6} {noun2} burger.''')


def the_communist():
    print("The Communist")
    print('Please give some inputs for the madlib')
    input('> ')
    adj = input('Adjective: ')
    adj2 = input('Adjective: ')
    adj3 = input('Adjective: ')
    adj4 = input('Adjective: ')
    adj5 = input('Adjective: ')
    noun = input('Noun: ')
    noun2 = input('Noun: ')
    noun3 = input('Noun: ')
    noun4 = input('Noun: ')
    print()
    print(f'''The {adj} communist was waiting for his {adj2} {noun}
and his potato rations. Yesterday he was feeling very {adj3}.
The reason for that is because he fought {adj4} Jim, he capitalist
{noun2}. The worst thing about capitalism is the rich {noun3}s and
the {adj5} {noun4}''')


def tom_brady():
    print("Tom Brady")
    print('Please give some inputs for the madlib')
    input('> ')
    adj = input('Adjective: ')
    adj2 = input('Adjective: ')
    adj3 = input('Adjective: ')
    noun = input('Noun: ')
    noun2 = input('Noun: ')
    noun3 = input('Noun: ')
    verb = input('Verb: ')
    verb2 = input('Verb: ')
    print()
    print(f'''Tom Brady is a very {adj} and famous football player.
He uses {noun}s to {verb} but he still {verb2}s. He has a {noun2}
that he bought when he beat the Super{adj2}. He once stated that
he enjoys a good {adj3} {noun3}, not many agreed. Tom likes to watch''')


def tutorial():
    print('When you see a [ > ] press [ ENTER ] to continue')
    input('> ')
    print('An adjective is a descriptor/a word that describes something.')
    print('i.e. fat, stinky, sticky, spicy, happy')
    input('> ')
    print('A noun is a person, place, or thing.')
    print('i.e. roller skate, plate, Florida, Jimmy')
    input('> ')
    print('A verb is an action word, an action.')
    print('i.e. run, jump, hide, hit, read')
    print('> ')


def random():
    ans = random.randint(1, 5)
    if ans == '1':
        coding()
    elif ans == '2':
        the_sea()
    elif ans == '3':
        mcdonalds()
    elif ans == '4':
        the_communist()
    elif ans == '5':
        tom_brady()
    else:
        print('Random failed, sorry, please rerun.')
