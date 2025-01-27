def main():

    book_path = 'books/frankenstein.txt'
    print_report(book_path)

def get_num_words(text):
    words = text.split()
    return len(words)
    
def count_characters(text):
    low_text = text.lower()

    characters_dic = {}
    for c in low_text:
        
        if characters_dic.get(c) == None:
            characters_dic[c] = 1
        else:
            characters_dic[c] += 1

    return characters_dic

def print_report(path):

    text = get_book_text(path)
    num_words = get_num_words(text)
    dic = count_characters(text)

    remove = []

    for c in dic:
       
        if (str(c).isalpha()) == False:
            remove.append(c)

    for r in remove:
        dic.pop(r)

    dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

    print(f'--- Begin report of {path} ---')
    print(f'{num_words} words found in the document \n')
    
    for f in dic:
        print(f"The '{f}' character was found {dic[f]} times")
    print('--- End report ---')

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()