
from fastapi import FastAPI,HTTPException
from models import Employee
from typing import List


employee_db:List[Employee]=[]

app=FastAPI()

@app.get('/employee',response_model=List[Employee])
def get_employee():
    return employee_db


#read specific employee
@app.get('/employee/{emp_id}',response_model=Employee)
def get_employee(emp_id:int):
    for index,employee in enumerate(employee_db): #Enumerate is used to get two thing one is the index and second is the employee object
        if employee.id==emp_id:
            return employee_db[index]
    raise HTTPException(status_code=404,detail='Employee not found')


#add an Employee
@app.post('/add_employee',response_model=Employee)
def add_employee(new_emp:Employee):
    for employee in employee_db:
        if employee.id==new_emp.id:
            raise HTTPException(status_code=400,detail='Employee already exists')
    employee_db.append(new_emp)
    return new_emp

 
 #update an employee
@app.put('/update_employee/{emp_id}')
def update_employee(emp_id:int,updated_employee:Employee):
    for index,employee in enumerate(employee_db):
        if employee_db.id== emp_id:
            employee_db[index]=update_employee
            return update_employee
    raise HTTPException(status_code=404,detail='Not found')


#delete an employee
@app.delete('delete_employee/{emp_id}')
def delete_employee(emp_id:int):
    for index,employee in enumerate(employee_db):
        if employee.id==emp_id:
            del employee_db[index]
            return {'message':'Employee deleted successfully'}
    raise HTTPException(status_code=404,detail='Employee not Found')






