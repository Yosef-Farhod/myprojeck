
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