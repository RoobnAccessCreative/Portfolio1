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
        query = f"SELECT * FROM proj WHERE isMain = {tof} ORDER BY date DESC;"
        cur.execute(query)
        projects = cur.fetchall()

        proj_dict = {} # dictionary of a group of projects

        for proj in projects:

            proj_dict[proj[1]] = {} # nested dict for individual project

            # fills the dict with key/value pairs
            proj_dict[proj[1]]['image'] = proj[2]
            proj_dict[proj[1]]['logo'] = proj[3]
            proj_dict[proj[1]]['bio'] = proj[bio_num]
            proj_dict[proj[1]]['github'] = proj[6]
            proj_dict[proj[1]]['figma'] = proj[7]
            proj_dict[proj[1]]['date'] = proj[9]

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
