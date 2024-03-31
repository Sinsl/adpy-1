from application.salary import run as run_salary
from application.people import run as run_people
import datetime
import emoji

if __name__ == '__main__':
    dt_now = datetime.datetime.now()
    dt_str = dt_now.strftime('%d-%m-%Y %H:%M:%S')
    print(dt_str)
    run_salary()
    run_people()
    
    result = emoji.emojize('Python is :thumbs_up:')
    print(result)