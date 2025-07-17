# Invoice Generator

This project is a Django-based invoice generator for managing products and invoices.

## Setup Instructions

### Prerequisites

- Python 3.10+
- pip
- (Recommended) Virtual environment tool: `venv`

### Installation

1. **Clone the repository**

   ```sh
   git clone https://github.com/Malfioso/generateur_facture.git
   cd generateur_facture
   ```

2. **Create and activate a virtual environment**

   ```sh
   python -m venv env
   # On Windows:
   env\Scripts\activate
   # On macOS/Linux:
   source env/bin/activate
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```sh
   python invoice/manage.py migrate
   ```

5. **Create a superuser (for admin access)**

   ```sh
   python invoice/manage.py createsuperuser
   ```

6. **Run the development server**

   ```sh
   python invoice/manage.py runserver
   ```

7. **Access the application**
   - Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to manage products and invoices.

## Project Structure

- `invoice/` : Django project folder
- `products/` : Django app for products and invoices
- `requirements.txt` : Python dependencies
- `env/` : Virtual environment (not tracked by git)

## Useful Commands

- Run tests: `python invoice/manage.py test`
- Create migrations: `python invoice/manage.py makemigrations`

## License

MIT
