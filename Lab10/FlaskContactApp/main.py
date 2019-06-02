from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def mainpage():
    contacts = []

    with open("contacts.txt", mode='r', encoding='utf-8') as file:
        for line in file:
            contacts.append(line.strip("\n").split(";"))

    return render_template("index.html", contact_info=contacts)


@app.route('/create', methods=['POST', 'GET'])
def create_record():
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        birthday = request.form.get('birthday')
        phone_number = request.form.get('phone_number')
        email = request.form.get('email')
        profession = request.form.get('profession')
        interests = request.form.get('interests')

        with open("contacts.txt", mode='r', encoding='utf-8') as file:
            for line in file:
                current_name = line.split(";")[0]

                if current_name == name:
                    string_to_render = "onload=\"alertUser('There is already a name like this!')\""
                    return render_template("create.html", warning_msg=string_to_render)

        with open("contacts.txt", mode='a', encoding='utf-8') as file:
            file.write(
                "{};{};{};{};{};{};{}\n".format(name, address, birthday, phone_number, email, profession, interests))

        return redirect(url_for('create_record'))

    elif request.method == 'GET':
        return render_template("create.html")
    else:
        return "Invalid request"


@app.route('/update', methods=['POST', 'GET'])
def update_record():
    if request.method == 'POST':

        search_name = request.form.get('search_name')

        is_found = False
        result_str = "There is no contact with the same name!"
        with open("contacts.txt", mode='r', encoding='utf-8') as file:
            for line in file:
                current_name = line.split(";")[0]

                if current_name == search_name:
                    result_str = line
                    is_found = True
                    break

        if is_found:
            return redirect(url_for('make_update', searched_contact=result_str))
        else:
            return render_template("update.html", found_data=result_str, is_found=False)

    elif request.method == 'GET':
        return render_template("update.html")
    else:
        return "Invalid request"


@app.route('/update/<searched_contact>', methods=['POST', 'GET'])
def make_update(searched_contact):
    if request.method == 'POST':

        name = searched_contact.split(";")[0] if request.form.get('name') == "" else request.form.get('name')
        address = searched_contact.split(";")[1] if request.form.get('address') == "" else request.form.get('address')
        birthday = searched_contact.split(";")[2] if request.form.get('birthday') == "" else request.form.get('birthday')
        phone_number = searched_contact.split(";")[3] if request.form.get('phone_number') == "" else request.form.get('phone_number')
        email = searched_contact.split(";")[4] if request.form.get('email') == "" else request.form.get('email')
        profession = searched_contact.split(";")[5] if request.form.get('profession') == "" else request.form.get('profession')
        interests = searched_contact.split(";")[6] if request.form.get('interests') == "" else request.form.get('interests')

        with open("contacts.txt", "r") as file:
            lines = file.readlines()
        with open("contacts.txt", "w") as file:
            for line in lines:
                if line.strip("\n") == searched_contact.strip("\n"):
                    file.write("{};{};{};{};{};{};{}\n"
                               .format(name, address, birthday, phone_number, email, profession, interests))
                else:
                    file.write(line)

        return render_template("update.html")

    elif request.method == 'GET':
        return render_template("update.html", found_data=searched_contact, is_found=True)


@app.route('/remove', methods=['POST', 'GET'])
def remove_record():
    if request.method == 'POST':

        search_name = request.form.get('search_name')
        message = "There is no such contact!"

        with open("contacts.txt", "r") as file:
            lines = file.readlines()
        with open("contacts.txt", "w") as file:
            for line in lines:
                if line.strip("\n").split(";")[0] != search_name:
                    file.write(line)
                else:
                    message = "Contact deleted!"

        return render_template("remove.html", display_message=message)

    elif request.method == 'GET':
        return render_template("remove.html")
    else:
        return "Invalid request"


if __name__ == '__main__':
    with open("contacts.txt", "a") as file:
        pass
    app.run(debug=True)