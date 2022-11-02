import qrcode

file_path = r'qr메이커\qr코드모음.txt'
with open(file_path,'rt',encoding='UTF-8')as f:
      read_file = f.readlines()
      for line in read_file:
            line = line.strip()
            print(line)
