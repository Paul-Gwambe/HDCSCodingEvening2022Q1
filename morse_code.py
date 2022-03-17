#!/usr/bin/env python
# coding: utf-8

# In[2]:


form  =  int(input('Please select an option by entering the menu number: \n 1 Encrypt to Morse Code \n 2. Decrypt from Morse Code \n 0. Exit'))

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

if form == 1:
    text = input('Input text to encrypt:')
    #method for encrpting

    def encrpyt_mess(mes):
        char = ""
        for i in mes:
            if i != ' ':
                morse = MORSE_CODE_DICT[i]
                char += morse 
            else:
                char += "/"
                
        print(char)
    encrpyt_mess(text.upper())
    
elif form == 2:
    text = input('Input Morse Code to decrpyt:')
    # Decoding method

    def decode_text(code):
        char = ""
        mes = ""
        for i in code:
            if i != ' ':
                char += i
            else:
                for key in MORSE_CODE_DICT:
                    value = MORSE_CODE_DICT[key]
                    if value == char:
                        mes += key
                if char == "/":
                    mes += " "
                char = ""
        print(mes)
    decode_text(text)
    #decode_text(".-..-. .... . .-.. .--. / -- . / -.-.-- .-..-.")
else:
    print('Exiting, goodbye!')


# In[ ]:





# In[ ]:




