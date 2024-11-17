import sqlite3
from singleton_decorator import singleton

@singleton
class DatabaseHandler:
    def __init__(self):
        self.connection = sqlite3.connect('tasks.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT NOT NULL,
                                description TEXT
                             )''')
        self.connection.commit()

    def add_task(self, task):
        self.cursor.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (task['title'], task['description']))
        self.connection.commit()

    def get_all_tasks(self):
        self.cursor.execute('SELECT * FROM tasks')
        rows = self.cursor.fetchall()
        tasks = [{"id": row[0], "title": row[1], "description": row[2]} for row in rows]
        return tasks