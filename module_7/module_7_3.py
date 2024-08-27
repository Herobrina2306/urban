import re


class WordsFinder:
    file_names = []
    def __init__(self, *files):
        for i in files:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        list_ = []
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                for line in file:
                    m = re.split(' ', line)
                    for j in m:
                        r = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
                        for z in r:
                            j = j.replace(z, '')
                            j = j.lower()
                        list_.append(j)
                all_words[i] = list_
                return all_words

    def find(self, word):
        words = self.get_all_words()
        word = word.lower()
        w = {}
        for k, v in words.items():
            for i in range(len(v)):
                if word == v[i]:
                    w[k] = i+1
                    return w

    def count(self, word):
        words = self.get_all_words()
        word = word.lower()
        w = {}
        cou = 0
        for k, v in words.items():
            for i in v:
                if word == i:
                    cou +=1
            w[k] = cou
            return w




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
