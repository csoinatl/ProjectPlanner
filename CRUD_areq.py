import pymysql
conn = pymysql.connect(host='localhost',user='root',password = 'secret_root_password', db='swe6633db')
sqlCursor = conn.cursor()


##------------------------
def addrequirements(pid,rid,reqtext,rtype):
     sqlCursor.execute("INSERT INTO requirements VALUES(" + str(pid) + "," + str(rid) + ",\'" + reqtext + "\'," + str(rtype)+")")
     print ('done')
     return

##------------------------
def addprojectteam(pid, tid, tmname, desig):
     "Add a new requirement to the projectteam table"
    sqlCursor.execute("INSERT INTO projectTeam VALUES(" + str(pid) + "," + str(tid) + ",\'" + tmname + "\'," + str(desig)+")")
     print ('done')
     return

##------------------------
def addprojects(pid, pname, pdesc, pown, pteam, sdate, edate):
     "Add a new requirement to the projects table"
     sqlCursor.execute("INSERT INTO projects VALUES(" + str(pid) + "," + pname + ",\'" + pdesc + "\',\'" + pown+ "\',\'" +pteam+ "\',\'" +sdate+ "\',\'" +edate+"\')")
     print ('done')
     return

##------------------------
def addprojectrisks(pid, rid, rdesc, rpri, rstat):
     "Add a new requirement to the projectrisks table"
    sqlCursor.execute("INSERT INTO projectRisks VALUES(" + str(pid) + "," + str(rid) + ",\'" + rdesc + "\'," + str(rpri)+ ","+ rstat +")")
     print ('done')
     return

##------------------------
def addprojecthours(pid, rid, tid, ahr, deshr, devhr, thr, mhr):
     "Add a new requirement to the projecthours table"
    sqlCursor.execute("INSERT INTO projectHours VALUES(" + str(pid) + "," + str(rid) + "," + str(tid) + "," + str(ahr)+"," +str(deshr)+","+str(devhr)+","+str(thr)+","+str(mhr)+")")
     print ('done')
     return

##------------------------
def getrequirements(pid):
     "Retrieve the requirements for a given project ID"

     query = 'SELECT * FROM requirements'
     sqlCursor.execute(query);
     print ('Parameters for getrequirements function: %d', pid)
     return

##------------------------
def setrequirements(pid, rid, reqtext, rtype):
     "Update the requirements for a given project ID"

     query = '"""UPDATE requirements SET requirements=%s, reqType=%d WHERE projectID = pid and fReqID = rid""", (reqtext, rtype))'
     sqlCursor.execute(query);
     conn.commit()
     print ('Parameters for setrequirements function: %d - %d - %s - %d', pid, rid, reqtext, rtype)
     print ('query: %s', query)
     return

##------------------------
def delrequirements(pid, rid):

    sqlCursor.execute("DELETE FROM requirements WHERE projectID =" +str(pid)+ " and reqID = "+str(rid))
    conn.commit()
    print('done')
    return


##------------------------
def delprojectteam(pid, tid):

    sqlCursor.execute("DELETE FROM projectteam WHERE projectID =" +str(pid)+ " and reqID = "+str(tid))
    conn.commit()
    print('done')
    return


##------------------------
def delprojects(pid):

    sqlCursor.execute("DELETE FROM projects WHERE projectID =" +str(pid))
    conn.commit()
    print('done')
    return


##------------------------
def delprojectrisks(pid, rid):

   sqlCursor.execute("DELETE FROM projectrisks WHERE projectID =" +str(pid)+ " and riskID = "+str(rid))
    conn.commit()
    print('done')
    return


##------------------------
def delprojecthours(pid, rid, tid):

    sqlCursor.execute("DELETE FROM projecthours WHERE projectID =" +str(pid)+ " and reqID = " +str(rid)+ " and teamMemberID = " +str(tid))
    conn.commit()
    print('done')
    return






##test data
addrequirements( 1,1,'This is functional requirement text', 1 );
##getrequirements( 1 );
##setrequirements( 1,1,'This is changed functional requirement text', 1 );
#delrequirements(1,2);

