import datetime

def fetch_student(database, id):
        '''
        Returns the student name for a particular student id, or None if the student is not in the database
        '''
        if id in database:
            return database[id]
        return None
    
def current_day_of_week():
    return datetime.today().strftime('%A')
    
def today_is_weekend():
    today = current_day_of_week()
    if today == "Saturday" or today == "Sunday":
        return True
    return False

class Student:
    def __init__(self, name, age, major_credits, AP_credits):
        self.name = name
        self.age = age
        self.major_credits = major_credits
        self.AP_credits  = AP_credits
        
    def total_credits(self):
        return self.major_credits + self.AP_credits
        
def satisfied_requirements(student):
    return student.total_credits() > 32