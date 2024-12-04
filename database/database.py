import sqlite3 as sql


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