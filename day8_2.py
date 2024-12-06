alphabet = ["a" , "b" , "c" , "d" ,"e" ,"f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" ,"q" , "r" , "s" , "t" , "u" , "v" , "w" ,"x" , "y" , "z"]

def caesar(original_text,shift_amount,encode_or_decode):
    Output_text=""

    if encode_or_decode == "decode":
                shift_amount *= -1

    for char in original_text:
        if char not in alphabet:
            Output_text += char

        else:
           shifted_position = alphabet.index(char) + shift_amount

           shifted_position %= len(alphabet)
           Output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result : {Output_text}")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : ").lower()
    text = input("Type Your Message : ").lower()
    shift = int(input("Type the shift Number : "))

    caesar(original_text=text , shift_amount=shift , encode_or_decode=direction)

    restart =  input("Type 'yes' if you want to go again. Otherwise,type 'no' : ").lower()
    if restart == "no":
            should_continue = False
            print("Good Bye!")



