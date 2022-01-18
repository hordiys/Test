from os import close


def check_phone(phone_number):
    correct_length = 10

    return len(phone_number) == correct_length

def get_operator(phone_number):
    operator_K = ("067", "097", "098")
    operator_V = ("050", "066", "099")
    operator_L = ("093", "063")
    
    
    code = phone[0:3]

    if code in operator_K:
        return 'K'
    elif code in operator_V:
        return 'V'
    elif code in operator_L:        
        return 'L' 
    else:
        return None

file_source = 'C:\\Test\\lessons\\lesson-12\\lesson-11-files\\phones.txt'
file_K = 'C:\\Test\\lessons\\lesson-12\\lesson-11-files\\phones-K.txt'
file_V = 'C:\\Test\\lessons\\lesson-12\\lesson-11-files\\phones-V.txt'
file_L = 'C:\\Test\\lessons\\lesson-12\\lesson-11-files\\phones-L.txt'

file_K = open(file_K, "w")
file_V = open (file_V, "w")
file_L = open(file_L, "w")
files = {'K': file_K, 'L': file_L, 'V': file_V}

with open(file_source, "r" ) as f:
    while True:
        phone = f.readline()
        if not phone:
            break
            
        phone_current = phone.rstrip('\n')    
        if(check_phone(phone_current) == True):
            print (phone_current)
            operator_code = get_operator(phone_current)
            if(operator_code):
                current_file = files[operator_code]
                current_file.write(phone_current +'\n')
                
                                
                print(phone_current)
            else:
                print ("operator is not supported", phone_current)
        else :
            print ("phone is invalid ", phone_current)
        #print(phone)
        

file_K.close()
file_L.close()
file_V.close()