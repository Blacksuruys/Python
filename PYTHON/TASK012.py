# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте.

# Единственное исключение — некоторые продавцы распродадут свой товар, купленный по старому курсу, по старым же ценам.
n = input("Введите предложение: ")
words = 0
cur_word = ''
list_2 = []

list_1 = ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в',
          'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', 'ё']

for i in n.lower():
    if i in list_1:
        cur_word += i
    else:
        if cur_word!='':
            list_2.append(cur_word)
        cur_word = ''
print(len(set(list_2)))

