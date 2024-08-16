# create name list
with open("Input/Names/invited_names.txt", mode='r') as invited_names:
    names = invited_names.read().splitlines()

# loop over name_list, creating a file each time
with open("Input/Letters/starting_letter.txt", 'r') as starting_letter:
    start_letter_content = starting_letter.read()

# loop over name_list, change info then write to new file
for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as output_letter:
        updated_letter = start_letter_content.replace("[name]", name)
        output_letter.write(updated_letter)





