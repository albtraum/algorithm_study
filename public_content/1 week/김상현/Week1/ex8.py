def solution(new_id):
    while True:
        new_id=new_id.lower()   #1단계
        new_id=list(new_id)  
        arr=[]
        arr1=[]
        for i in new_id:
            if (ord(i)>=97 and ord(i)<123) or (ord(i)>=48 and ord(i)<58) or i=="-" or i=="_" or i==".":     #2단계
                arr.append(i)
            else:
                continue
        for i in range(1,len(arr)):
            if arr[i-1]=="." and arr[i]==".":       #3단계
                continue
            else:
                arr1.append(arr[i-1])
        arr1.append(arr[len(arr)-1])
        if len(arr1)>=1:            #4단계
            if arr1[0]==".":
                arr1.remove(arr[0])
        if len(arr1)>=1:            #만약 arr1이 "."이었으면 앞에서 지워져서 arr1[-1]값이 없으므로 따로 코딩했다.
            if arr1[-1]==".":
                arr1.pop()
        if arr1==[]:
            arr1.append('a')        #5단계
        arr=[]
        if len(arr1)>=16:           #6단계
            for i in range(15):
                arr.append(arr1[i])
        else:
            for i in range(len(arr1)):
                arr.append(arr1[i])
        if len(arr)==1:             #7단계
            arr.append(arr[0])
            arr.append(arr[0])
        if len(arr)==2:
            arr.append(arr[1])
        new_id="".join(arr)
        if new_id[0]!="." and new_id[-1]!=".":      #만약 .이 맨앞과 맨뒤에 있으면 while문을 다시 반복한다.
            break
    return new_id