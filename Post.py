
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy employee data (a list of dictionaries)
dummy_employees = [
    {
        "id": 1,
        "name": "John Doe",
        "position": "Software Engineer",
        "salary": 175000.00,
        "department": "Engineering",
    },
    { 
        "id": 2,
        "name": "Smith",
        "position": "Data Analyst",
        "salary": 60000.00,
        "department": "Analytics",
    },
    {
        "id": 3,
        "name": "Johnson",
        "position": "Marketing Specialist",
        "salary": 55000.00,
        "department": "Marketing",
    },{
        "id": 4,
        "name": "Leo Das",
        "position": "Marketing Team",
        "salary": 95000.00,
        "department": "Marketing",
    },
    {
        "id": 5,
        "name": "Dileep",
        "position": "Developer",
        "salary": 95000.00,
        "department": "Engineering",
    }
]

@app.route('/get_employees', methods=['GET', 'POST'])
def get_employees():
    employee_id = request.args.get('id')
    
    if request.method == 'GET':
        if employee_id is not None:
            filtered_employees = [employee for employee in dummy_employees if employee['id'] == int(employee_id)]
            return jsonify(filtered_employees)
        else:
            return jsonify(dummy_employees)
    elif request.method == 'POST':
        return jsonify(dummy_employees)
    else:
        return "Invalid request method. Use GET or POST to retrieve employee details."

if __name__ == '__main__':
    app.run(debug=True)
