import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


def get_comments(post_id):
    conn = get_db_connection()
    comments = conn.execute('SELECT * FROM comments WHERE posts_id = ?', (post_id,)).fetchall()
    return comments


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>', methods=('GET', 'POST'))
def post(post_id):
    post = get_post(post_id)
    comments = get_comments(post_id)
    if request.method == 'POST':
        author = request.form['author']
        comment = request.form['comment']
        posts_id = post_id

        if not author:
            author = "Unknown"

        if not comment:
            flash('Comment is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO comments (author, comment, posts_id) VALUES (?, ?, ?)',
                         (author, comment, posts_id))
            conn.commit()
            conn.close()
            return redirect(url_for('post', post_id=post_id))
    return render_template('post.html', post=post, comments=comments)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))


@app.route('/<int:id>/delete_comments', methods=('POST',))
def delete_comments(id):
    comments = get_comments(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM comments WHERE posts_id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Comments was successfully deleted!')
    return redirect(url_for('post', post_id=id))


if __name__ == '__main__':
    print(app.config)
    app.run(debug=True, port=5001)

