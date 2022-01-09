T = int(input())
for i in range(T):
  m_count=0
  p_count=0
  vps=list(input())
  for i in vps:
    if i=="(":
      p_count+=1
    elif i==")":
      m_count+=1
    if m_count>p_count:
      print("NO")
      break
  if p_count==m_count:
    print("YES")
  elif m_count<p_count:
    print("NO")