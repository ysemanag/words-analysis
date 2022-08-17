#CPSC 115L Project 1 - Python WordsAnalysis
#Focus on Strings and Lists and i/o
#Due 10-14-2020 11:59 pm
#Author: Yves Semana Gisubizo(2024)


#accessing the files

infile= open("crosswords.txt","r") #open() is an inbuilt function to open  infile file and "r" means only reading 
words_list=[]

def isPalindrome(w):
    reverse_w=''
    length=len(w)
    while length>0:
        reverse_w=reverse_w + w[length-1]
        length=length-1
    if reverse_w==w:
        return True            
    else:
        return False

#printing the words one by one
pal=0
short_len=0
short_pal=''
long_len=0
long_pal=''
no_e_count=0
long_no_e_word=''
short_no_e_word=''
len_no_e=0
char='a' #character from which I increase while iterating the letters
letter_word_count=0  # fro counting the words that begin with letters from a to z
nbr_list=[] #list that will store the number of words starting by letters from a to z in order



for line in infile:
    word=line[:len(line)-1] #remove the new line character '\n' at the end of each line
    words_list.append(word)
    #words that do not contain 'e'
    if 'e' not in word:
            no_e_count +=1
            if len_no_e<len(word): #checking for the length of the word without 'e' 
               long_no_e_word=word
               len_no_e=len(word)
            else:
               short_no_e_word=word
            
    #printing words with more than 20 letters
    if len(word)>20: 
       print (word)
    #checking for palindrome    
    if isPalindrome(word):
        pal +=1
        if long_len<len(word): #checking for the length of the palindrome 
            long_pal=word
            long_len=len(word)
        else:
            short_pal=word
       
    #print (word)
    #printing nbr of words that start with specicific alphabets
    if word[0]==char:    #as the words are already sorted in alphabetical order, I will use this loop to count words that start with alphabets
        letter_word_count+=1
        
    else:
        nbr_list.append(letter_word_count)
        char=chr(ord(char)+1) #incrementing the letters from a to y using their ASCII codes
        letter_word_count=0
    
infile.close()
print()
print("In the official list of 113,809 crosswords, there are "+ str(pal),"palindromes.\n\
The shortest palindrome is "+short_pal,"\n\
The longest palindrome is "+long_pal)
print()

print("In the official list of 113,809 crosswords, there are "+ str(no_e_count),"words that do not have 'e'.\n\
The shortest such word is "+short_no_e_word,"and the longest such word is "+long_no_e_word)
print()

    
#printing the number of words starting with a to z
ch='a'
freq_l_value=0
freq_letter=''

#separately calculating the number of words starting in z as it is being skipped above 
count_z=113809-sum(nbr_list)

##print("In the official list of 113,809 crosswords,\n")
for i in nbr_list:
    print(str(i),"words begin with '"+str(ch)+"'.")    #printing the number of words starting with a to y
    if i>freq_l_value: #checking for most frequently first letter
            freq_l_value=i
            freq_letter=str(ch)
    ch=chr(ord(ch)+1)
if freq_l_value<count_z: #separately checking for frequency with z
    freq_letter=str('z')
    
print(str(count_z),"words begin with 'z'.")
print("and",freq_letter,"is the most frequently-used first letter.")
print()

#calculating number of words that use different alphabets
ch='a'
char='a'
counter_w=0
count_freq=0
freq_used_value=0
freq_used_letter=0
freq_list=[]
freq_count_list=[]
while ord(ch)<=ord('z'):
    for i in words_list: #it will check for every sinlge letter in all the words always sstarting from the first word for each letter
        if ch in i:
            counter_w +=1 #counting how many words contain the letter 
            for j in range(len(i)):
                if i[j]==ch:
                   count_freq +=1 #counting the frequency of the letter in the single word
    freq_list.append(counter_w)
    freq_count_list.append(count_freq)
    ch=chr(ord(ch)+1)
    counter_w=0
    count_freq=0
    
print("In the official list of 113,809 crosswords,\n")
for i in freq_list:
    print(str(i),"words use '"+str(char)+"'.")
    char=chr(ord(char)+1)
    
#checking for most frequently used letter
char='a'
for j in freq_count_list:
    if j>freq_used_value: 
        freq_used_value=j
        freq_used_letter=str(char)
    char=chr(ord(char)+1)
print("and",freq_used_letter,"is the most frequently-used first letter.")
    

