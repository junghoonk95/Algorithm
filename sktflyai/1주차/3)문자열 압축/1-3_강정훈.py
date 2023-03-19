def solution(s):
    arr=[]
    sol=[]
    if len(s)==1:
        return 1
    else:
        for i in range(1,len(s)):
            a=[s[j:j+i] for j in range(0,len(s),i)]
            a.append(0)
            newst=""
            q=[]
            cnt=1
            for t in range(len(a)-1):
                q.append(a[t])
                if a[t+1] in q:
                    cnt=cnt+1

                else:
                    if cnt>1:
                        newst=newst+str(cnt)+q[0]
                        cnt=1
                        q=[]
                    else:
                        newst=newst+q[0]
                        cnt=1
                        q=[]

            sol.append(len(newst))
        print(sol)
        return(min(sol))
