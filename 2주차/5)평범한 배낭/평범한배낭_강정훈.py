###시간 초과...

n,K =map(int,input().split())
w=[]
val=[]
for i in range(n):
    w_t,v_t=map(int, input().split())
    w.append(w_t)
    val.append(v_t)

def knap(K, w, val, n):
    if n == 0 :
        return 0
    elif (w[n-1] > K):
        return knap(K, w, val, n-1)
    else:
        return max(
            val[n-1] + knap(
                K-w[n-1], w, val, n-1),
            knap(K, w, val, n-1))



print(knap(K, w, val, n))
