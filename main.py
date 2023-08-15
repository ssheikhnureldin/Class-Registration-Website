from flask import Flask
from flask_mysqldb import MySQL
from flask import Flask, render_template, request, redirect, url_for, session
import MySQLdb.cursors
import re
from flask import Flask,session,render_template,request
import mysql.connector 

app = Flask('app')

app.secret_key=b'phase2-key'
d = mysql.connector.connect(
  host = "ec2-3-231-226-249.compute-1.amazonaws.com",
  user = "ssheikhnureldin",
  password = "seas",
  database = "phase2"
 )


# Intialize MySQL
#mysql = MySQL(app)
@app.route('/')
def homepage():
  # Render the homepage 
  return render_template("index.html")
##login 
@app.route('/login',methods=['GET', 'POST'])
def login():
  messgage =''
  print("test1")
  if request.method == 'POST':
   #and 'uname' in request.form and 'pword' in request.form:
    username = request.form["uname"]
    password = request.form["pword"]
    c=d.cursor()
    c.execute("SELECT * FROM user WHERE uname = %s AND pword = %s",(username, password),)
    results = c.fetchone()
    print(results)
    if results == None:
      return render_template("index.html",message = "Incorrect username/password: please try again.")
    elif (username == 'gradsec' and password == 'gradsec1'):
      c.execute("SELECT uname and pword FROM user WHERE uname = %s AND pword= %s",(username,password),)
      username = c.fetchone()
      session['loggedin'] = True
      session['id'] = username
      return render_template('gradsechome.html')
    elif (username == 'narahari' and password == 'narahari1'):
      c.execute("SELECT faculty_ID FROM faculty WHERE fname = %s AND lname= %s",(results[0],results[1]),)
      faculty_ID = c.fetchone()
      session['loggedin'] = True
      session['id'] = faculty_ID
      return render_template('facultyhome.html')
    elif (username == 'choi' and password == 'choi1'):
      c.execute("SELECT faculty_ID FROM faculty WHERE fname = %s AND lname= %s",(results[0],results[1]),)
      faculty_ID = c.fetchone()
      session['loggedin'] = True
      session['id'] = faculty_ID
      return render_template('facultyhome.html')
    elif len(results) !=0: 
      print("TEST1")
      c.execute("SELECT university_ID FROM student WHERE fname = %s AND lname = %s",(results[0],results[1]),)
      university_ID = c.fetchone()
      print(university_ID)
      print("TEST2")
      if university_ID != None:
        print(university_ID)
        print("TEST3")
        session['loggedin'] = True
        session['id'] = university_ID
        return render_template('home.html')
    #else:
     #c.execute("SELECT faculty_ID FROM faculty WHERE fname = %s AND lname = %s",(results[0],results[1]),)
     #print("TEST4")
      #faculty_ID = c.fetchone()
      #if len(faculty_ID) != 0:
        #session['loggedin'] = True
        #session['id'] = faculty_ID;
        #return render_template('facultyhome.html')
    else:
      return render_template("index.html",message = "Incorrect username/password: please try again.")
    c.close()
  else:
      return render_template("index.html",message = "Incorrect username/password: please try again.")
  return render_template('index.html')


## welcome the user
@app.route ('/user/')
def user_handler():
    return "Welcome %s" % session['uname']


