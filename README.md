
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

4. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python app.py
   ```

