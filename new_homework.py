


def fanc(nuber,cheir,cheir_list):
    while True:
        pasword = input('enter password--').title
        if ' ' in pasword:
            print('your password is not true')
        if len(pasword) < 8:
            print('you are enter wrong pasword')
            continue
        else:
            for i in pasword:
                if i.isdigit:
                    nuber +=1
                if i in cheir_list:
                    cheir += 1
        if nuber >= 2 and cheir >= 2:
            print('your pasword is strong')
            break
fanc(0,0,['!','@','#','$','%','&','*','/'])        
