def solution(new_id):
    new_id = new_id.lower() #1
    #print(new_id)
    spe = "~!@#$%^&*()=+[{]}:?,<>/" #2
    for e in new_id:
        if spe.find(e) > -1:
            new_id = new_id.replace(e," ")
    new_id = new_id.replace(" ","")
    #print(new_id)
    
    while(new_id.find("..") > -1 ): #3
        new_id = new_id.replace("..",".")
    #print(new_id)
    
    if new_id == ".":
        new_id = ""
    else :
        if new_id[0] == ".": #4
            new_id = new_id[1:]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    #print(new_id)    
    
    if new_id == "": #5
        new_id += 'a'
    #print(new_id)    
    
    if len(new_id) >= 16 : #6
        new_id = new_id[:15]
        if new_id [-1]== ".":
            new_id = new_id[:-1]
    #print(new_id)
    
    if len(new_id) <= 2 : #7
        new_id += (new_id[-1]*4)
        new_id = new_id[:3]
    #print(new_id)
    return new_id
