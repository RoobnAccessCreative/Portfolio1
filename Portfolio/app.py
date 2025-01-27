from flask import Flask, render_template
import sqlite3 as sql

def queries(tof, bio_num):
    # Queries projects.db for project info for either 'Main Features'
    # section or 'Other Recents' in projects.html.
    # @param tof - bool value (1 or 0), relates to either
    # aforementioned section.
    # @param bio_num - 4 or 5, relates to either
    # mainBio or bio column in 'projects.db'.
    conn = sql.connect('projects.db')
    
    with conn:

        cur = conn.cursor()

        # Safe parameterized query
        # despite no ueser input - no reason not to
        query = "SELECT * FROM proj WHERE isMain = ? ORDER BY date DESC;"
        cur.execute(query, (tof,))
        projects = cur.fetchall()

        proj_dict = {}

        for proj in projects:
            proj_dict[proj[1]] = {
                # name can be accessed when looping
                'image': proj[2],
                'logo': proj[3],
                'bio': proj[bio_num], # proj[4 or 5]
                'github': proj[6],
                'figma': proj[7],
                'date': proj[9] # proj[8] is 'isMain' which doesn't need to be taken
            }

        return proj_dict
   
            

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/profile')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects(): 
    main = queries(1, 4)
    recents = queries(0, 5)
    return render_template('projects.html', main=main, rec=recents)


if __name__ == '__main__':
    app.run(debug=True)
