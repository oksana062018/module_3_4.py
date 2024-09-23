def single_root_words(root_word, *other_words):
    same_words = []
    for k in other_words:
        if root_word.lower() in k.lower() or k.lower() in root_word.lower():
            same_words.append(k)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)




