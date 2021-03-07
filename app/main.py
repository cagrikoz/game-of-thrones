import mysql.connector
from flask import Flask

app = Flask(__name__)

def executeQuery(query):
    try:
        db = mysql.connector.connect(user='root',
                             passwd='Asdqwe234',
                             host='localhost',
                             port='3306',
                             database='imdb',
                             auth_plugin='mysql_native_password')
        cur = db.cursor()
        cur.execute(query)
        print("executed")
        return cur.fetchall()
    except Exception as err:
        print(err)

@app.route('/')
def get_data():
    rows = """
    <html>
    <head>
    <title>Game of Thrones</title>
    </head>
    <body>
    <table border="1">
    <tr>
    <td width="125" height="25" bgcolor="#550000" align="center"><font color="#ffffff">Order</font></td>
    <td width="125" bgcolor="#550000" align="center"><font color="#ffffff">Title</font></td>
    <td width="125" bgcolor="#550000" align="center"><font color="#ffffff">Season</font></td>
    <td width="125" bgcolor="#550000" align="center"><font color="#ffffff">Episode</font></td>
    <td width="125" bgcolor="#550000" align="center"><font color="#ffffff">Average Rating</font></td>
    </tr>"""
    try:
        query = """select tb.primary_title, te.season_number, te.episode_number, tr.average_rating from 
        imdb.title_episode te inner join imdb.title_ratings tr on tr.tconst = te.tconst
        inner join imdb.title_basics tb on tb.tconst = te.tconst 
        where te.parent_tconst = 'tt0944947' order by tr.average_rating desc;"""
        result = executeQuery(query)
        k = 1
        for i in result:
            row = """
                    <tr>
                    <td height="25" align="center">{0}</td>
                    <td align="center">{1}</td>
                    <td align="center">{2}</td>
                    <td align="center">{3}</td>
                    <td align="center">{4}</td>
                    </tr>""".format(k, i[0], i[1], i[2], i[3])
            rows += row
            k += 1
        rows += """
        </table>
        </body>
        </html>"""
        return rows

    except Exception as err:
        print(err)