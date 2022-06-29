spam = ['apples', 'bananas', 'tofu', 'cats']

st=''

def change(tabl):
    global st
    i = 0
    while i < (len(tabl)-1):
        st += tabl[i] + ','
        i += 1
        if i == (len(tabl)-1):
            st += 'and ' + tabl[i]


    return st


print(change(spam))
input('press enter')
