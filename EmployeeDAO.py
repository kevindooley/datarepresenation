import mysql.connector
import dbconfig as cfg

# connecting to database without hard coding password, username etc
class EmployeeDAO:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql['host'], 
            user=cfg.mysql['user'], 
            password=cfg.mysql['password'], 
            db=cfg.mysql['db']
            )
        #print("connection made")
    
#create
    def create(self, employee):
        cursor = self.db.cursor()
        sql="insert into employees (f_name,s_name, age,emp_role,salary) values (%s,%s,%s,%s,%s)"
        
        values = [
 
            employee['f_name'],
            employee['s_name'],
            employee['age'],
            employee['emp_role'],
            employee['salary']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid


    #get all
    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from employees"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results: # takes out results independently. Turns tuple into dict
            returnArray.append(self.convertToDictionary(result))
        return returnArray

    #find by ID
    def findById(self, id):
        cursor = self.db.cursor()
        sql="select * from employees where id = %s"
        values = [id]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

#update
    def update(self, employee):
        cursor = self.db.cursor()
        sql="update employees set f_name=%s,s_name=%s, age=%s, emp_role=%s, salary=%s  where id = %s"

        values = [

            employee['f_name'],
            employee['s_name'],
            employee['age'],
            employee['emp_role'],
            employee['salary'],
            employee['id']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return employee

# delete by id 
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from employees where id = %s"
        values = [id]

        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()


    #function to turn tuples to dict
    def convertToDictionary(self, result):
        colnames=['id','f_name','s_name', 'age','emp_role','salary']
        item = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item

employeeDAO = EmployeeDAO()
