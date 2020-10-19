from yoyo import step

__depends__ = {}

steps = [
    step("CREATE TABLE users (id uuid primary key default uuid_generate_v4(),"
         " telegram_id integer,"
         " last_name text,"
         " first_name text,"
         " create_at date)",
         "DROP TABLE users")
]
