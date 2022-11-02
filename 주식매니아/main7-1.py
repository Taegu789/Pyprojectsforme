from currency_converter import CurrencyConverter

cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
print(cc.convert(1,'USD','KRW'))
#ZIP 파일을 받아서 ( 최신 환율) 1 당 USD KRW 환율
# 1428.4042~쯤