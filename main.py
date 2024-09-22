def main():
   #VARS
   #book_path > text > character_count_dict > character_sorted_list
   book_path = "books/frankenstein.txt"
   text = get_book_text(book_path)
   w_count = word_count(text)
   character_count_dict = char_count_dict(text)
   character_sorted_list = char_dict_to_sorted_list(character_count_dict)


   #FORMATING OUTPUT
   print(f"--- Begin report of {book_path} ---")
   print(f"{w_count} words found in the document")
   print()

   for i in character_sorted_list:
       if not i["char"].isalpha():#checks if character is a letter
           continue
       print(f"The '{i['char']}' character was found '{i['num']}' times")

   print("--- End report ---") 

#FUNCTIONS
def get_book_text(path):
    with open(path) as f:
        return f.read()
            
def word_count(string): #could use a .length here
    words = string.split()
    count = 0
    for i in words:
            count += 1
    return(count)

def char_count_dict(string):#convert letters to lowercase and add them to a dict with key:value   
    lower_string = string.lower()
    dictionary = {}
    for i in lower_string:
        if i in dictionary:
            dictionary[i] += 1
        else:
             dictionary[i] = 1
    return(dictionary)

def char_dict_to_sorted_list(dict):
    list = []
    for i in dict:
        list.append({"char":i, "num":dict[i]})
    list.sort(reverse = True, key=sort_on)
    list.sort()
    return list

def sort_on(dict):  
    return dict["num"]



main()
