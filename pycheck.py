import dns.resolver, requests , sys


#This stuff is just to make the text look pretty. If you want to know how this works lookup ANSI escape sequences :)
#########################################
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
#########################################



flag = 0

#The ip address we are using from arguments
ip = sys.argv[1]

#reverse ip for dns query
revip = '.'.join(reversed(ip.split('.')))

#List of black lists we want to check

bList = ["b.barracudacentral.org","bl.mailspike.net","psbl.surriel.com","cbl.abuseat.org",
"sbl-xbl-spamhaus.org","zen.spamhaus.org","bl.spamcop.net","ubl.unsubscore.com","dnsbl.sorbs.net","spam.dnsbl.sorbs.net"]

for ls in (bList):
        try:
            resolver = dns.resolver.Resolver()
            query = revip + '.' + ls
            a_record = resolver.query(query,"A")
            print ("LISTED ON " + ls)
            flag = 1
        except dns.resolver.NXDOMAIN:
            print ("NOT LISTED " + ls)

sendns = "query.senderbase.org"

try:
    resolver = dns.resolver.Resolver()
    query = revip + '.' + sendns
    txt_record = resolver.query(query,"TXT")
    print (txt_record[0])
    flag = 1
except dns.resolver.NXDOMAIN:
    print (sendns)


if (flag == 0):
    print (bcolors.OKBLUE + "IP IS CLEAN :)" + bcolors.ENDC)
