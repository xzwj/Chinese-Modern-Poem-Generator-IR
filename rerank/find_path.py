def find_path(j):
    path_vertexs.append(j)  #把该节点标记为已走过    
    row=c[j]  
    #创建copy_row,删除row中已走过的顶点,防止直接在row上操作.
    copy_row=[value for value in row]
    walked_vertex=[]
    for i in path_vertexs:#已走过的顶点
        walked_vertex.append(copy_row[i])
    for vertex in walked_vertex:
        copy_row.remove(vertex)
    #寻找row中的未遍历过的最短边
    if len(path_vertexs)<5:
        min_e=min(copy_row)
        j=row.index(min_e)
        path_length.append(min_e)
        find_path(j)
    else:
        min_e=c[j][0]
        path_length.append(min_e)
        path_vertexs.append(0)
    return path_vertexs,path_length

def print_path(vertexs,lengths):
    path=[]    
    vertexs=[vertex+1 for vertex in vertexs]
    for i,vertex in enumerate(vertexs):
        path.append(vertexs)
        if i==5:
            break
        
    print("最小总旅费为：",sum(lengths))
    print("路 径：",path)
    
def init(distances):
    path_length_sum = 0
    path_vertexs = []
    for i in range(len(distances)):
        path_vertexs_tmp, path_length=find_path(0)
        if path_length_sum < sum(path_length):
            path_vertexs_sum = sum(path_vertexs)
            path_vertexs = path_vertexs_tmp
    return path_vertexs
            
    
    

if __name__ == "__main__":
    c=[[0,3,1,5,8],
    [3,0,6,7,9],
    [1,6,0,4,2],
    [5,7,4,0,3],
    [8,9,2,3,0]]
    path_length=[]
    path_vertexs=[]   
    path_vertexs,path_length=find_path(0)
    print_path(path_vertexs,path_length)
