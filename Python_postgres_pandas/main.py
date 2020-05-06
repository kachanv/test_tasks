# -*- coding: utf-8 -*-
import psycopg2
import pandas
from tabulate import tabulate

from custom_tools import create_data


def print_df(df, header='Table'):
    return print('\n{}: \n'.format(header), tabulate(df, headers='keys', tablefmt='psql'))


if __name__ == '__main__':

    # postgres select data
    conn = psycopg2.connect(dbname='postgres', user='admin', password='example', host='localhost')
    #create_data(sql_conn=conn)
    user_select = 'SELECT id_user, name FROM postgres.public.users;'
    computer_select = 'SELECT comp_name, id_user FROM postgres.public.computers;'

    # pandas transform data
    df_user = pandas.read_sql_query(user_select, conn)
    df_computer = pandas.read_sql_query(computer_select, conn)
    df_union = pandas.merge(df_user, df_computer, on='id_user', how='outer')
    user_comp_cnt = df_union.groupby(['name'])['comp_name'].nunique().sort_values(ascending=False).to_frame(). \
        rename(columns={'comp_name': 'computers_count'}).rename_axis(index={'name': 'user_name'})

    # display data
    print_df(df=user_comp_cnt, header='Computers per users:')
    print_df(df=user_comp_cnt.query('computers_count == 0'), header='Users without computers:')
    print_df(df=user_comp_cnt[:3], header='TOP 3 users with max count of computers:')
