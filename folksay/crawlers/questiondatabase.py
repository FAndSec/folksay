import sqlite3

class MyDatabase:
    """Decorator class for inserting questions in database, we create and increase a table\
    called Answer and we store the mined questions."""

    
    def createDB(self):
        self.connection = sqlite3.connect("database/survey.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('''DROP TABLE Answer''')
        self.cursor.execute('''CREATE TABLE Answer (questionURL TEXT, answerURL TEXT
        , questionID INT, answerID INT, title TEXT)''')
        self.cursor.execute('''INSERT INTO Site (lat, long, location) VALUES (12.25, 34.66, 'Morocco')''')

    def insertAnswer(self, values):
        self.cursor.execute('''INSERT INTO Answer (questionURL, answerURL, questionID, answerID, title) VALUES '''
        + values)

    def closeDB(self):
        self.cursor.close()
        self.connection.commit()
        self.connection.close()

    def showAll(self):
        self.cursor.execute("SELECT * FROM Answer;")
        results = self.cursor.fetchall()
        for r in results:
            print(r)