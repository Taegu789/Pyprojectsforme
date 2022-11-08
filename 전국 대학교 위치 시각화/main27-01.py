import pandas as pd

filePath = r'C:\Users\user\Downloads\Pyprojectsforme\전국 대학교 위치 시각화\고등교육기관 하반기 주소록(2021).xlsx'

df_from_excel = pd.read_excel(filePath,engine='openpyxl')

df_from_excel.columns = df_from_excel.loc[4].tolist()

un1 = df_from_excel.columns

#엑셀파일의 4번째 행의 값을 칼럼으로 지정해준다.
print(un1)