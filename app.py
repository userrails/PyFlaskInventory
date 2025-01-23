from flask import Flask, redirect, url_for
from config import Config
from models import db
from stocks.routes import stocks_bp

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return redirect(url_for('stocks.get_categories', _external=True))
    
    app.config.from_object(Config)
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(stocks_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=3000)
