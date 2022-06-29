spam = ['apples', 'bananas', 'tofu', 'cats']

st = ''




def change(tabl):
    for i, st in enumerate(tabl):
        if i == (len(tabl)-1):
            print('and '+st)
        else:
            print(st, end=',')


print(change(spam))

input('type enter')
