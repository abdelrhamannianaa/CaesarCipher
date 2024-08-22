

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encryptionAndDecryption(direction,message,shift):
    output = ""
    for letter in message:
       if letter not in alphabet: #this is to keep the whitespaces or characters that aren't letters as is
           output+=letter
       else:   
           if direction == "encode":
             shiftedPosition = alphabet.index(letter) + shift #this is the index of the letter in message + its shift
           elif direction == "decode":
             shiftedPosition = alphabet.index(letter) - shift #this is the index of the letter in message - its shift
           shiftedPosition %= len(alphabet)# this is to ensure its always between 0 and 25 never over or under
           output += alphabet[shiftedPosition]
    print(f"Here is the {direction}d result: {output}")

restart = True #flag for whether the user wants to go again or exit 
while restart:
    direction = input("Which way do you want to go, encode or decode?: ").lower()
    while direction != "encode" and direction != "decode":
        direction = input("Please enter a valid direction to go: ").lower()
    message = input("What is the message you're trying to get accross?:  ").lower()
    shift = int(input("Type the shift number: "))

    encryptionAndDecryption(direction,message,shift)
    again = input("Would you like to go again? ").lower()
    if again == "yes":
       restart = True
    elif again == "no":
       restart = False      
    else:
       again = input("Please enter a valid answer: ").lower()



     

    
