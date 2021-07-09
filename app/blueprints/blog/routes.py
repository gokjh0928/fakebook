from flask import jsonify, render_template, url_for, redirect
from app.blueprints.blog.models import Post
from .import bp as app
# current_app gets instance of currently running app

# jsonify converts python dict to json
# @app.route('/users')
# def users():
#     return jsonify({'message': 'This works!'})

# listen in for a new route


@app.route('/post/<int:id>')
def get_post(id):
    context = {
        'p': Post.query.get(id)
    }
    return render_template("blog-single.html", **context)
