
matrix = [['1','2','3','4'],['1','2','3','4'],['1','2','3','?'],['1','?','3','4'],
          ['5','6','7','8'],['5','6','7','8'],['5','6','7','8'],['5','6','7','8'],
          ['9','10','?','12'],['9','10','11','12'],['9','10','11','12'],['9','10','11','12'],
          ['13','14','15','16'],['13','14','?','16'],['13','14','15','16'],['13','14','15','16']
          ]
def replace_intero(arrayo):
    checker = set(tuple(range(1,17)))
    for i in range(len(arrayo)):
        if arrayo[i] !='?':
            checker.remove(int(arrayo[i]))
        else:
            index = i
    arrayo[index]= checker.pop()
    arrayo.append(arrayo[index])

def fill_missing(matrix):
    num_mat = len(matrix)//4
    mat_list = [[] for _ in range(num_mat)]
    for i in range(len(matrix)):
        j = i % num_mat
        mat_list[j]+=matrix[i]
    for row in mat_list:
        replace_intero(row)
    mat_list.sort(key=lambda x:x[-1])
    print(mat_list)
    new_mat = []
    
    i=0
    while i<12:
        j=0
        while j < num_mat:
            new_mat.append(mat_list[j][i:i+4])
            print(mat_list[j][i:i+4])
            j+=1
        i+=4
    print(new_mat)
        
fill_missing(matrix)