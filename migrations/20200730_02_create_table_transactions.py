from yoyo import step

__depends__ = {'20200730_01_create_table_users'}

steps = [
    step("CREATE TABLE transactions (id uuid PRIMARY KEY,"
         "created_by uuid,"
         "created_at date,"
         "amount integer,"
         "for_what text,"
         "creditor_id uuid,"
         "debtor_id uuid,"
         "FOREIGN KEY(created_by) REFERENCES users(id),"
         "FOREIGN KEY(creditor_id) REFERENCES users(id),"
         "FOREIGN KEY(debtor_id) REFERENCES users(id))",
         "DROP TABLE transactions")
]
