import sqlite3, sys
conn = sqlite3.connect('food.db')
curs = conn.cursor()

query = "SELECT * FROM FOOD WHERE " + sys.argv[0]
print(query)
curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print('{}:{}'.format(*pair))
    print()