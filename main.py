def main():
   book_path = "books/frankenstein.txt"
   #text = "Hello my name is Nash and I love to cook, sometimes."
   text = get_book_text(book_path)
   w_count = word_count(text)
   character_count = char_count(text)
   print(character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
            

def word_count(string):
    words = string.split()
    count = 0
    for i in words:
            count += 1
    return(count)

def char_count(string):   
    lower_string = string.lower()
    dictionary = {
         "a": 0,
         "b": 0,
         "c": 0,
         "d": 0,
         "e": 0,
         "f": 0,
         "g": 0,
         "h": 0,
         "i": 0,
         "j": 0,
         "k": 0,
         "l": 0,
         "m": 0,
         "n": 0,
         "o": 0,
         "p": 0,
         "q": 0,
         "r": 0,
         "s": 0,
         "t": 0,
         "u": 0,
         "v": 0,
         "w": 0,
         "x": 0,
         "y": 0,
         "z": 0,
    }
    list = "abcdefghijklmnopqrstuvwxyz"
    for i in lower_string:
        if i in list:
              dictionary[i] += 1
        else:
             pass
    return(dictionary)
    
main()