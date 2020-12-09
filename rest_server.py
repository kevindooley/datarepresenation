from flask import Flask, jsonify, request, abort
from EmployeeDAO import employeeDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')



#demonstrate connection to server
# #curl "http://127.0.0.1:5000/
@app.route('/')
def index():
   return "Hello, welcome to server"

# get all employees
#curl "http://127.0.0.1:5000/employees"
@app.route('/employees')
def getAll():
    #print("in getall")
    results = employeeDAO.getAll()
    return jsonify(results)

#findById
#curl "http://127.0.0.1:5000/employees/"
@app.route('/employees/<int:id>')
def findById(id):
    foundEmployee = employeeDAO.findById(id)
    return jsonify(foundEmployee)

#create an employee
#curl  -i -H "Content-Type:application/json" -X POST -d "{\"f_name\":\"joel\",\"s_name\":\"someone\",\"age\":123,\"emp_role\":\"ENG\",\"salary\":56000}" http://127.0.0.1:5000/employees
@app.route('/employees', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)

    employee = {
        "f_name": request.json['f_name'],
        "s_name": request.json['s_name'],
        "age": request.json['age'],
        "emp_role": request.json['emp_role'],
        "salary": request.json['salary'],
    }

    return jsonify(employeeDAO.create(employee))

#update an employee
#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"s_name\":\"Owens\",\"age\":45,\"emp_role\":\"FIN\"}" http://127.0.0.1:5000/employees/4
@app.route('/employees/<int:id>', methods=['PUT'])
def update(id):
    foundEmployee = employeeDAO.findById(id)
    print(foundEmployee)
    if foundEmployee == {}:
        return jsonify({}),404
    currentEmployee = foundEmployee
    if 'f_name' in request.json:
        currentEmployee['f_name'] = request.json['f_name']
    if 's_name' in request.json:
        currentEmployee['s_name'] = request.json['s_name']
    if 'age' in request.json:
        currentEmployee['age'] = request.json['age']
    if 'emp_role' in request.json:
        currentEmployee['emp_role'] = request.json['emp_role']
    if 'salary' in request.json:
        currentEmployee['salary'] = request.json['salary']
    
    employeeDAO.update(currentEmployee)
    return jsonify(currentEmployee)
        
# delete an employee
# curl -X DELETE http://127.0.0.1:5000/employees/6   
@app.route('/employees/<int:id>' , methods=['DELETE'])
def delete(id):
    employeeDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)