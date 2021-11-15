def solution(new_id):
    while True:
        new_id=new_id.lower()   #1단계
        new_id=list(new_id)
        arr=[]
        arr1=[]
        for i in new_id:
            if (ord(i)>=97 and ord(i)<123) or (ord(i)>=48 and ord(i)<58) or i=="-" or i=="_" or i==".":
                arr.append(i)
            else:
                continue
        for i in range(1,len(arr)):
            if arr[i-1]=="." and arr[i]==".":
                continue
            else:
                arr1.append(arr[i-1])
        arr1.append(arr[len(arr)-1])
        if len(arr1)>=1:
            if arr1[0]==".":
                arr1.remove(arr[0])
        if len(arr1)>=1:
            if arr1[-1]==".":
                arr1.pop()
        if arr1==[]:
            arr1.append('a')
        arr=[]
        if len(arr1)>=16:
            for i in range(15):
                arr.append(arr1[i])
        else:
            for i in range(len(arr1)):
                arr.append(arr1[i])
        if len(arr)==1:
            arr.append(arr[0])
            arr.append(arr[0])
        if len(arr)==2:
            arr.append(arr[1])
        new_id="".join(arr)
        if new_id[0]!="." and new_id[-1]!=".":
            break
    return new_id