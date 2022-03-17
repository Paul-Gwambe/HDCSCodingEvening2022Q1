#!/usr/bin/env python
# coding: utf-8

# In[7]:


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


# In[8]:


#method for encrpting

def encrpyt_mess(mes):
    char = ""
    for i in mes:
        if i != ' ':
            morse = MORSE_CODE_DICT[i]
            char += morse + ' '
        else:
            print('space')
    print(char)


# In[9]:


encrpyt_mess('SOS')


# In[12]:


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
            char = ""
    print(mes)
        
decode_text(".-..-. .... . .-.. .--. / -- . / -.-.-- .-..-.")


# In[ ]:




