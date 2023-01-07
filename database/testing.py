from models import *

testing_user = Librarian("localhost","root","Polekpacz1998$","wypozyczalnia")
testing_user.open_connection()
testing_user.select_issue(1)