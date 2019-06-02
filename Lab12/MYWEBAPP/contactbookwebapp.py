from flask import Flask, redirect, url_for, request,abort, render_template, session
from datetime import timedelta
import os
import sqlite3

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    

@app.route('/')
def mainpage():
    if not 'username' in session:
        return redirect(url_for('login'))
    return render_template('index.html')



@app.route('/create', methods=['GET', 'POST'])
def create_record():
    if not 'username' in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        bothnames=request.form['bothnames']
        address=request.form['address']
        birthday=request.form['birthday']
        phone=request.form['phone']
        email=request.form['email']
        prof=request.form['profession']
        interests=request.form['interests']
        db=sqlite3.connect('database.db')
        conn = db.cursor()
        conn.execute("INSERT INTO Contacts (names, address, birthday, phone, email, prof, interests) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');"
                     .format(bothnames, address, birthday, phone, email, prof, interests))
        db.commit()
        db.close()
        return render_template('success.html')
    elif request.method == 'GET':
        return render_template('enterinfo.html')
    else:
        return "Invalid reguest"
    
filecontent_update=[]
@app.route('/update/<commit>', methods=['GET', 'POST'])
def update_record(commit):
    if not 'username' in session:
      return redirect(url_for('login'))
    global filecontent_update
    if request.method == 'GET':
        return render_template('whattoupdate.html', whichpath='/update/search')
    elif request.method == 'POST':
        if commit == 'search':
            searchtext = request.form['searchtext']
            updatelist = []
            index = 0
            db = sqlite3.connect('database.db')
            conn = db.cursor()
            conn.execute("SELECT * FROM Contacts WHERE ( names LIKE '%{0}%' OR address LIKE '%{0}%' OR "
                         "birthday LIKE '%{0}%' OR phone LIKE '%{0}%' OR email LIKE '%{0}%' OR "
                         "prof LIKE '%{0}%' OR interests LIKE '%{0}%')".format(searchtext))
            updatelist = conn.fetchall()
            db.commit()
            db.close()

            updatelist = list(map(lambda x: list(x), updatelist))

            for n in range(0, len(updatelist)):
                updatelist[n].pop(0)

            return render_template('visualisecontacts.html', whichpath=url_for('update_record', commit='write'),
                                   contactdb=updatelist)
        elif commit == 'write':
            confirmlist = request.form.getlist('records_update')
            if not confirmlist:
                return "Nothing has been selected"
            db = sqlite3.connect('database.db')
            conn = db.cursor()
            for item in confirmlist:
                updatednames = request.form['names_' + item]
                updatedaddress = request.form['address_' + item]
                updatedbday = request.form['bday_' + item]
                updatedphone = request.form['phone_' + item]
                updatedemail = request.form['email_' + item]
                updatedprof = request.form['prof_' + item]
                updatedinter = request.form['inter_' + item]

                conn.execute("SELECT * FROM Contacts")
                rows = conn.fetchall()

                conn.execute("UPDATE Contacts "
                             "SET names = '{}', address = '{}', birthday = '{}', phone = '{}', email = '{}', prof = '{}', interests = '{}' "
                             "WHERE id=={};"
                             .format(updatednames, updatedaddress, updatedbday, updatedphone, updatedemail, updatedprof, updatedinter, rows[int(item)][0]))
                db.commit()
            db.close()
            return "The update has been done successfuly" + str(confirmlist) + \
                   "</br> click <a href=\"/\">here to return to the home page</a>"
        else:
            abort(400)
    else:
        return "Invalid reguest"
    
 
        
