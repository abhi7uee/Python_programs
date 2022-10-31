#Method 1
def runLengthEncoding(string):
    encoded_string =""
    count = 0
    for index in range(0,len(string)-1):
        if (string[index] == string[index+1]):
            count +=1
            if count == 9:
                encoded_string = append_encoded_letter(encoded_string, count, string)
            count = 0 #initialize count = 0 and start from the next index
            index +=1
            encoded_string = append_encoded_letter(encoded_string, count, string)


                
        elif (string[index] == string[index+1]) and count != 0 :
            encoded_string = encoded_string + str(count) + (string[index]) #append to string and start over
            count = 0 #initialize count = 0 and start from the next index
            index +=1
    return encoded_string
            
def append_encoded_letter(encoded_string, count, string):
    encoded_string = encoded_string + str(count) + (string[index]) #append to string and start over

string = "AAAAAAAAAAAAABBCCCCDD"
print(string)
output_string = runLengthEncoding(string)
print(output_string)