# http://localhost:5000/python/logout - this will be the logout page
@app.route('/pythonlogin/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('uname', None)
   # Redirect to login page
   return redirect(url_for('login'))



# http://localhost:5000/pythinlogin/profile - this will be the profile page, only accessible for loggedin users
@app.route('/pythonlogin/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


#function for returning transcript table
@app.route('/pythonlogin/transcript', methods=['GET', 'POST'])
def transcript():
    # Output message if something goes wrong...
    msg = ''
     # Check if user is loggedin
    if session['loggedin'] == True:
      print(session['id'])
    #if button pressed to view transcript then show this page 
      print("hello")
      c=d.cursor()
      print("hello1")
      c.execute('SELECT * FROM testuserTranscript WHERE university_ID = %s', (session['id']),)
      transcript = c.fetchall()
      c.execute('SELECT * FROM student WHERE university_ID = %s', (session['id']),)
      result = c.fetchone()
      print(transcript)
      if len(transcript) !=0:
        return render_template('transcript.html',transcript = transcript,degree=result[5],gpa = result[7])
    # Show transcript page 
    return render_template('transcript.html')


#function for returning student home table
@app.route('/pythonlogin/studenthome', methods=['GET', 'POST'])
def studenthome():
  # Check if user is loggedin
  #if 'loggedin' in session:
  #if button pressed to view transcript then show this page 
  if session['loggedin'] == True:
      # Check if account exists using MySQL
      print(session['id'])
      c=d.cursor()
      print(session['id'])
      c.execute('SELECT * FROM student WHERE university_ID = %s', (session['id']),)
      result = c.fetchone()
      #display student info
      return render_template('studenthome.html', fname = result[1],lname = result[2], address = result[3],phonenum = result[4], degree = result[5], gpa = result[7])

  print("false")
  return render_template('studenthome.html')

#function for returning transcript table
@app.route('/pythonlogin/registerforclasses', methods=['GET', 'POST'])
def registerforclasses():
    # Output message if something goes wrong...
  msg = ''
  if session['loggedin'] == True:
    if request.method == 'POST':
        dept = request.form['dept']
        course_num = request.form['course_num']
        # Check if course exists using MySQL
        c=d.cursor(buffered = True)
        c.execute('SELECT * FROM schedule WHERE dept = %s AND course_num = %s', (dept, course_num),)
        result = c.fetchall()
        #d.commit()
        results = result[0]
        print(results)
        c.execute('SELECT * FROM CourseCatalog WHERE dept = %s AND course_num = %s', (dept, course_num),)
        info = c.fetchone();
        print(info)
        prereq_1 = info[5]
        prereq_2 = info[6]
        if results == None:
          return render_template('registerforclasses.html',message = "course not found")
        
        elif len(results) !=0:
          ID = session['id']
          print(results)
          grade = 'IP'
          #check prereqs
          #c.execute('SELECT prereq_1, prereq_2 FROM schedule WHERE dept = %s AND course_num = %s', (dept, course_num),)
          sql = "INSERT INTO verifyCourses(dept,course_num,course_name,credits,prereq_1,prereq_2,university_ID,grade,day,time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
          val = (results[1],results[2],results[3],results[4],prereq_1,prereq_2,ID[0],grade,results[5],results[6])
          print(val)
          c.execute(sql, val) 
          d.commit()
          
          print(val)
          return render_template('registerforclasses.html',message = "your course has been submitted for review")
        else:
          return render_template('registerforclasses.html', message = 'course does not exist, please try again')
  return render_template('registerforclasses.html')


#function for changing first name
@app.route('/pythonlogin/changeinfo', methods=['GET', 'POST'])
def changeinfo():
    # Output message if something goes wrong...
    msg = ''
    return render_template('changeinfo.html')


#function for changing first name
@app.route('/pythonlogin/changefname', methods=['GET', 'POST'])
def changefname():
    # Output message if something goes wrong...
    msg = ''

    if request.method == 'POST':
      fname = request.form['fname']
      if session['loggedin'] == True:
        c=d.cursor()
        print("test1")
        c.execute('SELECT fname FROM student WHERE university_ID = %s',(session['id']),)
        oldname = c.fetchone();
        print("test2")
        if len(oldname) !=0:
          print("test3")
          sql = "UPDATE student SET fname = %s WHERE fname = %s"
          val = (fname,oldname[0])
          print(val)

          c.execute(sql, val,)   
          d.commit()
          sql = "UPDATE user SET fname = %s WHERE fname = %s"
          val = (fname,oldname[0])
          c.execute(sql,val,)
          d.commit()      
          c.execute('SELECT fname FROM student WHERE university_ID = %s',(session['id']),)
          result = c.fetchone()
          d.commit() 
          return render_template('changeinfo.html',fname = result)
        else:
          return render_template('changeinfo.html', fname = 'please try again')

    return render_template('changeinfo.html')

#function for changing last name
@app.route('/pythonlogin/changelname', methods=['GET', 'POST'])
def changelname():
    # Output message if something goes wrong...
    msg = ''
    if request.method == 'POST':
      lname = request.form['lname']
      if session['loggedin'] == True:
        c=d.cursor()
        c.execute('SELECT lname FROM student WHERE university_ID = %s',(session['id']),)
        oldname = c.fetchone();
        if len(oldname) !=0:
          sql = "UPDATE student SET lname = %s WHERE lname = %s"
          val = (lname,oldname[0])

          c.execute(sql, val,)  
          d.commit()
          sql = "UPDATE user SET lname = %s WHERE lname = %s"
          val = (lname,oldname[0])
          c.execute(sql,val,)
          d.commit()         
          c.execute('SELECT lname FROM student WHERE university_ID = %s',(session['id']),)
          result = c.fetchone()
          d.commit() 
          return render_template('changeinfo.html',lname = result)
        else:
          return render_template('changeinfo.html', lname = 'please try again')

    return render_template('changeinfo.html')


#function for changing first name
@app.route('/pythonlogin/changefacultyinfo', methods=['GET', 'POST'])
def changefacultyinfo():
    # Output message if something goes wrong...
    msg = ''
    return render_template('changefacultyinfo.html')


#function for changing first name
@app.route('/pythonlogin/changefacultyfname', methods=['GET', 'POST'])
def changefacultyfname():
    # Output message if something goes wrong...
    msg = ''

    if request.method == 'POST':
      fname = request.form['fname']
      if session['loggedin'] == True:
        c=d.cursor()
        print("test1")
        c.execute('SELECT fname FROM faculty WHERE faculty_ID = %s',(session['id']),)
        oldname = c.fetchone();
        print("test2")
        if len(oldname) !=0:
          print("test3")
          sql = "UPDATE faculty SET fname = %s WHERE fname = %s"
          val = (fname,oldname[0])
          print(val)

          c.execute(sql, val,)   
          d.commit()
          sql = "UPDATE user SET fname = %s WHERE fname = %s"
          val = (fname,oldname[0])
          c.execute(sql,val,)
          d.commit()      
          c.execute('SELECT fname FROM faculty WHERE faculty_ID = %s',(session['id']),)
          result = c.fetchone()
          d.commit() 
          return render_template('changefacultyinfo.html',fname = result)
        else:
          return render_template('changefacultyinfo.html', fname = 'please try again')

    return render_template('changefacultyinfo.html')

#function for changing last name
@app.route('/pythonlogin/changefacultylname', methods=['GET', 'POST'])
def changefacultylname():
    # Output message if something goes wrong...
    msg = ''
    if request.method == 'POST':
      lname = request.form['lname']
      if session['loggedin'] == True:
        c=d.cursor()
        c.execute('SELECT lname FROM faculty WHERE faculty_ID = %s',(session['id']),)
        oldname = c.fetchone();
        if len(oldname) !=0:
          sql = "UPDATE faculty SET lname = %s WHERE lname = %s"
          val = (lname,oldname[0])

          c.execute(sql, val,)  
          d.commit()
          sql = "UPDATE user SET lname = %s WHERE lname = %s"
          val = (lname,oldname[0])
          c.execute(sql,val,)
          d.commit()         
          c.execute('SELECT lname FROM faculty WHERE faculty_ID = %s',(session['id']),)
          result = c.fetchone()
          d.commit() 
          return render_template('changefacultyinfo.html',lname = result)
        else:
          return render_template('changefacultyinfo.html', lname = 'please try again')

    return render_template('changefacultyinfo.html')


#function for changing last name
@app.route('/pythonlogin/changeaddress', methods=['GET', 'POST'])
def changeaddress():
    # Output message if something goes wrong...
    msg = ''
    if request.method == 'POST':
      address = request.form['address']
      if session['loggedin'] == True:
        c=d.cursor()
        c.execute('SELECT address FROM student WHERE university_ID = %s',(session['id']),)
        oldname = c.fetchone();
        if len(oldname) !=0:
          sql = "UPDATE student SET address = %s WHERE address = %s"
          val = (address,oldname[0])

          c.execute(sql, val,)         
          c.execute('SELECT address FROM student WHERE university_ID = %s',(session['id']),)
          result = c.fetchone()
          d.commit() 
          return render_template('changeinfo.html',address = result)
        else:
          return render_template('changeinfo.html', address = 'please try again')

    return render_template('changeinfo.html')

#function for changing first name
@app.route('/pythonlogin/changephonenum', methods=['GET', 'POST'])
def changephonenum():
    # Output message if something goes wrong...
    msg = ''

    if request.method == 'POST':
      phonenumber = request.form['phonenumber']
      if session['loggedin'] == True:
        c=d.cursor()
        c.execute('SELECT phone_num FROM student WHERE university_ID = %s',(session['id']),)
        oldname = c.fetchone();
        if len(oldname) !=0:
          sql = "UPDATE student SET phone_num = %s WHERE phone_num = %s"
          val = (phonenumber,oldname[0])
          

          c.execute(sql, val,)   
          d.commit()      
          c.execute('SELECT phone_num FROM student WHERE university_ID = %s',(session['id']),)
          result = c.fetchone()
          return render_template('changeinfo.html',phonenumber = result)
        else:
          return render_template('changeinfo.html', phonenumber = 'please try again')

    return render_template('changeinfo.html')

#function for search bar
@app.route('/pythonlogin/searchbar', methods=['GET', 'POST'])
def searchbar():
    # Output message if something goes wrong...
    msg = ''

    if request.method == 'POST':
        search = request.form['search']
        # Check if course exists using MySQL
        c=d.cursor()
        c.execute('SELECT * FROM schedule WHERE dept = %s OR course_num = %s OR course_name = %s OR credits = %s', (search, search, search, search),)
        result = c.fetchall()
        #if course exists print it out in table
        if len(result) !=0:
          return render_template('searchclasses.html', result = result)
        
        #course doesnt exist 
        else:
          return render_template('searchclasses.html', messageresult= 'no courses found, please try again')
  
    return render_template('searchclasses.html')
#function for changing grade
@app.route('/pythonlogin/changegrade', methods=['GET', 'POST'])
def changegrade():
    # Output message if something goes wrong...
    msg = ''
    if request.method == 'POST':
      grade = request.form['grade']
      search = request.form['search'] 
      if session['loggedin'] == True:
        c=d.cursor(buffered = True)
        print(grade)
        print(search)
        c.execute('SELECT grade FROM testuserTranscript WHERE university_ID = %s', (search,))
        oldgrade= c.fetchone();
        if oldgrade is not None:
          sql = "UPDATE testuserTranscript SET grade = %s WHERE grade= %s"
          val = (grade,oldgrade[0])

          c.execute(sql, val,)         
          c.execute('SELECT grade FROM testuserTranscript')
          result = c.fetchone()
          d.commit() 
          return render_template('changegrade.html',grade= result)
        else:
          return render_template('changegrade.html',grade = 'please try again')

    return render_template('changegrade.html')
#function for changing grade for submit
@app.route('/pythonlogin/submitchangegrade', methods=['GET', 'POST'])
def submitchangegrade():
   # Output message if something goes wrong...
    msg = ''
    if request.method == 'POST':
      grade = request.form['grade']
      search = request.form['search']
      #if session['loggedin'] == True: 
      c=d.cursor(buffered = True)
      #buffered cursor
      c.execute('SELECT grade FROM verifyCourses WHERE university_ID = %s', (search,))
      oldgrade= c.fetchone();
      if oldgrade is not None:
        sql = "UPDATE verifyCourses SET grade = %s WHERE grade= %s"
        val = (grade,oldgrade[0])
        d.commit()

        c.execute(sql, val,)         
        c.execute('SELECT grade FROM verifyCourses WHERE university_ID = %s', (search,))
        result = c.fetchone()
        d.commit() 
        return render_template('submitgrades.html',grade= result)
      else:
        return render_template('submitgrades.html',grade = 'please try again')

    return render_template('submitgrades.html')

#function for changing grade for submit gs
@app.route('/pythonlogin/gssubmitchangegrade', methods=['GET', 'POST'])
def gssubmitchangegrade():
   # Output message if something goes wrong...
    msg = ''
    if request.method == 'POST':
      grade = request.form['grade']
      search = request.form['search']
      #if session['loggedin'] == True: 
      c=d.cursor(buffered = True)
      #buffered cursor
      c.execute('SELECT grade FROM verifyCourses WHERE university_ID = %s', (search,))
      oldgrade= c.fetchone();
      if oldgrade is not None:
        sql = "UPDATE verifyCourses SET grade = %s WHERE grade= %s"
        val = (grade,oldgrade[0])
        d.commit()

        c.execute(sql, val,)         
        c.execute('SELECT grade FROM verifyCourses WHERE university_ID = %s', (search,))
        result = c.fetchone()
        d.commit() 
        return render_template('gssubmitgrades.html',grade= result)
      else:
        return render_template('gssubmitgrades.html',grade = 'please try again')

    return render_template('gssubmitgrades.html')

#prereq page
@app.route('/pythonlogin/prereq',methods=['GET', 'POST'])
def prereq():
  msg = ''
  if session['loggedin'] == True:
    if request.method == 'POST':
        dept = request.form['dept']
        course_num = request.form['course_num']
        grade = request.form['grade']
        # Check if course exists using MySQL
        c=d.cursor()
        c.execute('SELECT * FROM schedule WHERE dept = %s AND course_num = %s', (dept, course_num),)
        result = c.fetchall()
        #d.commit()
        results = result[0]
        print(results)
        c.execute('SELECT * FROM CourseCatalog WHERE dept = %s AND course_num = %s', (dept, course_num),)
        info = c.fetchone();
        prereq_1 = info[5]
        prereq_2 = info[6]
        
        if len(results) !=0:
          print("YE1")
          ID = session['id']
          print(results)
          sql = "INSERT INTO verifyCourses (dept,course_num,course_name,credits,prereq_1,prereq_2,university_ID,grade,day,time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
          val = (results[1],results[2],results[3],results[4],prereq_1,prereq_2,ID[0],grade,results[5],results[6])
          c.execute(sql, val) 
          d.commit()
          
          print(val)
          return render_template('prereq.html',message = "your course has been submitted for review")
        else:
          return render_template('prereq.html', message = 'course does not exist, please try again')
  return render_template('prereq.html')
#search for transcript by university ID
@app.route('/pythonlogin/searchtranscript', methods=['GET', 'POST'])
def searchtranscript():
  msg = ''
  if request.method == 'POST':
        search = request.form['search']
        # Check if course exists using MySQL
        c=d.cursor()
        c.execute('SELECT course, grade, semester_and_year, credit_hours, university_ID FROM testuserTranscript WHERE university_ID = %s', (search,))
        result = c.fetchall()
        #if course exists print it out in table
        if len(result) !=0:
          return render_template('changegrade.html', transcript = result)
          
        
        #course doesnt exist 
        else:
          return render_template('changegrade.html', messageresult= 'student not found, please enter valid universtiy ID')
  
  return render_template('changegrade.html')
#prereq page

#function for returning transcript table
@app.route('/pythonlogin/showdropcourse', methods=['GET', 'POST'])
def showdropcourse():
    # Output message if something goes wrong...
    msg = ''
    print("error 1 in showdropcourse")
     # Check if user is loggedin
    if session['loggedin'] == True:
      print(session['id'])
    #if button pressed to view currently enrolled courses then show this page 
      c=d.cursor()
      print("error 2 in showdropcourse")
      ID = session['id']
      print(ID[0])
      c.execute("SELECT * FROM verifyCourses WHERE university_ID = %s", (session['id']),)
      result = c.fetchall()
      
      d.commit()
      print("error 3 in showdropcourse")
      print(result)
      if len(result) !=0:
        return render_template('dropcourses.html',result = result)
    # Show transcript page 
    print("error 4 in showdropcourse")
    return render_template('dropcourses.html')

#function for returning transcript table
@app.route('/pythonlogin/dropcourse', methods=['GET', 'POST'])
def dropcourse():
    # Output message if something goes wrong...
    msg = ''
     # Check if user is loggedin
    if session['loggedin'] == True:
      print(request.form)
      if request.form != 'POST':
        c=d.cursor(buffered = True)
        print(session['id'])
        dept = request.form['dept']
        course_num = request.form['course_num']
        # Check if course exists using MySQL
        ID = session['id']
        c.execute('SELECT * FROM verifyCourses WHERE dept = %s AND course_num = %s AND university_ID = %s', (dept, course_num,ID[0]),)
        results = c.fetchone()
        d.commit()
        print(len(results))
        #if len(results) !=0:
        sql = "DELETE FROM verifyCourses WHERE dept = %s AND course_num = %s AND university_ID = %s"
        ID = session['id']
        print(dept,course_num,ID[0])
        val = (dept, course_num,ID[0])
        c.execute(sql, val,) 
        d.commit()
        return render_template('dropcourses.html',message = "course successfully dropped")
    # Show register page 
    print("wtf")
    return render_template('dropcourses.html')


##############################################
#FACULTY

#faculty home page 
@app.route('/pythonlogin/facultyhome', methods=['GET', 'POST'])
def facultyhome():
  if session['loggedin'] == True:
      # Check if account exists using MySQL
      print(session['id'])
      c=d.cursor()
      c.execute('SELECT * FROM faculty WHERE faculty_ID = %s', (session['id']),)
      result = c.fetchone()
      #display faculty info
      c.execute('SELECT * FROM teaches WHERE faculty_ID = %s', (session['id']),)
      teaches = c.fetchall()
  
      if len(teaches) !=0:
        return render_template('facultyhome.html', fname = result[1],lname = result[2], dept = result[3],teaches = teaches)

  print("false")
  return render_template('facultyhome.html')


#function for submitting grades
@app.route('/pythonlogin/submitgrades', methods=['GET', 'POST'])
def submitgrades():
  msg = ''
  if request.method == 'POST':
        search = request.form['search']
        # Check if course exists using MySQL
        c=d.cursor()
        c.execute('SELECT university_ID, course_name, course_num, grade, credits FROM verifyCourses WHERE university_ID = %s', (search,))
        result = c.fetchall()
        c.execute('SELECT * FROM testuserTranscript WHERE university_ID = %s', (search,))
        transcript = c.fetchall()
        #if course exists print it out in table
        if len(transcript) !=0:
          return render_template('submitgrades.html', submitgrade = result, transcript = transcript)
          
        
        #course doesnt exist 
        else:
          return render_template('submitgrades.html', messageresult= 'student not found, please enter valid universtiy ID')
  
  return render_template('submitgrades.html')


#function for submitting grades
@app.route('/pythonlogin/gssubmitgrades', methods=['GET', 'POST'])
def gssubmitgrades():
  msg = ''
  if request.method == 'POST':
        search = request.form['search']
        # Check if course exists using MySQL
        c=d.cursor()
        c.execute('SELECT university_ID, course_name, course_num, grade, credits FROM verifyCourses WHERE university_ID = %s', (search,))
        result = c.fetchall()
        c.execute('SELECT * FROM testuserTranscript WHERE university_ID = %s', (search,))
        transcript = c.fetchall()
        #if course exists print it out in table
        if len(transcript) !=0:
          return render_template('gssubmitgrades.html', submitgrade = result, transcript = transcript)
          
        
        #course doesnt exist 
        else:
          return render_template('gssubmitgrades.html', messageresult= 'student not found, please enter valid universtiy ID')
  
  return render_template('gssubmitgrades.html')


#generate list of total students 
@app.route('/pythonlogin/generatelist', methods=['GET', 'POST'])
def generatelist():
  msg = ''
  if request.method == 'POST':
    #generate list based on university ID's
    c=d.cursor()
    c.execute('SELECT * FROM student')
    result = c.fetchall()
    print("LIST")
    print(result)
    #if exists print it out in table
    if len(result) !=0:
      return render_template('generatelist.html', result = result)
    #error
    else:
      return render_template('generatelist.html', message= 'error, please try again')
  return render_template('generatelist.html')


@app.route('/pythonlogin/gradsechome', methods=['GET', 'POST'])
def gradsechome():
  # Check if user is loggedin
  #if 'loggedin' in session:
  #if button pressed to view transcript then show this page 
  if session['loggedin'] == True:
    # Check if account exists using MySQL
    print(session['id'])
    c=d.cursor()
    print(session['id'])
    return render_template('gradsechome.html')

  return render_template('gradsechome.html')


app.run(host='0.0.0.0', port=8080)

