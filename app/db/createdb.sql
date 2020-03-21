create table users
(
    id integer primary key,
    telegram_id integer,
    last_name varchar(255),
    first_name varchar(255),
    created_at date
);

create table transactions
(
    id integer primary key,
    created_by integer,
    created_at date,
    amount integer,
    creditor_id integer,
    debtor_id integer,
    -- negotiation_status ENUM ('A',  'B',  'C'),
    FOREIGN KEY(created_by) REFERENCES users(id),
    FOREIGN KEY(creditor_id) REFERENCES users(id),
    FOREIGN KEY(debtor_id) REFERENCES users(id)
);