from retrieval import find_chunks

while True:
    question = input("질문 입력(끝내려면 종료):")
    if question == "종료":
        break
    matches=find_chunks(question)
    print("찾은 문단 수:", len(matches))
    
    # 검색 결과가 없을 때
    if not matches:
        print("자료에서 관련 내용을 찾지 못했습니다.\n")
           #  "sources":[],  
    
    for match in matches:
        print(f"파일 : {match['source']}")
        print(f"내용 앞부분 : , {match['text'][:80]}")
        