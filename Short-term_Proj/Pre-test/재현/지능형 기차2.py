p = 0
max_p = 0

for _ in range(10):
    out_t, in_t  = map(int, input().split()) 
    p += in_t - out_t 
    max_p = max(p, max_p) 
    
print(max_p)