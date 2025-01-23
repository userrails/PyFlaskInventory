from flask import Blueprint, jsonify, request, redirect, url_for
from models import db, Category

stocks_bp = Blueprint('stocks', __name__)

@stocks_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return '''
        <h1>Categories</h1>
        <ul>
            {}
        </ul>
        <a href="/categories/new">Add Category</a>
    '''.format(''.join(f'<li>{c.name} <a href="/categories/{c.id}">Show</a> <a href="/categories/{c.id}/edit">Edit</a></li>' for c in categories))

@stocks_bp.route('/categories/new', methods=['GET', 'POST'])
def new_category():
    if request.method == 'POST':
        name = request.form['name']
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('stocks.get_categories'))
    
    return '''
        <h1>Add Category</h1>
        <form method="POST">
            <label>Name:</label>
            <input type="text" name="name" required>
            <button type="submit">Save</button>
        </form>
        <a href="/categories">Back to Categories</a>
    '''

@stocks_bp.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    new_category = Category(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'id': new_category.id, 'name': new_category.name}), 201

@stocks_bp.route('/categories/<int:id>', methods=['GET'])
def get_category(id):
    category = Category.query.get_or_404(id)
    return f'''
        <h1>Category Details</h1>
        <p><strong>ID:</strong> {category.id}</p>
        <p><strong>Name:</strong> {category.name}</p>
        <a href="/categories/{category.id}/edit">Edit</a> | 
        <a href="/categories">Back to Categories</a>
    '''

@stocks_bp.route('/categories/<int:id>/edit', methods=['GET', 'POST'])
def edit_category(id):
    category = Category.query.get_or_404(id)
    
    if request.method == 'POST':
        category.name = request.form['name']
        db.session.commit()
        return redirect(url_for('stocks.get_categories'))
    
    return f'''
        <h1>Edit Category</h1>
        <form method="POST">
            <label>Name:</label>
            <input type="text" name="name" value="{category.name}" required>
            <button type="submit">Update</button>
        </form>
        <a href="/categories">Back to Categories</a>
    '''

@stocks_bp.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    category = Category.query.get_or_404(id)
    data = request.get_json()
    category.name = data['name']
    db.session.commit()
    return jsonify({'id': category.id, 'name': category.name})

@stocks_bp.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return '', 204
