import madlibs

print('''Please Select a madlib to do
1. Coding
2. The Sea
3. McDonald's
4. The Communist
5. Tom Brady
T. Tutorial
R. Random''')
ans = str(input('> ')[0].upper())

if ans == '1':
    madlibs.coding()
elif ans == '2':
    madlibs.the_sea()
elif ans == '3':
    madlibs.mcdonalds()
elif ans == '4':
    madlibs.the_communist()
elif ans == '5':
    madlibs.tom_brady()
elif ans == 'T':
    madlibs.tutorial()
elif ans == 'R':
    madlibs.random()
else:
    print('Incorrect input, please rerun.')
