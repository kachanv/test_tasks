# -*- coding: utf-8 -*-


def create_data(sql_conn):
    with sql_conn.cursor() as cursor:
        sql_conn.autocommit = True

        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS postgres.public.users
            (
                id_user serial PRIMARY KEY,
                name VARCHAR (50) UNIQUE NOT NULL
            );
            ''')

        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS postgres.public.computers
            (
                comp_id SERIAL PRIMARY KEY,
                id_user INTEGER REFERENCES users(id_user),
                comp_name VARCHAR (50) UNIQUE NOT NULL
            );
            ''')

        cursor.execute(
            '''
            INSERT INTO postgres.public.users
                (name)
            VALUES
                ('user_1'),
                ('user_2'),
                ('user_3'),
                ('user_4'),
                ('user_5'),
                ('user_6'),
                ('user_7'),
                ('user_8'),
                ('user_9'),
                ('user_10'),
                ('user_11'),
                ('user_12'),
                ('user_13'),
                ('user_14'),
                ('user_15'),
                ('user_16'),
                ('user_17'),
                ('user_18'),
                ('user_19'),
                ('user_20'),
                ('user_21'),
                ('user_22'),
                ('user_23'),
                ('user_24'),
                ('user_25'),
                ('user_26'),
                ('user_27'),
                ('user_28'),
                ('user_29'),
                ('user_30');
            '''
        )

        cursor.execute(
            '''
            INSERT INTO postgres.public.computers 
                (id_user, comp_name)
            VALUES
                (1,'comp_name_1'),
                (2,'comp_name_2'),
                (3,'comp_name_3'),
                (14,'comp_name_4'),
                (5,'comp_name_5'),
                (14,'comp_name_6'),
                (1,'comp_name_7'),
                (8,'comp_name_8'),
                (9,'comp_name_9'),
                (10,'comp_name_10'),
                (14,'comp_name_11'),
                (12,'comp_name_12'),
                (13,'comp_name_13'),
                (14,'comp_name_14'),
                (15,'comp_name_15'),
                (1,'comp_name_16'),
                (17,'comp_name_17'),
                (18,'comp_name_18'),
                (30,'comp_name_19'),
                (20,'comp_name_20'),
                (21,'comp_name_21'),
                (22,'comp_name_22'),
                (23,'comp_name_23'),
                (1,'comp_name_24'),
                (25,'comp_name_25'),
                (30,'comp_name_26'),
                (27,'comp_name_27'),
                (1,'comp_name_28'),
                (29,'comp_name_29'),
                (30,'comp_name_30');
            '''
        )
