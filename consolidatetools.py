#Cosolidatetools.py
#Class with tools utils.

__author__ = 'Erick Lopez'
import configparser
import dotnettools
import simujertools
import psycopg2
import time

class Consolidate:

    def getcnnparam(self):
        cnf = configparser.ConfigParser()
        cnf.read('config.ini')

        Host = cnf.get('PostgresServers','host')
        User = cnf.get('PostgresServers','dbsuser')
        Password = cnf.get('PostgresServers','dbspassword')
        DbName = cnf.get('PostgresServers', 'dbname')
        return Host, User,Password, DbName
        
    def getrowAllServers(self):
        lhost, luser, lpassword, ldb = self.getcnnparam()
        cnn = psycopg2.connect("dbname=" + ldb + " host=" + lhost + " user=" + luser + " password=" + lpassword)
        cur = cnn.cursor()

        cur.execute("select * from cnn_servers where active = true order by last_update")
        rows = cur.fetchall()
        #print(cur.rowcount)
        row = cur.fetchone()

        #for r in rows:
        #    print(r[0])
        #    print(r[1])
        cnn.close()
        return rows

    def getUsersDotnet(self):
        #data
        pass

    def getUsersSimujer(self):
        #data
        pass

    def Add_stat_usuaria2(self,params):
        lhost, luser, lpassword, ldb = self.getcnnparam()
        cnn = psycopg2.connect("dbname=" + ldb + " host=" + lhost + " user=" + luser + " password=" + lpassword)
        cur = cnn.cursor()
        cur.callproc("insert_stat_paersona",params)
        cnn.commit()
        #cur.callproc("insert_stat_paersona",params[0],str(params[1]),str(params[2]),str(params[3]),str(params[4]),str(params[5]),str(params[6]),str(params[7]),str(params[8]), params[9],str(params[10]),str(params[11]),str(params[12]),str(params[13]),str(params[14]),str(params[15]),str(params[16]),str(params[17]),str(params[18]),str(params[19]),str(params[20]),params[21],params[22],str(params[23]),params[24],str(params[25]),str(params[26]) )


    def Add_stat_usuaria(self, \
                        pdotnet_idperson, \
                        pdui, \
                        pnombre1, \
                        pnombre2, \
                        papellido1, \
                        papellido2, \
                        pdireccion, \
                        ptelefono, \
                        pcelular, \
                        pfech_crea, \
                        psede, \
                        pocupacion, \
                        pestadocivil, \
                        pdiscapacidad, \
                        psituacion_empleo, \
                        pdepartamento, \
                        pmunicipio, \
                        pcantoncas, \
                        pcaserio, \
                        pnivel_academico, \
                        pnivel_alfabetizacion, \
                        pfecha_nacimiento, \
                        pnum_hijos, \
                        pnit, \
                        pembarazada, \
                        pid_expediente, \
                        pzona
                         ):
        if pcelular is None:
            pcelular = "0"

        print("pdotnet_id")
        print(pdotnet_idperson)
        #print(pfecha_nacimiento)
        #print(pfecha_nacimiento.strftime('%Y-%m-%d'))
        strQuery = "select insert_stat_persona ( " + \
        str(pdotnet_idperson) + ", "\
        "'" + pdui + "', "\
        "'" + pnombre1 + "', "\
        "'" + pnombre2 + "', "\
        "'" + papellido1 + "', "\
        "'" + papellido2 + "', "\
        "'" + pdireccion + "', "\
        "'" + ptelefono + "', "\
        "'" + pcelular + "', "\
        "'" + pfech_crea.strftime('%Y-%m-%d %H:%M:%S') + "', "\
        "'" + psede + "', "\
        "'" + pocupacion + "', "\
        "'" + pestadocivil + "', "\
        "'" + pdiscapacidad + "', "\
        "'" + psituacion_empleo + "', "\
        "'" + pdepartamento + "', "\
        "'" + pmunicipio + "', "\
        "'" + pcantoncas + "', "\
        "'" + pcaserio + "', "\
        "'" + pnivel_academico + "', "\
        "'" + pnivel_alfabetizacion + "', "\
        "'" + pfecha_nacimiento.strftime('%Y-%m-%d %H:%M:%S') + "', "\
        "'" + str(pnum_hijos) + "', "\
        "'" + pnit + "', "\
        "'" + str(pembarazada) + "', "\
        "'" + pid_expediente + "', "\
        "'" + pzona + "' )"

        #print(strQuery)

        lhost, luser, lpassword, ldb = self.getcnnparam()
        cnn = psycopg2.connect("dbname=" + ldb + " host=" + lhost + " user=" + luser + " password=" + lpassword)
        cur = cnn.cursor()
        cur.execute(strQuery)
        cur.execute('update cnn_servers set lastid = ' + str(pdotnet_idperson) + ", last_update = '" + time.strftime("%Y-%m-%d %H:%M:%S")  + "' where sede = '" + psede + "'")
        cnn.commit()
        #r = cur.fetchone()
        cur.close()
        return None


    def processUsers(self,stype,host,user,password,dbname,sede, lastid,yearfilter,monthfilter,dayfilter):
        if stype == ".net":
            process_dotnet = dotnettools.dotnetServer()
            process_dotnet.host = host
            process_dotnet.dbuser = user
            process_dotnet.dbpassword = password
            process_dotnet.dbname = dbname
            process_dotnet.sede = sede
            process_dotnet.lastid = lastid
            process_dotnet.year_filter = yearfilter
            process_dotnet.month_filter = monthfilter
            process_dotnet.dayfilter = dayfilter

            if lastid < process_dotnet.getMaxId():
                #se ejecuta la actualización
                netusers = process_dotnet.getNewUsers()
                for netuser in netusers:
                    self.Add_stat_usuaria(netuser[0],netuser[1], netuser[2],netuser[3],netuser[4],netuser[5],netuser[6], netuser[7],netuser[8],netuser[9],netuser[10],netuser[11],netuser[12],netuser[13],netuser[14],netuser[15],netuser[16],netuser[17],netuser[18],netuser[19],netuser[20],netuser[21],netuser[22],netuser[23], netuser[24],netuser[25],netuser[26])
                    #self.Add_stat_usuaria2(netuser)
                    pass
        else:
            process_simujer = simujertools.simujerServer()
            process_simujer.host = host
            process_simujer.dbuser = user
            process_simujer.dbpassword = password
            process_simujer.dbname = dbname
            process_simujer.sede = sede
            process_simujer.lastid = lastid
            process_simujer.year_filter = yearfilter
            process_simujer.month_filter = monthfilter
            process_simujer.dayfilter = dayfilter

            if lastid < process_simujer.getMaxId():
                simujerusers = process_simujer.getNewUsers()
                for simujeruser in simujerusers:
                    self.Add_stat_usuaria(simujeruser[0], simujeruser[1], simujeruser[2],simujeruser[3],simujeruser[4],simujeruser[5],simujeruser[6],simujeruser[7],simujeruser[8],simujeruser[9],simujeruser[10],simujeruser[11],simujeruser[12],simujeruser[13],simujeruser[14],simujeruser[28],simujeruser[27],"",simujeruser[16],simujeruser[17],simujeruser[18],simujeruser[19],simujeruser[20],simujeruser[21],simujeruser[22],simujeruser[23],"")
                    pass
            pass
            #getUsersSimujer()



#ca = Consolidate()
#r = ca.getrowAllServers()
#print('estra es la r')
#print(r[0])

#ca.processUsers('.net', '10.20.35.12', 'sa', '123','WCity','CMLC',0)

#print(ca.getcnnparam())
#print(ca.Host)
#print("era host")
#print(ca.getrowAllServers())