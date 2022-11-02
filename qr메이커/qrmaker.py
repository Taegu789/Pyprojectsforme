import qrcode

qr_data ='www.naver.com'
picof = qrcode.make(qr_data)
type(picof)
picof.save("naver.png")