@app.route('/search', methods=['GET', 'POST'])
def search_record():
    if not 'username' in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        searchtext = request.form['searchtext']
        searchlist = []

        con = sqlite3.connect('database.db')
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Contacts WHERE ( names LIKE '%{0}%' OR address LIKE '%{0}%' OR "
                        "birthday LIKE '%{0}%' OR phone LIKE '%{0}%' OR email LIKE '%{0}%' OR "
                        "prof LIKE '%{0}%' OR interests LIKE '%{0}%')"
                        .format(searchtext))

            rows = cur.fetchall()

            for row in rows:
                currentStr = ""
                for n in range(1, len(row)):
                    currentStr += str(row[n]) + ";"
                searchlist.append(currentStr.strip(";"))

        return render_template('visualisecontacts.html', whichpath=url_for('search_record'), contactdb=searchlist)
    elif request.method == 'GET':
        return render_template('searchinfo.html', whichpath=url_for('search_record'))
    else:
        return "Invalid reguest"
    
    
    
filecontext=[]
@app.route('/remove', methods=['GET', 'POST'])
def remove_record():
    if not 'username' in session:
        return redirect(url_for('login'))
    if request.method == 'GET':
        con = sqlite3.connect('database.db')
        with con:
            cur = con.cursor()

            cur.execute("SELECT * FROM Contacts")

            rows = list(map(lambda x: list(x), cur.fetchall()))

            for n in range(0, len(rows)):
                rows[n].pop(0)

            rows = map(lambda x: ";".join(x), rows)

            global filecontext

            filecontext=list(enumerate([line for line in rows]))

            return render_template('removecontacts.html', contactdb=filecontext)
    elif request.method == 'POST':
        records_removal=request.form.getlist('records_removal')
        confirmation=request.form['confirmation']
        removal_button=request.form['removal_button']

        removed=[]
        if confirmation != 'on':
            return "<h3>You need to check the confirmation checkbox!</h3>"

        for record in sorted(records_removal, reverse=True):
          removed.append(filecontext.pop(int(record))[1])

        for record in removed:
            record_rows = record.split(";")

            bothnames = record_rows[0]
            address = record_rows[1]
            birthday = record_rows[2]
            phone = record_rows[3]
            email = record_rows[4]
            prof = record_rows[5]
            interests = record_rows[6]

            con = sqlite3.connect('database.db')
            with con:
                cur = con.cursor()

                cur.execute("DELETE FROM Contacts WHERE ( names LIKE '%{}%' AND address LIKE '%{}%' AND "
                            "birthday LIKE '%{}%' AND phone LIKE '%{}%' AND email LIKE '%{}%' AND "
                            "prof LIKE '%{}%' AND interests LIKE '%{}%')"
                            .format(bothnames, address, birthday, phone, email, prof, interests))

        return render_template('successremoved.html', removed_contacts=removed)
    else:
        return "Invalid reguest"
    

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
     db=sqlite3.connect('database.db')
     conn = db.cursor()
     username1 = request.form['uname']
     password1 = request.form['pass']
     conn.execute("SELECT password from Accounts where username = '%s'" % username1)
     passwd = conn.fetchone()
     db.close()
    # return username1+" "+passwd[0]
     if password1 == passwd[0]:
       session['username'] = username1  
       return redirect(url_for('mainpage'))
     return abort(401)
   else:
       return """
<html>
<head>
</head>
<body align=center>
<h1>Enter your login credentials:</h1>
<form action='/login', method='POST'>
<table align=center>
<tr><td>Username:</td><td> <input type="text" name="uname" size=14/></td></tr>
<tr><td>Password:</td><td> <input type='password' name='pass' size=14/></td></tr>
</table><br><br>
<input type='submit' name='login' value='Login'> 
</form>
</body>
</html>
"""
@app.route('/logout',methods = ['POST', 'GET'])
def logout():
    global session
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
     db=sqlite3.connect('database.db')
     conn = db.cursor()
     conn.execute("create table if not exists Contacts (id INTEGER NOT NULL PRIMARY KEY, names text , address text, birthday text, phone text, email text, prof text, interests text)")
     conn.execute("create table if not exists Accounts (u_id INTEGER NOT NULL PRIMARY KEY ON CONFLICT IGNORE , username text, password text)")
     db.commit()
     conn.execute("INSERT OR IGNORE INTO  Accounts VALUES (0, 'admin', '12345678')")
     db.commit()
     db.close()
     app.run(port=5017, debug = True)
