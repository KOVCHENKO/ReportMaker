import pymysql

from settings.settings import host, user, passwd, db, port


def user_payments_request():
    conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=port)
    cursor = conn.cursor()
    cursor.execute('''select contractors.title, users.id, users.email, contractors.name, rates.title, parents_payments.payment, parents_payments.finish, parents_groups.title, 
            (select count(*) from sys_log where element = 'user_login' and text = users.id) as entries
            from users
            join parents_schools on parents_schools.user_id = users.id
            join contractors on parents_schools.contractor_id = contractors.id
            join parents_payments on parents_payments.user_id = users.id
            join rates on rates.id = parents_payments.rate_id
            join parents_in_groups on parents_in_groups.parent_id = users.id
            join parents_groups on parents_groups.id = parents_in_groups.group_id
            where parents_payments.state = 'on'
            and users.state <> 'blocked'
            and CURRENT_DATE < parents_payments.finish
            order by contractors.id, parents_payments.payment''')
    data = cursor.fetchall()
    conn.close()

    return data
