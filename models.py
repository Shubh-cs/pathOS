from database import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        deadline TEXT,
        category TEXT,
        goal_id INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        importance INTEGER,
        status TEXT DEFAULT 'todo',
        event_id INTEGER,
        task_deadline TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_goal(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO goals (name) VALUES (?)",
        (name,)
    )

    conn.commit()
    conn.close()

def get_goals():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM goals")
    goals = cursor.fetchall()

    conn.close()
    return goals

def add_event(name, deadline, category, goal_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO events (name, deadline, category, goal_id)
        VALUES (?, ?, ?, ?)
        """,
        (name, deadline, category, goal_id)
    )

    conn.commit()
    conn.close()
    
def get_events(goal_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM events WHERE goal_id = ?",
        (goal_id,)
    )

    events = cursor.fetchall()

    conn.close()
    return events