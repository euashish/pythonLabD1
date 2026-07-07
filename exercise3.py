# Write a program that counts how many vowels exists in a sentence.

text = input("enter a sentence :")
vowels = "aeiouAEIOU"
count = 0
for char in text : 
          if char in vowels :
                    count +=1
                    print("Number of vowels:", count)
# text = input("enter a sentence :")
# vowels = "aeiouAEIOU"
# count = 0
# for char in text : 
#           if char in vowels :
#                     count +=1
#                     print("Number of vowels:", count)
