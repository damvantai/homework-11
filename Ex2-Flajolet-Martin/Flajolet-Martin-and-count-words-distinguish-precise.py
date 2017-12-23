
# coding: utf-8

# In[1]:


"""
The hash functions used are:
1. CityHash
2. MurmurHash
3. SpookyHash
4. Java hashCode() method
"""


# In[2]:


from bitarray import bitarray
from cityhash import CityHash32
from spooky import hash32
import statistics
import jhashcode
import mmh3
import re
import math


# In[3]:


# hàm đếm số phần tư 0 ở đuôi 
def return_tail_length(s):
    s = str(s) # chuyển về dạng string 
    rev = s[::-1]
    
    count = 0
    for i in rev:
        if i is '0':
            count = count + 1
        else:
            break
    return count


# In[4]:


file_name_shakespeare = "pg100.txt"


# In[5]:


file_name_shakespeare


# In[6]:


word_distingush = set()


# In[7]:


hash_function_1_tail_length = []
hash_function_2_tail_length = []
hash_function_3_tail_length = []
hash_function_4_tail_length = []


# In[8]:


with open(file_name_shakespeare) as f:
    for line in f:
        line = line.replace('\n', '')
        line_list = line.split(' ')
        for word in line_list:
            temp = re.match('[a-zA-Z]+', word)
            if temp != None:
                word = temp.group()
                
                word_distingush.add(word)

                hash_value_1 = abs(CityHash32(word))
                hash_value_2 = abs(hash32(word))
                hash_value_3 = abs(jhashcode.hashcode(word))
                hash_value_4 = abs(mmh3.hash(word))

                # Binary representation
                binary_1 = format(hash_value_1, '032b')
                binary_2 = format(hash_value_2, '032b')
                binary_3 = format(hash_value_3, '032b')
                binary_4 = format(hash_value_4, '032b')

                # calculator tail length
                hash_function_1_tail_length.append(return_tail_length(binary_1))
                hash_function_2_tail_length.append(return_tail_length(binary_2))
                hash_function_3_tail_length.append(return_tail_length(binary_3))
                hash_function_4_tail_length.append(return_tail_length(binary_4))
            
f.close()


# In[9]:


# Lấy trung bình ước lượng của 4 hàm băm


# In[10]:


avg_hash = (2**(max(hash_function_1_tail_length)) + 2**(max(hash_function_2_tail_length)) + 2**(max(hash_function_3_tail_length)) + 2**(max(hash_function_4_tail_length))) / float(4)


# In[11]:


print("Số từ phân biệt theo ước lượng Flajolet-Martin là: ", avg_hash)


# In[12]:


print("Số từ phân biệt chính xác là: ", len(word_distingush))


# ## 
