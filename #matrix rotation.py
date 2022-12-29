#matrix rotation


def reverse(t,n):
    rev_mat=[]
    for i in range(n):
        rev_mat.append(t[i][::-1])
    return rev_mat
def transpose(mat,n):
    new_mat=[]
    for i in range(n):
        m=[]
        for j in range(n):
            m.append(mat[j][i])
        new_mat.append(m)
    return new_mat            
            
    
    
            
        
    
n=int(input())
mat=[]
s=0
for i in range(n):
    a=input().split()
    length=len(a)
    mat.append(a)
mat_i=mat
for inp in range(8):
    try:
        command=input().split()
        if command[0]==-1:
            break
        if "R"==command[0]:
            
            num=int(command[1])
            if num>=360:
                num=num-360
            else:
                num=num
            num=int(command[1])/90
            num=int(num)
            s+=int(command[1])
            for rotation in range(num):
                t=transpose(mat,n)
                mat=reverse(t,n)
        if "Q"==command[0]:
            print(mat[int(command[1])][int(command[2])])
        if "U"==command[0]:
            length=len(command)
            mat_i[int(command[1])][int(command[2])]=int(command[3])
            mat=mat_i
            if s>=360:
                s1=s-360
            else:
                s1=s
            s1=int(s1/90)
            for rotation in range(s1):
                t=transpose(mat,n)
                mat=reverse(t,n)
    except EOFError as e:
        print(end="")
    
    
    


