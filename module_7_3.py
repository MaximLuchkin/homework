import re


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as f:
                words = []
                for line in f:
                    line = line.lower()
                    line = re.sub(r'[,.!=?;:\s-]+', ' ', line)
                    words.extend(line.split())
                all_words[file] = words
        return all_words

    def find(self, word):
        result = {}
        word = word.lower()
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1
        return result

    def count(self, word):
        result = {}
        word = word.lower()
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего