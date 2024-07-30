import sqlite3


class DatabaseManager:
    def __init__(self, db_name='db_information.db'):
        """
        Initializes the DatabaseManager with a connection to the specified SQLite database.

        Args:
            db_name (str): The name of the database file.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()


    def get_student_data(self, student_id):
        """
        Retrieves student data from the SQLite database.

        Args:
            student_id (int): The ID of the student.

        Returns:
            tuple: The data of the student.
        """
        self.cursor.execute('SELECT * FROM questions WHERE ID = ?', (student_id,))
        return self.cursor.fetchone()
          
    
    def close(self):
        """
        Closes the database connection.
        """
        self.connection.close()