from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__, template_folder=os.path.join(os.getcwd()))
app.config['SECRET_KEY'] = 'secret_key'
 
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/spotlite')
def spotlite():
    return render_template('phase2artistpage.html')

@app.route('/v6')
def search():
    return render_template('ver6.html')

@app.route('/alb')
def albpage():
    return render_template('albumpage.html')

@app.route('/als')
def albsspage():
    return render_template('albumss.html')

@app.route('/abo')
def aboutspage():
    return render_template('aboutus.html')

@app.route('/pla')
def playlistpage():
    return render_template('playlist_final.html')

@app.route('/ab1')
def ab1():
    return render_template('album1.html')

@app.route('/ab2')
def ab2():
    return render_template('album2.html')

@app.route('/ab3')
def ab3():
    return render_template('album3.html')

@app.route('/se1')
def se1():
    return render_template('seca.html')

@app.route('/se2')
def se2():
    return render_template('secb.html')

@app.route('/se3')
def se3():
    return render_template('secc.html')

@app.route('/se4')
def se4():
    return render_template('secd.html')

@app.route('/se5')
def se5():
    return render_template('sece.html')

@app.route('/se6')
def se6():
    return render_template('secf.html')

@app.route('/artistpage')
def artistpage():
    return render_template('albumspage.html')

@app.route('/ravi1')
def ravi1():
    return render_template('raviartist1.html')

@app.route('/ravi2')
def ravi2():
    return render_template('raviartist2.html')

@app.route('/ravi3')
def ravi3():
    return render_template('raviartist3.html')

@app.route('/ravi4')
def ravi4():
    return render_template('raviartist4.html')

@app.route('/ravi5')
def ravi5():
    return render_template('raviartist5.html')

@app.route('/ravi')
def ravi():
    return render_template('ravimain.html')

@app.route('/raja')
def raja():
    return render_template('rajamain.html')

@app.route('/raja1')
def raja1():
    return render_template('rajaartist1.html')


@app.route('/raja2')
def raja2():
    return render_template('rajaartist2.html')


@app.route('/raja3')
def raja3():
    return render_template('rajaartist3.html')


@app.route('/raja4')
def raja4():
    return render_template('rajaartist4.html')

@app.route('/raja5')
def raja5():
    return render_template('rajaaritist5.html')



@app.route('/ara')
def ara():
    return render_template('Arijitmain.html')

@app.route('/ara1')
def ara1():
    return render_template('singhartist1.html')

@app.route('/ara2')
def ara2():
    return render_template('singhartist2.html')

@app.route('/ara3')
def ara3():
    return render_template('singhartist3.html')

@app.route('/ara4')
def ara4():
    return render_template('singhartist4.html')

@app.route('/ara5')
def ara5():
    return render_template('singhartist5.html')




@app.route('/sid')
def sid():
    return render_template('sidmain.html')

@app.route('/sid1')
def sid1():
    return render_template('sidartist1.html')

@app.route('/sid2')
def sid2():
    return render_template('sidartist2.html')

@app.route('/sid3')
def sid3():
    return render_template('sidartist3.html')

@app.route('/sid4')
def sid4():
    return render_template('sidartist4.html')

@app.route('/sid5')
def sid5():
    return render_template('sidartist5.html')




@app.route('/spb')
def spb():
    return render_template('spbmain.html')

@app.route('/spb1')
def spb1():
    return render_template('spbartist1.html')

@app.route('/spb2')
def spb2():
    return render_template('spbartist2.html')

@app.route('/spb3')
def spb3():
    return render_template('spbartist3.html')

@app.route('/spb4')
def spb4():
    return render_template('spbartist4.html')

@app.route('/spb5')
def spb5():
    return render_template('spbartist5.html')


@app.route('/add-to-playlist')
def add_to_playlist():
    song_title = request.args.get('title')
    if song_title:
        conn = sqlite3.connect('playlist.db')
        c = conn.cursor()
        c.execute('INSERT INTO songs (title) VALUES (?)', (song_title,))
        conn.commit()
        conn.close()
    return ''

@app.route('/playlist')
def playlist():
    conn = sqlite3.connect('playlist.db')
    c = conn.cursor()
    c.execute('SELECT DISTINCT title FROM songs')
    songs = [row[0] for row in c.fetchall()]
    conn.close()
    return render_template('playlist_final.html', songs=songs)

@app.route('/remove')
def remove_from_playlist():
    song_title = request.args.get('title')
    if song_title:
        conn = sqlite3.connect('playlist.db')
        c = conn.cursor()
        c.execute('''DELETE FROM songs
                WHERE title = (?)''', (song_title,))
        conn.commit()
        conn.close()
    return ''

if __name__ == '__main__':
    conn = sqlite3.connect('playlist.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS songs (title TEXT)')
    conn.commit()
    conn.close()
    app.run(debug=True, host='0.0.0.0')
