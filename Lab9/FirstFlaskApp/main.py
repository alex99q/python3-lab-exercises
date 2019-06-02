from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def mainpage():

    return"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <ul style="display:block; width:10%; height:100%; float:left">
          <li><a href="/">Home</a></li>
          <li><a href="/create">Create</a></li>
          <li><a href="news.asp">Update</a></li>
          <li><a href="about.asp">Remove</a></li>
        </ul>
        <table style="width:80%">
          <tr>
            <th>Firstname</th>
            <th>Lastname</th> 
            <th>Age</th>
          </tr>
          <tr>
            <td>Jill</td>
            <td>Smith</td> 
            <td>50</td>
          </tr>
          <tr>
            <td>Eve</td>
            <td>Jackson</td> 
            <td>94</td>
          </tr>
        </table>
    </body>
    </html>
    """

@app.route('/create', methods = ['POST', 'GET'])
def create_record():
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        birthday = request.form.get('birthday')
        phone_number = request.form.get('phone_number')
        email = request.form.get('email')
        profession = request.form.get('profession')
        interests = request.form.get('interests')

        with open("contacts.txt", mode='a', encoding='utf-8') as file:
            file.write("name{};{};{};{};{};{};{}\n".format(name, address, birthday, phone_number, email, profession, interests))

        return redirect(url_for('create_record'))

    elif request.method == 'GET':
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
            <ul style="display:block; width:10%; margin-bottom:100%; float:left">
              <li><a href="/">Home</a></li>
              <li><a href="/create">Create</a></li>
              <li><a href="news.asp">Update</a></li>
              <li><a href="about.asp">Remove</a></li>
            </ul>
            <div>
                <form action="http://localhost:5000/create" method="post" >
                    <p>Enter Name:</p>
                    <p><input type = "text" name="name" /></p>
                    
                    <p>Enter Address:</p>
                    <p><input type = "text" name="address" /></p>
                    
                    <p>Enter Birthday:</p>
                    <p><input type = "text" name="birthday" /></p>
                    
                    <p>Enter Phone number:</p>
                    <p><input type = "text" name="phone_number" /></p>
                    
                    <p>Enter Email:</p>
                    <p><input type = "text" name="email" /></p>
                    
                    <p>Enter Profession:</p>
                    <p><input type = "text" name="profession" /></p>
                    
                    <p>Enter Interests:</p>
                    <p><input type = "text" name="interests" /></p>
                    
                    <p><input type = "submit" value = "submit" /></p>
                </form>
            </div>
        </body>
        </html>
        """
    else:
        return "Invalid reguest"

if __name__ == '__main__':
    app.run(debug=True)
