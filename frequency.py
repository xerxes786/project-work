test_word = input('enter the word! ')
frequency = {}

for i in test_word:
    if i in frequency:
        frequency[i] = frequency[i] + 1
        

    else:
        frequency[i] = 1
        print('count of letter', i, 'is: \n' + str(frequency))
            