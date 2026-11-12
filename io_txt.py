print("hello")

from pathlib import Path 
#Path라는 라이브러리로 호출
# from 어떤 함수 어떤 모듈을 사용할거냐
def read_document():
#변수는 직관적으로 만든다.함수이름도.
  return Path("data/git_기초.txt").read_text(encoding="utf-8") 

def save_preview(preview): #def는함수 output
# 파이썬에없는함수니까. 내가 만들어서 쓰겠다
#()는 함수의 호출
  output_dir = Path("output")
  output_dir.mkdir(exist_ok=True)
  (output_dir/"미리보기.txt").write_text(preview,encoding="utf-8") #인코딩 한글로인코딩해라깨지지않게

text = read_document()
preview = text[:100]
print(preview)
save_preview(preview)