def countSeniors( details):
    
    cnt=0
    for detail in details:
        if int(detail[11:13])>60: 
            cnt+=1
    return cnt

print(countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))