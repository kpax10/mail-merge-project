#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# create name list
with open("Input/Names/invited_names.txt", mode='r') as f:
    name_list = f.read().splitlines()

# loop over name_list, creating a file each time
with open("Input/Letters/starting_letter.txt", 'r') as file:
    letter_data = file.read()

# loop over name_list, change info then write to new file
for name in name_list:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as name_letter:
        new_info = letter_data.replace("[name]", name)
        name_letter.write(new_info)





