from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = '34.101.173.241'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'capstone123'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    return "API is running!"

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Task")
    tasks = cur.fetchall()
    cur.close()
    return jsonify(tasks)


@app.route('/users', methods=['GET'])
def get_all_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM User")
    users = cur.fetchall()
    cur.close()
    return jsonify(users)


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Task WHERE Id = %s", (task_id,))
    task = cur.fetchone()
    cur.close()
    return jsonify(task)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM User WHERE Id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    return jsonify(user)


@app.route('/tasks', methods=['POST'])
def create_task():
    taskname = request.json['Taskname']
    dateline = request.json['Dateline']
    urgency = request.json['Urgency']
    importance = request.json['Importance']
    complexity = request.json['Complexity']
    status = request.json['Status']
    description = request.json['Description']

    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO Task (Taskname, Dateline, Urgency, Importance, Complexity, Status, Description) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (taskname, dateline, urgency, importance, complexity, status, description)
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Task created successfully'}), 201


@app.route('/users', methods=['POST'])
def create_user():
    name = request.json['Name']
    username = request.json['Username']
    email = request.json['Email']
    phone = request.json['Phone']
    country = request.json['Country']
    password = request.json['Password']
    confirm_password = request.json['Confirm_Password']

    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO User (Name, Username, Email, Phone, Country, Password, Confirm_Password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (name, username, email, phone, country, password, confirm_password)
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'User created successfully'}), 201


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    taskname = request.json['Taskname']
    dateline = request.json['Dateline']
    urgency = request.json['Urgency']
    importance = request.json['Importance']
    complexity = request.json['Complexity']
    status = request.json['Status']
    description = request.json['Description']

    cur = mysql.connection.cursor()
    cur.execute(
        "UPDATE Task SET Taskname = %s, Dateline = %s, Urgency = %s, Importance = %s, Complexity = %s, Status = %s, Description = %s WHERE Id = %s",
        (taskname, dateline, urgency, importance, complexity, status, description, task_id)
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Task updated successfully'})


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    name = request.json['Name']
    username = request.json['Username']
    email = request.json['Email']
    phone = request.json['Phone']
    country = request.json['Country']
    password = request.json['Password']
    confirm_password = request.json['Confirm_Password']

    cur = mysql.connection.cursor()
    cur.execute(
        "UPDATE User SET Name = %s, Username = %s, Email = %s, Phone = %s, Country = %s, Password = %s, Confirm_Password = %s WHERE Id = %s",
        (name, username, email, phone, country, password, confirm_password, user_id)
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'User updated successfully'})


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Task WHERE Id = %s", (task_id,))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Task deleted successfully'})


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM User WHERE Id = %s", (user_id,))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'User deleted successfully'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
