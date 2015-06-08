#Tools to connect to SQL Server and get data from table persona
__author__ = 'erick_sis'
import pymssql

class dotnetServer:
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
        cnn = pymssql.connect(self._host, self._dbuser, self._dbpassword, self._dbname)

        pass

    def getMaxId(self):
        #returndata = 0
        cnn = pymssql.connect(self._host, self._dbuser, self._dbpassword, self._dbname)
        cursor = cnn.cursor()
        cursor.execute('select max(idperson) from persona')
        row = cursor.fetchone()
        returndata = row[0]
        cnn.close()
        return returndata

    def getNewUsers(self):
        shortCede = self._sede[2:]
        strDate = str(self._year_filter) + '-' + str(self._month_filter) + '-' + str(self._dayfilter)

        strQuery = "select top 100 " \
                    "IDPerson, "\
                    "isnull(DUI,''), "\
                    "isnull(Nombre,''), "\
                    "isnull(Nombre2,''), "\
                    "isnull(Apellido,''), "\
                    "isnull(Apellido2,''), "\
                    "isnull(Direccion,''), "\
                    "isnull(Telefono,'0') Telefono, "\
                    "isnull(Celular,'0') Celular, "\
                    "FechaCreac, "\
                    + "'" + self._sede + "', "\
                    "isnull(Ocupacion,''), "\
                    "isnull(EstadoCivil,''), "\
                    "isnull(Discapacidad,''), "\
                    "isnull(SituEmpleo,''), "\
                    "isnull(Departamento,''), "\
                    "isnull(Municipio,''), "\
                    "isnull(CantonCas,''), "\
                    "isnull(Caserio,''), "\
                    "isnull(GradoEstudio,'') nivel_academico, "\
                    "isnull(LeerEscribir,'') nivel_alfabetizacion, "\
                    "dateadd(year, cast(isnull(EdadEx,18) as int)*-1 ,fechacreac) fecha_nacimiento, "\
                    "0 num_hijos, "\
                    "'' NIT, "\
                    "0 embarazada, "\
                    +"'" + shortCede +"'"+ " +'-'" + "+ replicate('0', 6- len(ltrim(str( IDPerson))) ) + ltrim(str( IDPerson)), "\
                    "'     ' zona "\
                    "from persona " \
                    "where " \
                    "fechacreac >= '" + strDate + "'"  + \
                    " and IDPerson > " + str(self._lastid) + " "\
                    " order by IDPerson "

        print(strQuery)

        cnn = pymssql.connect(self._host, self._dbuser, self._dbpassword, self._dbname)
        cursor = cnn.cursor()
        cursor.execute(strQuery)
        row = cursor.fetchone()
        rows = cursor.fetchall()
        print('esta es la nueva salida')
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print(row[4])
        print(row[5])
        print(row[6])
        print(row[7])
        print(row[8])
        print(row[9])
        print(row[10])
        print(row[11])
        print(row[12])
        print(row[13])
        print(row[14])
        print(row[15])
        print(row[16])
        print(row[17])
        print(row[18])
        print(row[19])
        print(row[20])
        print(row[21])
        print(row[22])
        print(row[23])
        print(row[24])
        print(row[25])
        print(row[26])
        print("Fin de impresion de row")
        cnn.close()
        return rows

class dotnetUsuaria:
    def __init__(self):
        self._id_usuaria = 1
        self._name1 = ""
        self._name2 = ""
        self._name3 =""

    @property
    def name3(self):
        return self._name3

    @name3.setter
    def name3(self, value):
        self._name3 = value

    @property
    def name2(self: str):
        return self._name2

    @name2.setter
    def name2(self, value: str):
        self._name2 = value


    @property
    def name1(self):
        return self._name1

    @name1.setter
    def name1(self, value):
        self._name1 = value

    @property
    def id_usuaria(self):
        return self._id_usuaria

    @id_usuaria.setter
    def id_usuaria(self, value):
        self._id_usuaria = value

    def process_usuaria(self):
        pass





dot = dotnetUsuaria()

dot.id_usuaria = 1
dot.name1 = "ana"
dot.name2 = 5
