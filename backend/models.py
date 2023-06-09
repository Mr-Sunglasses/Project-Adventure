from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from uuid import uuid4

db = SQLAlchemy()

def get_uuid():
    return uuid4().hex

class Employees(db.Model):
    __tablename__ = "EMPLOYEE"
    Employeeid = db.Column(db.Integer, primary_key=True, unique=True, nullable = False)
    Email = db.Column(db.String(345), unique=True, nullable = False)
    Password = db.Column(db.Text, nullable=False)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    PhoneNumber = db.Column(db.Integer, nullable = False)
    Admin = db.Column(db.Boolean, nullable=False)
    DateHired = db.Column(db.String(345), nullable=False)

class Customers(db.Model):
    __tablename__ = "CUSTOMER"
    Customerid = db.Column(db.Integer,primary_key=True, unique=True)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(345), unique=True, nullable=False)
    City = db.Column(db.String(50), nullable=False)
    Street = db.Column(db.String(50), nullable=False)
    State = db.Column(db.String(50), nullable=False)
    ZIP = db.Column(db.String(5), nullable=False)
    PhoneNumber = db.Column(db.Integer, nullable=False)

class Generators(db.Model):
    __tablename__ = "GENERATOR"
    Generatorid = db.Column(db.Integer, primary_key=True, unique=True)
    Name = db.Column(db.String(50), nullable=False)
    Cost = db.Column(db.Double(5,2), nullable=False)
    Notes = db.Column(db.Text, nullable=True)

class ServiceRecords(db.Model):
    __tablename__ = "SERVICE_RECORD"
    Serviceid = db.Column(db.Integer, primary_key=True, unique=True)
    Customerid = db.Column(db.Integer, db.ForeignKey('CUSTOMER.Customerid'), nullable=False)
    ServiceCustomer = db.relationship("Customers", backref=db.backref("CUSTOMER", uselist=False))
    Generatorid = db.Column(db.Integer, db.ForeignKey('GENERATOR.Generatorid'), nullable=False)
    ServiceGenerator = db.relationship("Generators", backref = db.backref("GENERATOR", uselist=False))
    ServicePerformed = db.Column(db.Boolean, nullable=False)
    StartDate = db.Column(db.String(10), nullable=False)
    StartTime = db.Column(db.String(7), nullable=False)
    FinishDate = db.Column(db.String(10), nullable=True)
    FinishTime = db.Column(db.String(7), nullable=True)
    ServiceType = db.Column(db.String(50), nullable=False)
    Notes = db.Column(db.Text, nullable=True)
    

class Service_Employee_Int(db.Model):
    __tablename__ = "SERVICE_EMPLOYEE_INT"
    Serviceid = db.Column(db.Integer, db.ForeignKey('SERVICE_RECORD.Serviceid'), primary_key = True, nullable=False)
    IntService = db.relationship("ServiceRecords", backref=db.backref("SERVICE_RECORD", uselist=False))
    Employeeid = db.Column(db.Integer, db.ForeignKey('EMPLOYEE.Employeeid'), primary_key = True, nullable=True)
    IntEmployee = db.relationship("Employees", backref=db.backref("EMPLOYEES", uselist=False))

class Password_Recovery(db.Model):
    __tablename__ = "PASSWORD_RECOVERY"
    Code = db.Column(db.Text, primary_key =True, nullable = False, unique = True)
    Email = db.Column(db.String(345), nullable = False, unique = False)
    Password = db.Column(db.Text, nullable = False)
    DateMade = db.Column(db.String(345), nullable = False)