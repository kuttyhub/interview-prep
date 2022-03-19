def comprase_string(string):
    current_char = ""
    count =0
    result =""
    
    for i in string:
        if current_char != i:
            #add to result
            if current_char != "":
                result += current_char+str(count)
            #update it
            current_char = i
            count = 1
        else:
            count+=1

    #added last unique character count 
    if current_char != "":
        result += current_char +str(count)

    return result

string = "aabcccccaaa"
print(comprase_string(string))