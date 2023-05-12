import sqlite3


class Phone:
    def __init__(self):
        self.connection = sqlite3.connect("p3.db")
        self.cursor = self.connection.cursor()
        self.create_user()

    def create_user(self):
        self.cursor.execute("""
            create table if not exists user(
                id integer primary key,
                name varchar ,
                age integer ,
                phone_number varchar ,
                email varchar,
                photo varchar 
            )
        """)
        self.connection.commit()

    def add_user(self, name, age, phone_number, email, photo):
        self.cursor.execute("""
            insert into user (name, age, phone_number, email, photo)
            values (?, ?, ?, ?, ?)
        """, (name, age, phone_number, email, photo))
        self.connection.commit()

    def all_user(self, offset, limit):
        self.cursor.execute(f"""
            SELECT * FROM products LIMIT {limit} OFFSET {offset}
        """)
        return self.cursor.fetchall()

    # Barcha productlar sonini olish
    def get_total_users(self):
        self.cursor.execute("SELECT COUNT(*) FROM products")
        return self.cursor.fetchone()[0]

    def get_user(self, id):
        self.cursor.execute("""
            select * from user where id=?
        """, (id,))
        return self.cursor.fetchone()

    def update_user(self, id, name, age, phone_number, email, photo):
        self.cursor.execute("""
            update user set name=?, age=?, phone_number=?, email=?, photo=?
            where id=?
        """, (name, age, phone_number, email, photo, id))
        self.connection.commit()

    def delete_user(self, id):
        self.cursor.execute("""
            delete from user where id=?
        """, (id,))
        self.connection.commit()



