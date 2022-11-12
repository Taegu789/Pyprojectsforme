# 파이토치를 응용해서 사람의 얼굴을 인식하여보자.

from glob import glob
# glob 이란 무엇일까 -> 글롭을 통해서 .exe, .txt 처럼 뒤에 패턴이 일치하는 모든 것을 불러올 수 가있음!!!! 패턴을 주려면 별 때려박기~

img_path = r'40. 사진 사람인식\humans'

img_list = glob(img_path + "\*.jpg")
# 글롭을 통해서 jpg 패턴의 파일들을 다 가져오렴~ ^_^
print(img_list)
