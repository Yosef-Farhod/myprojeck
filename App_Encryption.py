# Name : Yosef Ahmed Mabrok Farhod
import tkinter as tk 
from tkinter import messagebox

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

def create_key_matrix(key):
    
    key = key.upper().replace('J', 'I')
    matrix = []
    letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    for letter in key:
        if letter not in matrix:
            matrix.append(letter)

    for letter in letters:
        if letter not in matrix:
            matrix.append(letter)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, letter):
    
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j

def playfair_encrypt(text, key):
    
    ciphertext = ""
    matrix = create_key_matrix(key)

    text = text.upper().replace('J', 'I')
    text = text.replace(" ", "")
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            text += 'X'
        elif text[i] == text[i+1]:
            text = text[:i+1] + 'X' + text[i+1:]
        i += 2

    for i in range(0, len(text), 2):
        digraphs = text[i:i+2]
        row1, col1 = find_position(matrix, digraphs[0])
        row2, col2 = find_position(matrix, digraphs[1])

        
        if row1 == row2:
            ciphertext += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        
        elif col1 == col2:
            ciphertext += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext


def playfair_decrypt(text, key):
    
    ciphertext = ""
    matrix = create_key_matrix(key)

    text = text.upper().replace('J', 'I')
    text = text.replace(" ", "")
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            text += 'X'
        elif text[i] == text[i+1]:
            text = text[:i+1] + 'X' + text[i+1:]
        i += 2

    for i in range(0, len(text), 2):
        digraphs = text[i:i+2]
        row1, col1 = find_position(matrix, digraphs[0])
        row2, col2 = find_position(matrix, digraphs[1])

        
        if row1 == row2:
            ciphertext += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        
        elif col1 == col2:
            ciphertext += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext


def vigenere_encrypt(text, key):
    text = text.upper()
    key = key.upper()

    extended_key = (key * (len(text) // len(key) + 1))[:len(text)]

    ciphertext = []

    for p_char, k_char in zip(text, extended_key):
        if p_char.isalpha():
            encrypted_char = chr(((ord(p_char) - ord('A') + ord(k_char) - ord('A')) % 26) + ord('A'))
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(p_char) 


    return ''.join(ciphertext)


def vigenere_decrypt(text, key):
    text = text.upper()
    key = key.upper()
    extended_key = (key * (len(text) // len(key) + 1))[:len(text)]
    plaintext = []
    for c_char, k_char in zip(text, extended_key):
        if c_char.isalpha():
            decrypted_char = chr(((ord(c_char) - ord('A') - (ord(k_char) - ord('A'))) % 26) + ord('A'))
            plaintext.append(decrypted_char)
        else:
            plaintext.append(c_char) 
    return ''.join(plaintext)
#App;ication
class ChipherApp :
    def __init__(self,root):
        from tkinter import ttk
        from tkinter import font
        root.title('Cipher App')
        root.geometry('500x500')
        root.resizable(False,False)
        
        custom_font = font.Font(family="Helvetice",size=16,weight="bold")
        self.mode_labal = tk.Label(root,text='Welcome to the Encryption program ',fg='white',bg='#C2DFFF',font=custom_font)
        self.mode_labal.pack()
        self.mode_labal = tk.Label(root,text='Select Mode ',fg='white',bg='#717D7D',font=custom_font)
        self.mode_labal.pack(pady='10')

        self.mode = tk.StringVar(value="Caesar")
        self.caesar_radio = ttk.Radiobutton(root,text="Caesar Cipher",variable=self.mode,value="Caesar")
        self.caesar_radio.pack()
        self.playfair_radio = ttk.Radiobutton(root,text="Playfair Cipher",variable=self.mode,value="Playfair")
        self.playfair_radio.pack()
        self.vigenere_radio = ttk.Radiobutton(root,text="Vigenere Cipher",variable=self.mode,value="Vigenere") 
        self.vigenere_radio.pack()

        self.key_label = tk.Label(root,text=' Enter Key ')
        self.key_label.pack(pady=10)
        self.key_entry = tk.Entry(root,justify='center')
        self.key_entry.pack()

        self.text_label = ttk.Label(root,text='Enter Text ')
        self.text_label.pack()
        self.text_entry = tk.Entry(root,width=53,justify='center')
        self.text_entry.pack()

        self.result_label = ttk.Label(root,text="Result")
        self.result_label.pack()
        self.result_text = tk.Text(root,height=5,width=40)
        self.result_text.pack()

        self.encrypt_btn = ttk.Button(root,text='Encrypt',command=self.encrypt)
        self.encrypt_btn.pack(pady='5')
        self.decrypt_btn = ttk.Button(root,text='Decrypt',command=self.decrypt)
        self.decrypt_btn.pack(pady='1')
        self.clear_btn = ttk.Button(root,text='Clear',command=self.clear)
        self.clear_btn.pack(pady=20)

      


    def encrypt(self):
        text = self.text_entry.get()
        key = self.key_entry.get()
        mode =self.mode.get()
        result = ""
        if mode =="Caesar" :
            try:
                key = int(key)
                result = caesar_encrypt(text,key)
            except ValueError :
                messagebox.showerror("Invalid Key","key must be an integer for Caesar Cipher.")
                return 
        elif mode =="Playfair" :
            result = playfair_encrypt(text,key)
        elif mode =="Vigenere" :
            result = vigenere_encrypt(text,key)
        self.result_text.delete(1.0,tk.END)
        self.result_text.insert(tk.END,result)
                                
    def decrypt (self) :
        text =self.text_entry.get()
        key = self.key_entry.get()
        mode = self.mode.get()
        result=""
        if mode == "Caesar" :
            try :
                key =int(key)
                result = caesar_decrypt(text,key)
            except ValueError :
                messagebox.showerror("InvaliD Key","Key must be an integer for Caesar Cipher.")
                return
        elif mode =="Playfair" :
            result = playfair_decrypt(text,key)
        elif mode =="Vigenere" :
            result = vigenere_decrypt(text,key)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)
    def clear(self) :
        self.text_entry.delete(0, tk.END)
        self.key_entry.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)


if __name__=="__main__" :
    root= tk.Tk()
    app = ChipherApp(root)
    root.mainloop()
