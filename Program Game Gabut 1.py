#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random

angka_rahasia = random.randint(1, 100)


print("PROGRAM GAME GABUT TEBAK ANGKA")

print('=' * 40)
print('Kami telah memiliki angka, silahkan tebak!')
print('=' * 40)

while True:
    jawaban = int(input('\nMasukkan angka: '))
    
    if jawaban == angka_rahasia:
        print('Selamat, tebakanmu benar!')
        break
    else:
        print(
            'Tebakanmu terlalu', 'kecil'
        if jawaban < angka_rahasia
        else 'besar')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




