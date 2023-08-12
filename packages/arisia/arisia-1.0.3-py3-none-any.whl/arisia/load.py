# def load():
#     # package installer
#     import os
#     # list of packages and packages2
#     packages = ['numpy', 'pandas', 'scipy', 'scikit-learn', 'pymysql', 'cryptography']
#     # packages -  packages name
#     packages2 = ['np', 'pd', 'sp', 'sk']
#     # packages2 - packages export name
#     for i in range(len(packages)):
#         # get packages length
#         print(f"Loading {packages[i]}...")
#         # echo packages name
#         os.system(f"pip install {packages[i]}")
#         # excute command : pip install {packages[i]}

def connect(ex, type):
    # example server connection method
    import numpy as np
    import pymysql
    import pymysql.cursors
    import pandas as pd
    import warnings
    warnings.filterwarnings('ignore') 
    # bypass warning (hide server address)
    # package import & on try code
    # database connection & excute querry
    print(f"예제를 불러오고 있습니다\n예제 : {ex}",',', f"출력 타입 : {type}")
    connect = pymysql.connect(host='database.arisia.space', user='view', password='example', db='example', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connect.cursor()
    # trying querry
    try:
        query = f"SELECT * FROM {ex}"
        cur.execute(query)
    except:
        print("예제가 존재하지 않습니다. 예제 번호를 확인하세요")
    connect.commit()
    connect.close()
    # same at connectdb method
    if type == "dataframe" or type == "df":
        print("데이터프레임 타입으로 반환합니다.")
        df = pd.DataFrame(cur.fetchall())
        return df
    elif type == "numpy" or type == "np":
        print("넘파이 타입으로 반환합니다.")
        df = pd.DataFrame(cur.fetchall())
        return np.array(df)
    else:
        print("타입이 잘못되었습니다. 문법을 확인하세요")
        # type error : return Null
        return None
        
def connectdb(ip, port, userid, userpw, database, type, querry):
    # custom database connection method
    try:
        # package import & on try code
        import numpy as np
        import pymysql
        import pymysql.cursors
        import pandas as pd
        # db connection, transfer user input for string & int
        connect = pymysql.connect(host=str(ip), port=int(port), user=str(userid), password=str(userpw), db=str(database),
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cur = connect.cursor()
        # set querry method
        query = str(querry)
        # excute querry for database
        cur.execute(query)
        # connection Close
        connect.commit()
        connect.close()
        # parser user type input
        if type == "dataframe" or type == "df":
            # type = dataframe
            print("데이터프레임 타입으로 반환합니다.")
            df = pd.DataFrame(cur.fetchall())
            # trasfer to dataframe & return dataframe
            return df
        elif type == "numpy" or type == "np":
            # type = numpy
            print("넘파이 타입으로 반환합니다.")
            df = pd.DataFrame(cur.fetchall())
            # echo & trabsfer to df & return numpy array
            return np.array(df)
        else:
            print("타입이 잘못되었습니다. 문법을 확인하세요")
            # error : type is not dataframe or numpy, return Null
            return None
    except:
        print("데이터베이스 연결에 실패하였습니다. 접속 가능 여부를 확인하세요")
        # error : fail to connect database, return Null
        return None
    
def example():
    # show help. example
    print("예제를 불러옵니다.","\n","예제 1")
    print('connect("example1", "numpy")')
    print('connect("example1", "dataframe")')
    print("예제 2")    
    print("connectdb('server.url', 3306, 'view', 'example', 'example', 'dataframe', 'SELECT * FROM example1')")
    print("connectdb('server.url', 3306, 'view', 'example', 'example', 'numpy', 'SELECT * FROM example1')")

def help():
    # show help
    print("자세한 도움말은 깃허브와 책의 도움 페이지를 참조하세요")

def version():
    # display version
    import __init__ as ver
    print(ver.__version__)
    
# connect("test1", "numpy")