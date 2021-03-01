def caesar(txt,sft,dir):
    str_en = ""
    if dir == "decode":
        sft *= -1
    sl = [" ","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")",",",".","/",";","'","-","=","+","_",":","<",">","?","[","]","{","}"]
    for i in txt:
        if i in sl:
            str_en += i
            continue
        en = alphabet.index(i)
        ken = en + sft  
        new_en = alphabet[ken]
        str_en += new_en
    print(f"Your {dir}d message is {str_en}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("""
░█████╗░███████╗░█████╗░░██████╗███████╗██████╗░
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗
██║░░╚═╝█████╗░░███████║╚█████╗░█████╗░░██████╔╝
██║░░██╗██╔══╝░░██╔══██║░╚═══██╗██╔══╝░░██╔══██╗
╚█████╔╝███████╗██║░░██║██████╔╝███████╗██║░░██║
░╚════╝░╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝

░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")

restart = "yes"

while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift>26:
        shift = shift%26
    caesar(txt=text,dir=direction,sft=shift)
    restart = input("Do you wanna go again?: ").lower()


print("Thanks for playing!\nGoodbye")