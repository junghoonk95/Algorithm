n = int(input())
paper = [list(map(int, input().split())) for i in range(n)]
result = [0,0,0]

def divid(x,y,n):
  check = paper[x][y]
  for i in range(x,x+n):
    for j in range(y,y+n):
      if paper[i][j] != check :
        divid(x,y,n//3)      
        divid(x,y+n//3,n//3)
        divid(x,y+n//3*2,n//3)     
        divid(x+n//3,y,n//3)       
        divid(x+n//3,y+n//3,n//3) 
        divid(x+n//3,y+n//3*2,n//3)   
        divid(x+n//3*2,y,n//3)       
        divid(x+n//3*2,y+n//3,n//3) 
        divid(x+n//3*2,y+n//3*2,n//3) 
        return

  result[check] += 1
  return

divid(0,0,n)

print(result[-1])
print(result[0])
print(result[1])
