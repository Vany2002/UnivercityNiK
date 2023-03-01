import re
import pymorphy2
from translate import Translator

translator = Translator(from_lang="ru", to_lang="en")
morph = pymorphy2.MorphAnalyzer()

def get_norm():
    file: TextIOWrapper = open('dialog.txt', mode='r+', encoding='utf-8')
    content: str = file.read()
    content: str = content.lower()
    p: str = r"(?:\я|\w+[^(\W|\d)]+)"
    words: list = re.findall(p, content)
    return words

def get_dict():
    lw: list = get_norm()
    dw: dict = {}

    for word in lw:
        if word in dw:
            dw[word] += 1
        else:
            dw[word] = 1
    return dw

def translate():
    dw: dict = get_dict()
    sdw: dict = dict(sorted(dw.items()))
    slw: list = sorted(sdw, key=sdw.get, reverse=True)
    res = open('translation.txt', mode='w+', encoding='utf-8')
    for word in slw:
        for key, value in sdw.items():
            if word == key:
                gw: pymorphy2.analyzer.Parse = morph.parse(word)[0]
                word: str = gw.normal_form
                tw: str = translator.translate(word)
                res.write(str(word))
                res.write("|")
                res.write(str(tw))
                res.write("|")
                res.write(str(value))
                res.write('\n')

    return "done"
