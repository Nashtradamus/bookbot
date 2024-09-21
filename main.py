def main():
   book_path = "books/frankenstein.txt"
   text = get_book_text(book_path)
   w_count = word_count(text)
   character_count_dict = char_count_dict(text)
   character_sorted_list = char_dict_to_sorted_list(character_count_dict)

   print(f"--- Begin report of {book_path} ---")
   print(f"{w_count} words found in the document")
   print()

   for i in character_sorted_list:
       if not i["char"].isalpha():
           continue #never showed this in lessons
       print(f"The '{i['char']}' character was found '{i['num']}' times")#never covered the difference between signle and double quotes. Simply stated to be consistent and always use double quotes
       #also never explained why you don't have to use single quotes around second set of elip for i['num']

   print("--- End report ---") #had to shift + left arrow to delete space that was getting auto inserted at beginning or I get an indentation error, this was never covered

def get_book_text(path):
    with open(path) as f:
        return f.read()
            
def word_count(string):
    words = string.split()
    count = 0
    for i in words:
            count += 1
    return(count)

def char_count_dict(string):   
    lower_string = string.lower()
    dictionary = {}
    for i in lower_string:
        if i in dictionary:
            dictionary[i] += 1
        else:
             dictionary[i] = 1
    return(dictionary)

def sort_on(dict):  
    return dict["num"]

def char_dict_to_sorted_list(dict):
    list = []
    for i in dict:
        list.append({"char": i, "num": dict[i]})

    list.sort(reverse=True, key=sort_on) #never showed "sort" in lessons, mentions it for first time in this project
    #every other time we have called a funtion you have to pass a value but for some reason with sort you don't have to when using "key="
    return list

main()
