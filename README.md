# Visitor Counter

This project implements a real-time visitor counter using Flask for the backend and Svelte for the frontend. The counter records unique visits by IP address and automatically updates the number of visitors on the page.

## Features

- Unique visitor tracking by IP address.
- Real-time visitor count updates using Socket.IO.
- Simple and attractive interface built with Svelte.

## Technologies Used

- **Backend**: Flask, Flask-SocketIO, Flask-CORS, dotenv
- **Frontend**: Svelte, Socket.IO Client
- **Storage**: Text files for logging visitors and IP addresses

## Requirements

- Python 3.6 or higher
- Node.js 14 or higher
- An appropriate development environment (you can use `venv` for the backend and a package manager like `npm` for the frontend)

## Installation

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd visitor-counter
```

### 2. Set Up the Backend

1. Navigate to the backend directory:

```bash
cd backend
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the backend directory with the following content:

```plaintext
HOST=127.0.0.1
PORT=5000
```

### 3. Set Up the Frontend

1. Navigate to the frontend directory:

    ```bash
    cd ../frontend
    ```

2. Install the required dependencies:

    ```bash
    npm install
    ```

## Running the Application

### 1. Start the Backend

Navigate to the backend directory and run the server:

```bash
cd backend
python app.py
```

### 2. Start the Frontend

Open another terminal, navigate to the frontend directory, and run the Svelte application:

```bash
cd frontend
npm run dev
```

## Usage

1. Open your browser and visit `http://localhost:5000` (or the port you have configured).
2. The visitor counter should display the number of unique visitors in real-time.
   
## Contributions

If you want to contribute to this project, feel free to open an **issue** or submit a **pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.