__author__ = 'Erick Lopez'
import consolidatetools
import time
#c = consolidatetools.consolidate()

#print(c.getcnnparam())
print("iniciamos")
print(time.ctime())

#Get list of servers
consolidate = consolidatetools.Consolidate()

servers = consolidate.getrowAllServers()
for server in servers:
    print("Sede a ejecutar")
    print(server[5])
    print(time.ctime())
    consolidate.processUsers(server[0], server[1], server[2], server[3], server[6], server[5],server[7],server[8],server[9],server[10])
    print("Sede finalizada")
    print(time.ctime())

print("Fin de todos los procesos")
print(time.ctime())
    #process every line the next desiction is in tools
        #for every server print sede
        #if .net
            #getdata_from_dotnet
        #else
            #getdata_from_simujer