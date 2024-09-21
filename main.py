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
    dictionary = {}
    for i in lower_string:
        if i in dictionary:
            dictionary[i] += 1
        else:
             dictionary[i] = 1
    return(dictionary)
    
main()