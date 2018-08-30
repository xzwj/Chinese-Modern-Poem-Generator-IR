import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence
from tqdm import tqdm

def calc_keys():
    tr4w = TextRank4Keyword()
    with open("dataSet/train.txt",'r',encoding = 'utf-8') as rf_train:
        lines = rf_train.readlines()
    
    with open("dataSet/keys.txt",'w',encoding = 'utf-8') as wf_keys:
        for line in tqdm(lines):
            tr4w.analyze(text=line, lower=True, window=2)
            wf_keys.write(' '.join([item.word for item in tr4w.get_keywords(5, word_min_len=1)]))
            wf_keys.write('\n')
            
if __name__ == '__main__':
    calc_keys()
    