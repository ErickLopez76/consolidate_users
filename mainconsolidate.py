__author__ = 'Erick Lopez'
import consolidatetools

#c = consolidatetools.consolidate()

#print(c.getcnnparam())


#Get list of servers
consolidate = consolidatetools.Consolidate()

servers = consolidate.getrowAllServers()
for server in servers:
    print("before server 5")
    print(server[5])
    consolidate.processUsers(server[0], server[1], server[2], server[3], server[6], server[5],server[7],server[8],server[9],server[10])
    pass
    #process every line the next desiction is in tools
        #for every server print sede
        #if .net
            #getdata_from_dotnet
        #else
            #getdata_from_simujer