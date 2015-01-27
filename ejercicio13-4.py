fich=open("/etc/passwd","r");
data = fich.readlines();
for user in data:
    print user.split(":")[0] + " shell: " + user.split(":")[-1]
print "Total users: " + str(len(data))
