
def caesar_encrypt(text,key) :
    import string

    az=string.ascii_lowercase
    AZ = string.ascii_uppercase

    cipher_text =''

    for letter in text :

        if letter in az :

            orgenil_letter = az.index(letter)
            location_letter =((orgenil_letter+key)%26)
            encrypted_letter = az[location_letter]
            cipher_text+=encrypted_letter

        elif letter in AZ :

            orgenil_letter = AZ.index(letter)
            location_letter =((orgenil_letter+key)%26)
            encrypted_letter = AZ[location_letter]
            cipher_text+=encrypted_letter

        else :
            cipher_text+= letter

    return cipher_text

def caesar_decrypt(text,key) :
    return caesar_encrypt(text=text,key=-key)