import pymysql
conn = pymysql.connect(host='localhost',user='root',password = 'secret_root_password', db='swe6633db')
sqlCursor = conn.cursor()


##------------------------
def addrequirements(pid, rid, reqtext, rtype):
     "Add a new requirement to the requirements table"
     add_req = ("INSERT INTO requirements "
           "(projectID, reqID, requirements, reqType)"
           "VALUES %d, %d, %s, %d)")
     data_req = (pid, rid, reqtext, rtype)

     ## Insert new requirement
     sqlCursor.execute(add_req, data_req);
     conn.commit()
     print ('Parameters for addrequirements function: %d - %d - %s - %d', pid, rid, reqtext, rtype)
     print ('query: %s%s', add_req, data_req)
     return
    ##------------------------

##------------------------
def addprojectteam(pid, tid, tmname, desig):
     "Add a new requirement to the projectteam table"
     add_req = ("INSERT INTO projectteam "
           "(projectID, teamMemberID, teamMemberName, designation)"
           "VALUES %d, %d, %s, %d)")
     data_req = (pid, rid, reqtext, rtype)

     ## Insert new Team Member
     sqlCursor.execute(add_req, data_req);
     conn.commit()
     print ('Parameters for addprojectteam function: %d - %d - %s - %d', pid, tid, tmname, desig)
     print ('query: %s%s', add_req, data_req)
     return
    ##------------------------

##------------------------
def addprojects(pid, pname, pdesc, pown, pteam, sdate, edate):
     "Add a new requirement to the projects table"
     add_req = ("INSERT INTO projects "
           "(projectID, projectName, projectDesc, projectOwner, projectTeam, startDate, endDate)"
           "VALUES %d, %s, %s, %s, %s, %s, %s)")
     data_req = (pid, pname, pdesc, pown, pteam, sdate, edate)

     ## Insert new projects
     sqlCursor.execute(add_req, data_req);
     conn.commit()
     print ('Parameters for addprojects function: %d - %s - %s - %s - %s - %s - %s', pid, pname, pdesc, pown, pteam, sdate, edate)
     print ('query: %s%s', add_req, data_req)
     return
    ##------------------------

##------------------------
def addprojectrisks(pid, rid, rdesc, rpri, rstat):
     "Add a new requirement to the projectrisks table"
     add_req = ("INSERT INTO projectrisks "
           "(projectID, projectName, projectDesc, projectOwner, projectTeam, startDate, endDate)"
           "VALUES %d, %d, %s, %d, %s)")
     data_req = (pid, rid, rdesc, rpri, rstat)

     ## Insert new projectrisks
     sqlCursor.execute(add_req, data_req);
     conn.commit()
     print ('Parameters for addprojectrisks function: %d - %d - %s - %d - %s', pid, rid, rdesc, rpri, rstat)
     print ('query: %s%s', add_req, data_req)
     return
    ##------------------------

##------------------------
def addprojecthours(pid, rid, tid, ahr, deshr, devhr, thr, mhr):
     "Add a new requirement to the projecthours table"
     add_req = ("INSERT INTO projecthours "
           "(projectID, projectName, projectDesc, projectOwner, projectTeam, startDate, endDate)"
           "VALUES %d, %d, %s, %d, %s)")
     data_req = (pid, rid, tid, ahr, deshr, devhr, thr, mhr)

     ## Insert new projecthours
     sqlCursor.execute(add_req, data_req);
     conn.commit()
     print ('Parameters for addprojecthours function: %d - %d - %d - %d - %d - %d - %d - %d', pid, rid, tid, ahr, deshr, devhr, thr, mhr)
     print ('query: %s%s', add_req, data_req)
     return
    ##------------------------

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

    sqlCursor.execute("DELETE FROM projectrisks WHERE projectID =" +str(pid)+ " and reqID = "+str(rid))
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

