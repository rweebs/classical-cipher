import re
import string
from collections import OrderedDict 
import helpers.lib as lib
def get_matrix(key):
    alphabet = string.ascii_uppercase
    cleaned_key = re.sub(r'[jJ^a-zA-Z]', '', key).upper()
    unique_char = ''.join(OrderedDict.fromkeys(cleaned_key))

    k=0
    matrix = [['' for i in range(5)] for j in range(5)]

    for i in range(5):
        for j in range(5):
            if((i*5)+j)<len(unique_char):
                matrix[i][j] = unique_char[i*5+j]
            else:
                if(alphabet[k] not in (item for sublist in matrix for item in sublist)):
                    matrix[i][j] = alphabet[k]
                    j+=1
                k+=1
    return matrix

def text_to_bigram_array(text):
    text=lib.remove_non_alphabet(text)
    replace_j_with_i = text.replace("J","I")

    if len(replace_j_with_i) ==0:
      return []

    repeated_text=[replace_j_with_i[0]]

    for x in replace_j_with_i[1:]:
      if x == repeated_text[-1]:
        repeated_text[-1]+=x
      else:
        repeated_text.append(x)

    bigram_text = ""
    for x in repeated_text:
        if(len(x)>1):
            bigram_text+='X'.join(x[i:i+1] for i in range(0, len(x)))
        else:
            bigram_text+=x
    if(len(bigram_text)%2==1):
        bigram_text+="X"
    bigram_array = [bigram_text[i:i+2] for i in range(0, len(bigram_text), 2)]

    print(bigram_array)
    return bigram_array

def get_matrix_position(char, matrix):
    for i in range(5):
        for j in range(5):
            if(matrix[i][j]==char):
                return [i, j]

def encrypt(text,key):
    matrix=get_matrix(key)
    bigram_array=text_to_bigram_array(text)
    encrypted_text=""

    for bigram in bigram_array:
        index_x = get_matrix_position(bigram[0], matrix)
        index_y = get_matrix_position(bigram[1], matrix)

        if(index_x[0]==index_y[0]):
            result= matrix[index_x[0]][(index_x[1]+1)%5]+matrix[index_y[0]][(index_y[1]+1)%5]
        elif(index_x[1]==index_y[1]):
            result= matrix[(index_x[0]+1)%5][index_x[1]]+matrix[(index_y[0]+1)%5][index_y[1]]
        else:
            result= matrix[index_x[0]][index_y[1]]+matrix[index_y[0]][index_x[1]]
        encrypted_text+=result

    return encrypted_text

def decrypt(text,key):
    matrix=get_matrix(key)
    bigram_array=[text[i:i+2] for i in range(0, len(text), 2)]
    decrypted_text=""
    
    for bigram in bigram_array:
        index_x = get_matrix_position(bigram[0], matrix)
        index_y = get_matrix_position(bigram[1], matrix)

        if(index_x[0]==index_y[0]):
            result= matrix[index_x[0]][(index_x[1]-1)%5]+matrix[index_y[0]][(index_y[1]-1)%5]
        elif(index_x[1]==index_y[1]):
            result= matrix[(index_x[0]-1)%5][index_x[1]]+matrix[(index_y[0]-1)%5][index_y[1]]
        else:
            result= matrix[index_x[0]][index_y[1]]+matrix[index_y[0]][index_x[1]]
        decrypted_text+=result
    return decrypted_text