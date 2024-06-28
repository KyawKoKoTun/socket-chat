
# How To Run

1. Create a virtual environment:
   ```bash
   python -m venv env
   ```

2. Activate the virtual environment:
   ```bash
   env/Scripts/activate  # For Windows
   source env/bin/activate  # For Unix or MacOS
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize Database:
   ```bash
   # In Python Console
   from app import app, db
   with app.app_context():
     db.create_all()
   ```

6. Start the development server:
   ```bash
   python app.py
   ```

