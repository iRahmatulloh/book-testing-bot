import psycopg2host="localhost"port="5432"user="postgres"password="0571"database="management"connection = psycopg2.connect(database=database, user=user, host=host, port=port, password=password)cur = connection.cursor()# cur.execute("select correct, variant from questions, answer_issue")cur.execute("""SELECT id_issue, correct, task_num, variantFROM questionsINNER JOIN answer_issue ON id_issue = task_num;""")# cur.execute("select * from answer_issue")print(cur.fetchall()[0])