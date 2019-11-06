def addPageLru(data,max):
    result = []
    page_fault = 0 

    for i in range(len(data)):
        page = []
        if(i<max):
            if(i==0):
                page.append([data[i],i,0])
                page_fault +=1
            else:
                if(checkUse(result[i-1],data[i])==False):
                    for j in result[i-1]:
                        if(j[0]==data[i]):
                            temp = j[2]+1
                            page.append([data[i],j[1],temp]) 
                        else:
                            page.append(j)
                else:
                    for j in range(i+1):
                        page.append([data[j],j,0])
                    page_fault +=1
        else:
            if(checkUse(result[i-1],data[i])==False):
                for j in result[i-1]:
                    if(j[0]==data[i]):
                        temp = j[2]+1
                        page.append([data[i],j[1],temp]) 
                    else:
                        page.append(j)
            else:
                least = len(data)
                leastInput = 0                    
                for k in range(3):
                    if(result[i-1][k][2]<=least):
                        least = result[i-1][k][2]
                    
                
                for j in range(max):                    
                    if(result[i-1][j][2]==least and result[i-1][j][1]==0 ):                   
                        page.append([data[i],2,0])   
                                       
                    else:
                        temp = result[i-1][j][0]
                        index = result[i-1][j][1]-1
                        use = result[i-1][j][2]
                        page.append([temp,index,use])        
                page_fault +=1  
        result.append(page)
    return [result,page_fault]

def checkUse(page,data):
    for i in page:
        if(i[0]==data):
            return False        
    return True

data = input('>')
a = addPageLru(data,3)

print(a)