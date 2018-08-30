from tqdm import tqdm
from collections import deque
import math
import random
# from gensim.models import Word2Vec
import word2vec
import numpy as np
import codecs

WINDOW_SIZE = 2
RANDRANGE = 1

def jaccard_sim(a, b): 
    unions = len(set(a).union(set(b))) 
    intersections = len(set(a).intersection(set(b))) 
    return 1. * intersections / unions

def cosine(diction, a, b):
    # TODO: get vecwith codecs.open('sgns.renmin.word', 'r', 'utf-8') as f:
    if diction.get(a) is not None:
        a_vec = diction[a]
    else:
        print(a)
        return 0.0
    
    b_vecs = []
    for word in b is not None:
        if diction.get(a):
            b_vecs.append(diction[a])
        else:
            b_vecs.append(np.zeros(300))
        
    cons = []
    for ii, vec in enumerate(b_vecs):
        dot_product = np.dot(a_vec, vec)
        norm_a = np.linalg.norm(a_vec)
        norm_b = np.linalg.norm(vec)
        if diction.get(b[ii]) is not None:
            cons.append(dot_product / (norm_a * norm_b))
        else:
            cons.append(0)
    return sum(cons) / len(b)
    


if __name__ == "__main__":
    with open("dataSet/keys.txt",'r',encoding = 'utf-8') as rf_keys:
        poem_keys = rf_keys.readlines()
    poem_keys = [_.split(' ') for _ in poem_keys]
    
    with open("dataSet/keywords.txt",'r',encoding = 'utf-8') as rf_keywords:
        keys_lines = rf_keywords.readlines()
    keys_lines = [_.split(' ') for _ in keys_lines]
    
    with open("dataSet/train.txt",'r',encoding = 'utf-8') as rf_train:
        train_lines = rf_train.readlines()
        train_sentences_len = len(train_lines)
    
    with codecs.open('dataSet/sgns.renmin.word', 'r', 'utf-8') as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            if len(line) == 301:
                num_array = []
                for i in range(1, 300):
                    num_array.append(float(line[i]))
                diction = {line[0]: num_array}
#                 print diction
#                 print "\n"
    
    with open("dataSet/jaccard.txt",'w',encoding = 'utf-8') as wf_jaccard:
        for key_line in tqdm(keys_lines):
            q = deque(maxlen=WINDOW_SIZE)
            for ii, key in enumerate(key_line):
                if ii == 0:
#                     jaccards = [cosine(diction, key, line) for line in poem_keys] 
                    jaccards = [jaccard_sim(key, line) for line in poem_keys] 
                    jaccards_sort = sorted(list(enumerate(jaccards)),key=lambda item: item[1],reverse=True)
                    index = random.randrange(RANDRANGE)
                    answer_index=jaccards_sort[index][0]
                    answer=train_lines[answer_index]
                    wf_jaccard.write(str(jaccards_sort[index][1])+'\t'+str(answer))
                    q.append(str(answer))
                else:
#                     jaccards = [cosine(diction, key, line) for line in poem_keys] 
                    jaccards = [jaccard_sim(key, line) for line in poem_keys]
                    index = random.randrange(RANDRANGE)
                    
                    q_reverse = q
                    q_reverse.reverse()
                    for ii, ans in enumerate(q_reverse):
#                         jaccards_history = [cosine(diction, ans, line) for line in poem_keys]
                        jaccards_history = [jaccard_sim(ans, line) for line in poem_keys]
                        jaccards = [jaccards[i] + jaccards_history[i-1] * math.exp(-(ii + 1)) if i > 0 else jaccards[i] for i in range(train_sentences_len) ]
                    jaccards_sort = sorted(list(enumerate(jaccards)),key=lambda item: item[1],reverse=True)
                    index = random.randrange(RANDRANGE)
                    answer_index=jaccards_sort[index][0]
                    answer=train_lines[answer_index]
                    wf_jaccard.write(str(jaccards_sort[index][1])+'\t'+str(answer))
                    q.append(str(answer))
            wf_jaccard.write("\n")
                
                
#                 jaccards = [jaccard_sim(key, line) for line in poem_keys] 
#                 jaccards_sort = sorted(list(enumerate(jaccards)),key=lambda item: item[1],reverse=True)
#                 with open("dataSet/train.txt",'r',encoding = 'utf-8') as rf_train:
#                     train_lines = rf_train.readlines()
#                 wf_jaccard.write(train_lines[jaccards_sort[0][0]])
#             wf_jaccard.write('\n')


            
#             jaccards = [jaccard_sim(key_line, line) for line in poem_keys]
#             jaccards_sort = sorted(list(enumerate(jaccards)),key=lambda item: item[1],reverse=True)
# #             wf_jaccard.write('\n'.join([' '.join(poem_keys[_[0]]) + '\t' + str(_[1])] for _ in jaccards_sort))

#             for i in range(len(key_line)):
# #                     print(i)
#                 wf_jaccard.write(train_lines[jaccards_sort[i][0]])
            
#             wf_jaccard.write('\n')
        