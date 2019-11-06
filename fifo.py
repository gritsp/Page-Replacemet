def addPageFifo(data,max):
    result = []
    page_fault = 0 

    for i in range(len(data)):
        page = []
        if(i<max):
            if(i==0):
                page.append([data[i],i])
                page.append([' ',i])
                page.append([' ',i])
                page_fault +=1
            else:
                if(checkUse(result[i-1],data[i])==False):
                    for j in result[i-1]:
                        page.append(j)
                else:
                    for j in range(i+1):
                        page.append([data[j],j])
                    page_fault +=1
                if i == 1:
                    page.append([' ',0])
        else:
            if(checkUse(result[i-1],data[i])==False):
                for j in result[i-1]:
                    page.append(j)
            else:
                for j in range(max):
                    if(result[i-1][j][1]==0):                   
                        page.append([data[i],2])   
                                       
                    else:
                        temp = result[i-1][j][0]
                        index = result[i-1][j][1]-1
                        page.append([temp,index])        
                page_fault +=1  
        result.append(page)
    return [result,page_fault]

def checkUse(page,data):
    for i in page:
        if(i[0]==data):
            return False        
    return True

# data = input('>')
# a = addPageFifo(data,3)

# print(a)
