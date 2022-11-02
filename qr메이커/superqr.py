import qrcode

file_path = r'qr메이커\qr코드모음.txt'
with open(file_path,'rt',encoding='UTF-8')as f:
        read_file = f.readlines()
        
        #for문은 여러번 반복되어진다.
        for line in read_file:
            line = line.strip()
            print(line)
            
            qr_data = line
            qr_img = qrcode.make(qr_data)
            
            save_path = 'qr메이커\\' + qr_data + '.png'
            qr_img.save(save_path)
