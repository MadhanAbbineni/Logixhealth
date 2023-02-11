def swap(k,s,i,c):
  for j in range(len(s)-1,k,-1):
    if(k<j):
      if(s[k]==s[i]):
        k=k+1
      else:
        if(s[j]==s[i]):
          c=c+1
          (s[k],s[j])=(s[j],s[k])
  return s,c
t=int(input())
l=[]
for x in range(t):
  s=list(input())
  k=0
  c=0
  for i in range(len(s)-1):
    if(s[i]=='2'):
      k=i+1
      s,c=swap(k,s,i,c)
    if(s[i]=='1'):
      k=i+1
      s,c=swap(k,s,i,c)
    if(s[i]=='0'):
      k=i+1
      s,c=swap(k,s,i,c)
  l.append(c)
for i in l:
  print(i)
