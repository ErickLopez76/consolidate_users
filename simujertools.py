__author__ = 'erick_sis'
#import mysql
#import mysql.connector
import pymysql
from contextlib import closing


class simujerServer:
    def __init__(self):
        self._host = ""
        self._dbuser = ""
        self._dbpassword = ""
        self._sede = ""
        self._dbname = ""
        self._lastid = 0
        self._year_filter = 0
        self._month_filter = 0
        self._dayfilter = 0

    @property
    def year_filter(self):
        return self._year_filter

    @year_filter.setter
    def year_filter(self, value):
        self._year_filter = value

    @property
    def month_filter(self):
        return self._month_filter

    @month_filter.setter
    def month_filter(self, value):
        self._month_filter = value

    @property
    def dayfilter(self):
        return self._dayfilter

    @dayfilter.setter
    def dayfilter(self, value):
        self._dayfilter = value

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

    @property
    def dbuser(self):
        return self._dbuser

    @dbuser.setter
    def dbuser(self, value):
        self._dbuser = value

    @property
    def dbpassword(self):
        return self._dbpassword

    @dbpassword.setter
    def dbpassword(self, value):
        self._dbpassword = value

    @property
    def sede(self):
        return self._sede

    @sede.setter
    def sede(self, value):
        self._sede = value

    @property
    def dbname(self):
        return self._dbname

    @dbname.setter
    def dbname(self, value):
        self._dbname = value

    @property
    def lastid(self):
        return self._lastid

    @lastid.setter
    def lastid(self, value):
        self._lastid = value
    #test
    def nothing(self):
        pass

    def process_users(self):
        cnn = pymysql.connect (host=self._host, user=self._dbuser, password=self._dbpassword,database=self._dbname)

        pass

    def getMaxId(self):
        print("start getMaxId")
        returndata = 0
        cnn = pymysql.connect (host=self._host, user=self._dbuser, password=self._dbpassword,database=self._dbname)
        cursor = cnn.cursor()
        cursor.execute('select max(id_usuaria) from cm_usuaria')
        row = cursor.fetchone()
        returndata = row[0]
        print("end getMaxId")
        return returndata

    def delete_temp_table(self):
        print("start delete_temp_table")
        cnn = pymysql.connect (host=self._host, user=self._dbuser, password=self._dbpassword,database=self._dbname)
        cursor = cnn.cursor()
        try:
            cursor.execute('drop table stat_cm_usuaria')
            cnn.commit()
            cnn.close()
        except:
            cnn.close()
            pass
        print("end delete_temp_table")
        return None

    def recreate_temp_table(self):
        print("start recreate_temp_table")
        cnn = pymysql.connect (host=self._host, user=self._dbuser, password=self._dbpassword,database=self._dbname )
        cursor = cnn.cursor()

        cursor.execute("call crea_temp_stat_usuaria(" + str(self._lastid) + ")")
        cnn.commit()
        cnn.close()
        print("end recreate_temp_table")
        return None


    def getNewUsers(self):
        print("start getNewUsers")
        shortCede = self._sede[2:]
        strDate = str(self._year_filter) + '-' + str(self._month_filter) + '-' + str(self._dayfilter)

        #Borrar Tabla Temporal
        self.delete_temp_table()
        #Ejecutar procedimiento para re-crear tabla
        self.recreate_temp_table()
        #Consultar resultado

        cnn = pymysql.connect (host=self._host, user=self._dbuser, password=self._dbpassword,database=self._dbname, connect_timeout=30000)
        with closing( cnn.cursor() ) as cur:
            #cursor = cnn.cursor()
            cur.execute("select * from v_stat_usuaria2 order by id_usuaria limit 100")
            rows = cur.fetchall()
        cnn.close()
        print("end getNewUsers")
        return rows

