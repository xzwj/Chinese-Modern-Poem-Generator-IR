# import word2vec
from gensim.models import Word2Vec
import jieba

with open("dataSet/keys.txt",'r',encoding = 'utf-8') as rf_keys:
    poem_keys = rf_keys.readlines()
sentences = [_.split(' ') for _ in poem_keys]

# model= Word2Vec()
# model.build_vocab(sentences)
# model.train(sentences, total_examples = model.corpus_count, epochs = model.iter)

# model = Word2Vec(sentences, size=100, window=5, min_count=1, workers=4)
# with open("dataSet/train.txt",'r',encoding = 'utf-8') as rf_keys:
#     train_lines = rf_keys.readlines()
# model = Word2Vec([jieba.lcut(_) for _ in train_lines], size=100, window=5, min_count=1, workers=4)
# model.save("dataSet/word2vec.model")


    
model = Word2Vec.load("dataSet/word2vec.model")
print(model)
# print(model.wv.vocab)
with open("dataSet/keywords.txt",'r',encoding = 'utf-8') as rf_keys:
    keys_lines = rf_keys.readlines()
    keys_lines = [_.strip().split(' ') for _ in keys_lines]
    
with open("dataSet/vec.txt",'w',encoding = 'utf-8') as wf_vec:
    for keys_line in keys_lines:
        for key in keys_line:
            keys = keys_line[:]
#             print(key, keys)
            wf_vec.write(' '.join([model.similarity(key, _) for _ in keys]))
            wf_vec.write('\n')
        wf_vec.write('\n')
            
        


