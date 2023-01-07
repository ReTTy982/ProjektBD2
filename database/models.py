from mysql.connector import connect, Error


""" try:
    with connect(
        host="localhost",
        user=input("Username: "),
        password=input("Password: "),
        database="library",
        auth_plugin='mysql_native_password'
    ) as connection:
        print(connection.is_connected())
except Error as e:
    print(e)

connection.close() """


class User(object):

    host = None
    user = None
    password = None
    database = None
    connection = None
    session = None

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def open_connection(self):
        try:
            cnx = connect(host=self.host, user=self.user, password=self.password)
            self.connection = cnx
            self.session = cnx.cursor()

        except Error as e:
            print(e)

    def close_connection(self):
        try:
            self.connection.close()
        except Error as e:
            print(e)


class Librarian(User):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insert_book(self):
        pass

    def delete_book(self):
        pass

    def update_book(self):
        pass

    def select_issue(self,x):
        query = (
            """SELECT * FROM wypozyczalnia.bookIssue
            WHERE BranchID = %s"""
        )
        self.session.execute(query, (x,))
        for i in self.session:
            print(i)




class Client(User):
    def __init__(self, username, password):
        super().__init__(username, password)
    
    
