for num in range(1,51):
    file_name =open(str(num) + "주차.txt", "w",encoding="utf8")
    print("""-{0} 주차 주간보고 -
    부서 : 
    이름 : 
    업무 요약: """.format(num), file=file_name)