from yoyo import step

__depends__ = {}

steps = [
    step("CREATE TABLE users (id integer PRIMARY KEY,"
         " telegram_id integer,"
         " last_name text,"
         " first_name text,"
         " create_at date)",
         "DROP TABLE users")
]
