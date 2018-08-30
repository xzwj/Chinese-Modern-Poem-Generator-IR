import word2vec

word2vec.word2vec("dataSet/keys.txt","dataSet/keys.bin", size=100, verbose=True)

with open("dataSet/keys.txt",'r',encoding = 'utf-8') as rf_keys:
    poem_keys = rf_keys.readlines()
    
model = word2vec.load("dataSet/keys.bin")
with open("dataSet/keywords.txt",'r',encoding = 'utf-8') as rf_keys:
    keys_lines = rf_keys.readlines()
with open("dataSet/vec.txt",'w',encoding = 'utf-8') as wf_vec:
    for keys_line in keys_lines:
        for key in keys_line.strip().split(' '):
            model.similarity(key, 'spain')
            
        


