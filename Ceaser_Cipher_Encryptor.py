def caesarCipherEncryptor(string, key):
    '''
    This function returns an output string in which each character 
    of the input string is shifted by key times.
    '''
    #Unicode of a = 97
    #Unicode of z = 122
    new_array = []
    key = key%26
    for letter in string:
        new_letter = find_shifted_letter(letter, key)
        new_array.append(new_letter)
    output_string = ','.join(new_array)
    return output_string
def find_shifted_letter(letter, key):
    nLC = ord(letter) + key
    if nLC <= 122:
        return chr(nLC)
    else:
        return chr(96 + nLC%122)
        
string = "xyz"
key = 2
output_string = caesarCipherEncryptor(string, key)
print(output_string)


string = "xyz"
for char in string:
    #print(char)
    print(ord(char) )
    char = chr( (ord(char)) + 2 )
    print(char)
print(string)
