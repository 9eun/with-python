from collections import deque
n,l,r = map(int,input().split())
arr = [list(map(int,input().split()))for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(i,j):
  q=deque()
  q.append((i,j))
  united=[]
  united.append((i,j))
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      
      if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1:
        if l<=(abs(arr[x][y]-arr[nx][ny]))<=r:
          visited[nx][ny]=1
          united.append((nx,ny))
          q.append((nx,ny))
      
  return united

result = 0
while True:
  flag=False
  visited=[[-1]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if visited[i][j]==-1:
        visited[i][j]=1
        ans = bfs(i,j)

        if len(ans)>1:
          
          flag=True 
          move = sum(arr[i][j]for i,j in ans)//len(ans)
          for g,h in ans:
            arr[g][h]=move
  if not flag:
    break
  result+=1
print(result)