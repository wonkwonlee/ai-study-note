import pymysql
import pandas as pd

db = None
try:
    #DB 호스트 정보에 맞게 입력
    db = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        db='k_digital',
        charset='utf8'
    )
    print("DB 연결 성공 ")

    # 데이터 DB에 추가될 항목들 정리 ---1
    students = [
        {'name': 'ABC', 'age': 36, 'address': 'SEOUL'},
        {'name': 'DEF','age': 22, 'address': 'ANYANG'},
        {'name': 'MARK', 'age': 31, 'address': 'ANYANG'},
        {'name': 'JAMES','age': 27, 'address': 'PUSAN'},
    ]
    for s in students:  # 한 줄씩 읽어와 s에 저장
        with db.cursor() as cursor:
            sql = '''
            insert tb_student(name, age, address) values("%s", "%d", "%s")
            ''' % (s['name'], s['age'], s['address'])
            cursor.execute(sql)
    db.commit()

    # 30대 학생만 조회 ---2
    cond_age = 30
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = '''
        select * from tb_student where age > %d 
        '''% cond_age
        cursor.execute(sql)
        results = cursor.fetchall()
    print(results)

    cond_name = 'ABC' #찾고자 하는 이름
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = '''
        select * from tb_student where name="%s"
        ''' % cond_name
        cursor.execute(sql)
        result = cursor.fetchone() #select 구문으로 조회한 데이터 중 하나만 불러오는 함수
    print(result['name'], result['age'])

    #pandas 데이터 프레임으로 표현
    df = pd.DataFrame(results)
    print(df)

except Exception as e:
    print(e) #DB 연결 실패 시 오류 내용 출력

finally:
    if db is not None: #DB 가 연결된 경우에만 접속 닫기 시도
        db.close()
        print("DB 연결 닫기 성공")




