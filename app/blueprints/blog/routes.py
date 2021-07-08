from flask import jsonify, render_template, url_for
from app.blueprints.main.routes import posts
from .import bp as app
# current_app gets instance of currently running app

# jsonify converts python dict to json
# @app.route('/users')
# def users():
#     return jsonify({'message': 'This works!'})

# listen in for a new route


@app.route('/post/<int:id>')
def get_post(id):
    for p in posts:
        if p['id'] == id:
            post = p
            break
    context = {
        'p': post
    }
    return render_template("blog-single.html", **context)
