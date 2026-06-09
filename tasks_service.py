from db import connect_database

def add_task(title):
    if not title.strip():
        print('Invalid title')
        return
    conn, cursor = connect_database()
    cursor.execute('''
           INSERT INTO tasks (title, is_done)
           VALUES (?, 0)
''', (title,))
    conn.commit()
    conn.close()

def get_all_tasks():
    conn, cursor = connect_database()
    cursor.execute('''
           SELECT * FROM tasks
''')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def mark_task_done(task_id):
    conn, cursor = connect_database()
    cursor.execute('''
           UPDATE tasks SET is_done = 1 WHERE id = ?
''', (task_id,))
    conn.commit()
    conn.close()
    return cursor.rowcount == 1

def delete_task(task_id):
    conn, cursor = connect_database()
    cursor.execute('''
           DELETE FROM tasks WHERE id = ?
''', (task_id,))
    conn.commit()
    conn.close()
    return cursor.rowcount == 1