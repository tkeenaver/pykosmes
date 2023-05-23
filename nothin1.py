while True:
    try:
        i1=int(input('number:'))
    except ValueError:
        print('input NUMBER, please!!!')
    else:
        break

i2=i1**3
print('answer: ',i2)
