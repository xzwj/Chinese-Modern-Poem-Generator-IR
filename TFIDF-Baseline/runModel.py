#encoding=utf-8

from cutWords import *
from fileObject import FileObj
from sentenceSimilarity import SentenceSimilarity
from sentence import Sentence
from tqdm import tqdm
import pickle
from collections import deque
import random
import string
from zhon.hanzi import punctuation

NO_PUNCTUATION = False # 去掉每句话首尾的标点
RANDRANGE = 1
MORE_HAPPY = True
BAD_EMO = ['死', '亡']


if __name__ == '__main__':
    # 读入训练集
    file_obj = FileObj(r"dataSet/train.txt")  
    train_sentences = file_obj.read_lines()
    train_sentences_len = len(train_sentences)
   

    # 读入测试集
    file_obj = FileObj(r"dataSet/test_keywords.txt")   
    test_sentences = file_obj.read_lines()


    # 分词工具，基于jieba分词，并去除停用词
    seg = Seg()

    # 训练模型
#     ss = SentenceSimilarity(seg)
#     ss.set_sentences(train_sentences)
#     ss.TfidfModel()         # tfidf模型
    
#     pickle.dump(ss, open('./dataSet/ss.pkl', 'wb+'), protocol=4)
        
    ss = pickle.load(open('./dataSet/ss.pkl', 'rb'))

    # 测试集
    right_count = 0
    
    file_result=open('dataSet/result.txt','w')
    with open("dataSet/train.txt",'r',encoding = 'utf-8') as file_answer:
        line = file_answer.readlines()
           
    for i in tqdm(range(0,len(test_sentences))):
#         q = deque(maxlen=4)
        for ii, keyword in enumerate(test_sentences[i].split(' ')):
            
            if ii == 0:
                top_15, _ = ss.similarity(keyword)
                index = random.randrange(RANDRANGE)
                answer_index=top_15[index][0]
                answer=line[answer_index]
                if NO_PUNCTUATION:
                    file_result.write(str(top_15[index][1])+'\t'+str(answer).strip(string.punctuation).strip(punctuation))
                else:
                    file_result.write(str(top_15[index][1])+'\t'+str(answer))
#                 deque.append(str(answer))
            else:
                _, sims_curr = ss.similarity(keyword)
                _, sims_last_sentence = ss.similarity(str(answer))
                sims = [sims_curr[i] + sims_last_sentence[i-1] * 0.5 if i > 0 else sims_curr[i] for i in range(train_sentences_len) ]
                sim_sort = sorted(list(enumerate(sims)),key=lambda item: item[1],reverse=True)
                
                index = random.randrange(RANDRANGE)
                answer_index=sim_sort[index][0]
                
                answer=line[answer_index]
                if NO_PUNCTUATION:
                    file_result.write(str(sim_sort[index][1])+'\t'+str(answer).strip(string.punctuation).strip(punctuation))
                else:
                    file_result.write(str(sim_sort[index][1])+'\t'+str(answer))
                sims_last = sims_curr
        file_result.write("\n")
#                 deque.append(str(answer))

#             top_15, _ = ss.similarity(keyword)
#             for j in range(0,len(top_15)):
#                 answer_index=top_15[j][0]
#                 answer=line[answer_index]
#                 file_result.write(str(top_15[j][1])+'\t'+str(answer))
#             file_result.write("\n")
        
    file_result.close() 
    
