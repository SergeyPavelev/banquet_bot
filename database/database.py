import sqlite3 as sql
import random


class Database:
    def __init__(self, db_file):
        with sql.connect(db_file) as self.con:
            self.cur = self.con.cursor()
            self.cur.execute(
                """CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )"""
            )
            self.cur.execute(
                """CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )"""
            )
            self.con.commit()
    
    def close(self):
        if self.con:
            self.con.close()
            
    def get_all_user(self):
        try:
            all_users = self.cur.execute("SELECT * FROM users").fetchall()
            string_users = ''
        
            for id, name in all_users:
                string_users += f'{id} - {name}\n'
            
            if string_users == '':
                return 'Нет пользователей'
            return string_users
        except sql.Error as e:
            print(f'Ошибка при получении всех пользователей {e}')
     
    def add_user(self, name_user):
        try:
            self.cur.execute('INSERT INTO users (name) VALUES (?)', (name_user,))
            self.con.commit()
        except sql.Error as e:
            print(f"Ошибка при добавлении нового пользователя: {e}")
    
    def delete_user(self, user_id):
        try:
            self.cur.execute('DELETE FROM users WHERE id = ?', (user_id,))
            self.con.commit()
        except sql.Error as e:
            print(f"Ошибка при удалении пользователя: {e}")
    
    def edit_user_name(self, user_id, new_user_name):
        try:
            self.cur.execute('UPDATE users SET name = ? WHERE id = ?', (new_user_name, user_id))
            self.con.commit()
        except sql.Error as e:
            print(f"Ошибка при редактировании имени пользователя: {e}")
    
    def get_all_tasks(self):
        try:
            all_tasks = self.cur.execute("SELECT * FROM tasks").fetchall()
            string_tasks = ''
        
            for id, name in all_tasks:
                string_tasks += f'{id} - {name}\n'

            if string_tasks == '':
                return 'Нет задач'
            return string_tasks
        except sql.Error as e:
            print(f'Ошибка при получении всех заданий {e}')
    
    def add_task(self, name_task):
        try:
            self.cur.execute('INSERT INTO tasks (name) VALUES (?)', (name_task,))
            self.con.commit()
        except sql.Error as e:
            print(f"Ошибка при добавлении нового задания: {e}")
    
    def delete_task(self, task_id):
        try:
            self.cur.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
            self.con.commit()
        except sql.Error as e:
            print(f"Ошибка при удалении задания: {e}")
            
    def edit_task_name(self, task_id, new_name_task):
        try:
            self.cur.execute('UPDATE tasks SET name = ? WHERE id = ?', (new_name_task, task_id))
            self.con.commit()
        except sql.Error as e:
            print(f"Ошибка при редактировании названия задания: {e}")
    
    def generate_values(self):
        try:
            all_users = self.cur.execute("SELECT * FROM users").fetchall()
            all_tasks = self.cur.execute("SELECT * FROM tasks").fetchall()
            
            if all_users == '':
                return 'Пользователей нет'
            if all_tasks == '':
                return 'Заданий нет'
            
            return f'{random.choice(all_users)[1]} - {random.choice(all_tasks)[1]}'
        except sql.Error as e:
            print(f'Ошибка генерации значений: {e}')
            