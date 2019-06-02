from flask import Flask, redirect, url_for, request,abort, render_template, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    if request.method == 'POST':
        session.pop('user', None)
        if request.form.get('password') != '':
            username = request.form.get('username')
            session['user'] = username

        return render_template('index.html')

    elif request.method == 'GET':
        return render_template('index.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return render_template('index.html')


@app.route('/create', methods=['GET', 'POST'])
def create_record():
    if 'user' in session:
        if request.method == 'POST':
            bothnames = request.form['bothnames']
            address = request.form['address']
            birthday = request.form['birthday']
            phone = request.form['phone']
            email = request.form['email']
            prof = request.form['profession']
            interests = request.form['interests']
            with open('mycontacts.db', 'a+') as db:
                db.write("{};{};{};{};{};{};{}\n".format(bothnames, address, birthday, phone, email, prof, interests))
            return render_template('success.html')
        elif request.method == 'GET':
            return render_template('enterinfo.html')
        else:
            return "Invalid reguest"
    else:
        return render_template('notloggedin.html')


@app.route('/update/<commit>', methods=['GET', 'POST'])
def update_record(commit):
    if 'user' in session:
        if request.method == 'GET':
            return render_template('whattoupdate.html', whichpath='/update/search')
        elif request.method == 'POST':
            if commit == 'search':
                searchtext = request.form['searchtext']
                updatelist = []
                index = 0
                with open('mycontacts.db', 'r') as db:
                    for line in db:
                        line = line.rstrip()
                        if searchtext in line:
                            updatelist.append([index, line])
                        index += 1
                return render_template('visualisecontacts.html', whichpath=url_for('update_record', commit='write'),
                                       contactdb=updatelist)
            elif commit == 'write':

                update_record_indexes = request.form.getlist('records_removal')

                dbLines = []
                with open('mycontacts.db', 'r') as db:
                    dbLines = db.readlines()

                with open('mycontacts.db', 'w') as db:
                    for i in range(0, len(dbLines)):
                        if str(i) in update_record_indexes:

                            bothnames = request.form[str(i + 1) + '1']
                            address = request.form[str(i + 1) + '2']
                            birthday = request.form[str(i + 1) + '3']
                            phone = request.form[str(i + 1) + '4']
                            email = request.form[str(i + 1) + '5']
                            profession = request.form[str(i + 1) + '6']
                            interests = request.form[str(i + 1) + '7']

                            db.write("{};{};{};{};{};{};{}\n"
                                     .format(bothnames, address, birthday, phone, email, profession, interests))
                        else:
                            db.write(dbLines[i])

                return render_template('success.html')

            else:
                abort(400)
        else:
            return "Invalid reguest"
    else:
        return render_template('notloggedin.html')
 
        
@app.route('/search', methods=['GET', 'POST'])
def search_record():
    if 'user' in session:
        if request.method == 'POST':
            searchtext = request.form['searchtext']
            searchlist = []
            with open('mycontacts.db', 'r') as db:
                for line in db.readlines():
                    line = line.rstrip()
                    if searchtext in line:
                        searchlist.append(line)
            return render_template('visualisecontacts.html', whichpath=url_for('search_record'), contactdb=searchlist)
        elif request.method == 'GET':
            return render_template('searchinfo.html', whichpath=url_for('search_record'))
        else:
            return "Invalid reguest"
    else:
        return render_template('notloggedin.html')

    
filecontext=[]
@app.route('/remove', methods=['GET', 'POST'])
def remove_record():
    if 'user' in session:
        if request.method == 'GET':
            with open('mycontacts.db', 'r') as db:
                global filecontext
                filecontext = list(enumerate([line for line in db.readlines()]))
                return render_template('removecontacts.html', contactdb=filecontext)
        elif request.method == 'POST':
            records_removal = request.form.getlist('records_removal')
            confirmation = request.form['confirmation']
            removal_button = request.form['removal_button']
            removed = []
            if confirmation != 'on':
                return "<h3>You need to check the confirmation checkbox!</h3>"
            for record in sorted(records_removal, reverse=True):
                # return str(filecontext[int(item)])+" "+item
                removed.append(filecontext.pop(int(record))[1])
            with open('mycontacts.db', 'w') as db:
                for record in filecontext:
                    db.write(record[1])
            return render_template('successremoved.html', removed_contacts=removed)
        else:
            return "Invalid reguest"
    else:
        return render_template('notloggedin.html')


if __name__ == '__main__':
   app.run(port=5015, debug = True)
