import pymysql
conn = pymysql.connect(host='localhost',user='root',password = 'secret_root_password', db='swe6633db')
sqlCursor = conn.cursor()


##------------------------
## Functional Requirements
##------------------------
def addrequirements(pid, rid, reqtext, rtype):
     "Add a new requirement to the requirements table"
     add_req = ("INSERT INTO reqirements "
           "(projectID, reqID, requirements, reqType"
           "VALUES %d, %d, %s, %d)")
     data_req = (pid, rid, reqtext, rtype)

     ## Insert new requirement
     sqlCursor.execute(add_req, data_req);
     conn.close()
     print ('Parameters for addrequirements function: %d - %d - %s - %d', pid, rid, reqtext, rtype)
     print ('query: %s%s', add_req, data_req)
     return
    ##------------------------

#------------------------
def getrequirements(pid):
     "Retrieve the requirements for a given project ID"

     query = 'SELECT * FROM requirements'
     sqlCursor.execute(query);
     print ('Parameters for getrequirements function: %d', pid)
     return

#------------------------
def setrequirements(pid, rid, reqtext, rtype):
     "Update the requirements for a given project ID"

     query = '"""UPDATE requirements SET requirements=%s, reqType=%d WHERE projectID = pid and fReqID = rid""", (reqtext, rtype))'
     sqlCursor.execute(query);
     conn.commit()
     print ('Parameters for setrequirements function: %d - %d - %s - %d', pid, rid, reqtext, rtype)
     print ('query: %s', query)
     return

#------------------------
def delrequirements(pid, rid):
     "Delete the requirements for a given project ID"
#     db_config = read_db_config()

     query = "DELETE FROM requirements WHERE projectID = %d and reqID = %d"
     sqlCursor.execute(query, (pid, rid,))
     conn.commit()
     print ('Parameters for delrequirements function: %d - %d', pid, rid)
     print ('query: %s', query)
     return






##test data
##addrequirements( 1,1,'This is functional requirement text', 1 );
getrequirements( 1 );
##setrequirements( 1,1,'This is changed functional requirement text', 1 );
delrequirements( 1, 1 );

