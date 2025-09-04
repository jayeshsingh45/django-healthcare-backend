
-----

## Healthcare Backend API

A **Django-based** healthcare backend system with **JWT authentication**, **patient and doctor management**, and **patient-doctor mapping** functionality.

### Setup Instructions

Follow these steps to set up and run the project locally.

#### 1\. Create and Activate Virtual Environment

A **virtual environment** isolates your project's dependencies from other Python projects.

  * To create a virtual environment, run:
    ```bash
    python3 -m venv venv
    ```
  * To activate it, use one of the following commands based on your operating system:
      * **Linux**:
        ```bash
        source venv/bin/activate
        ```
      * **Windows**:
        ```bash
        venv\Scripts\activate
        ```

#### 2\. Install Dependencies

Install the necessary Python packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

#### 3\. Configure Environment Variables

Create a **`.env`** file inside the `healthcare` folder and add the following configuration. Replace the placeholder values with your specific database and secret key information.

```bash
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_user_pass
DB_HOST=127.0.0.1
DB_PORT=5432
DB_SSLMODE=verify-ca
DB_SSLROOTCERT=root.crt
DB_SSLCERT=server.crt
DB_SSLKEY=server.key
DJANGO_SECRET_KEY=your_django_secret_key
```

#### 4\. Run the Development Server

Once everything is configured, you can start the Django development server.

```bash
python manage.py runserver
```

-----

**Thank You\!** ❤️

-----