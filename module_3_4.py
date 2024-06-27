def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if str(root_word.lower()) in str(i.lower()) or str(i.lower()) in str(root_word.lower()):
            same_words.append(i)
        else:
            continue
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)