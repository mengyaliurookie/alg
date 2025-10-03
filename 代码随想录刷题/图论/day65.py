import math
# 第k短路
def main():
    n,m=map(int,input().strip().split())
    edges=[]
    for _ in range(m):
        edges.append(list(map(int,input().strip().split())))
    src,dst,k=map(int,input().strip().split())
    mindist=[math.inf]*(n+1)
    mindist[src]=0
    for _ in range(k+1):
        lastmin=mindist[:]
        for i,j,v in edges:
            if lastmin[i]!=math.inf and mindist[j]>lastmin[i]+v:
                mindist[j]=lastmin[i]+v
    if mindist[dst]==math.inf:
        print("unreachable")
    else:
        print(mindist[dst])
if __name__=="__main__":
    main()