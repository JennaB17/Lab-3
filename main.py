#Part A Function 1

a = input("Please enter a string of numbers and words: ")   #user enters inputs as list
list1 = []   #empty list to add elements in by the input

for numbers in a.split():   #split the input returns a list of stings and returns it as integers
  if numbers.isdigit() == True:   #isdigit true is equal to integers
    list1.append(int(numbers))   #adds elements to a list
print(list1)   #prints the integers only

list2 = []
for words in a.split(): 
  if words.isdigit() == False: #isdigit false is not equal 
    list2.append(str(words))
print(list2) # print the words in the list


# Function 2
list1 # take list 1
list1.sort(reverse= True) # reverse its order

print(list1[::2]) # print every second number in the list in reversed order