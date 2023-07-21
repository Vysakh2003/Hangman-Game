import random

print("\n\n\t\t-----------------------")
print("\t\tWELCOME TO HANGMAN GAME\t\tBY : VYSAKH S")
print("\t\t-----------------------\n")

def generate_random_word():
    with open('words.txt', 'r') as file:
        word_list = file.read().splitlines()
    random_word = random.choice(word_list)
    return random_word

dict_word = generate_random_word().lower()

word_find = "*"*len(dict_word)
wordfind_list = list(word_find)

print("\nFIND THE WORD  :  ",word_find)

attempts = len(set(list(dict_word)))
# print(set(list(dict_word)))
print("\nYOU HAVE", attempts,"ATTEMPTS TO FIND\n")

i = 0
found = 0
while(i<attempts):
    print("\nATTEMPT",i+1)
    inp_letter = input("\nGUESS A LETTER : ").lower()
    if len(inp_letter)==1 and inp_letter.isalpha() and inp_letter not in word_find:
        if inp_letter in dict_word:
            for j in range(len(dict_word)):
                if dict_word[j]==inp_letter:
                    wordfind_list[j] = inp_letter
                    word_find = "".join(map(str,wordfind_list))
            print("\nGUESSED WORDS : ",word_find)
        else:
            print("\nGUESSED LETTER NOT IN THE WORD...")
            print("\nGUESSED WORDS : ",word_find)
        if word_find == dict_word:
            found = 1
            print("\nWOW...YOU FOUND THE WORD WITHIN THE ATTEMPTS")
            break
        i = i + 1
        print("\n")
    elif inp_letter in word_find:
        print("\nALREADY GUESSED THE LETTER ABOVE...PLEASE TRY AGAIN !")
    else:
        print("\nYOUR INPUT IS NOT A LETTER...PLEASE TRY AGAIN !")
if found==0:
    print("\nYOUR ATTEMPTS ARE OVER...\n\nBETTER LUCK NEXT TIME...\n\n")

print("\n\n\t\t-------------------")
print("\t\tEND OF HANGMAN GAME")
print("\t\t-------------------\n")


