import sqlite3

class MyDatabase:
    """Decorator class for inserting questions in database, we create and increase a table\
    called Answer and we store the mined questions."""

    def __init__(self):
        self.connection = sqlite3.connect("database/survey.db")
        self.cursor = self.connection.cursor()

    def createTableQuestion(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Question (questionURL TEXT, answerURL TEXT
        , questionID INT, answerID INT, title TEXT)''')

    def createTableAnswer(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Answer (questionURL TEXT, answerText TEXT) ''')

    def insertQuestion(self, values):
        self.cursor.execute('''INSERT INTO Question (questionURL, answerURL, questionID, answerID, title) VALUES '''
            + values)
    
    def insertAnswer(self, values):
        self.cursor.execute('''INSERT INTO Answer (questionURL, answerText ) VALUES ''' 
            + values)

    def closeDB(self):
        try:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
        except sqlite3.ProgrammingError as e:
            print(e)

    def showAllQuestion(self):
        self.cursor.execute("SELECT * FROM Question;")
        results = self.cursor.fetchall()
        for r in results:
            print(r)
        self.closeDB()

    def showAllAnswer(self):
        self.cursor.execute("SELECT * FROM Answer;")
        results = self.cursor.fetchall()
        for r in results:
            print(r)
        print(len(results))
        self.closeDB()

    def retrieveAllQuestionIDs(self):
        self.connection.row_factory = lambda cursor, row: row[0]
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT questionID FROM Question;")
        results = self.cursor.fetchall()
        for r in results:
            print(r)
        print(results)
        return results

if __name__ == '__main__':
    #MyDatabase().showAll()
    survey = MyDatabase()
    survey.showAllQuestion()