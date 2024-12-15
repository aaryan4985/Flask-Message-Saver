# 📩 Flask Message Saver

A basic **Flask web application** that allows users to submit messages, view all saved messages, and clear them. This project demonstrates form handling, SQLite database integration, and Flask routing.

---

## 🚀 Features

- **Submit Messages**: Users can submit their name and a message.
- **View Messages**: View all stored messages in a list format.
- **Clear Messages**: Admin can clear all saved messages from the database.
- **Easy Navigation**: Includes Home, About, Contact, and Messages pages.
- **Lightweight & Beginner-Friendly**: A perfect project to learn Flask and SQLite basics.

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS (basic templates)

---

## 📂 Project Structure

```
message-collector/
│
├── templates/
│   ├── home.html            # Home page template
│   ├── about.html           # About page template
│   ├── contact.html         # Form for submitting messages
│   └── messages.html        # Displays all messages
│
├── app.py                   # Main Flask application
├── messages.db              # SQLite database file (auto-generated)
└── README.md                # Project documentation
```

---

## 🔧 Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone [<repo-url>](https://github.com/aaryan4985/Flask-Message-Saver.git)
   cd Flask-Message-Saver
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate       # On macOS/Linux
   venv\Scripts\activate          # On Windows
   ```

3. **Install Flask**:
   ```bash
   pip install flask
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the Application**:
   - Open your browser and visit `http://127.0.0.1:5000/`

---

## 📝 Usage

1. **Home Page**:
   - Start from the home page (`/`).

2. **About Page**:
   - Navigate to `/about` for general information.

3. **Submit Messages**:
   - Go to `/contact` and fill in the **Name** and **Message** form.
   - Submit the form, and your message will be saved in the database.

4. **View Messages**:
   - Visit `/messages` to view all submitted messages.

5. **Clear Messages**:
   - Go to `/messages` and click on the **Clear Messages** button to delete all entries.

---

## 🛠️ Database Schema

The database is auto-created (`messages.db`) with the following table:

| Column | Type     | Constraints     |
|--------|----------|-----------------|
| id     | INTEGER  | Primary Key, Auto-increment |
| name   | TEXT     | Not Null        |
| message| TEXT     | Not Null        |

---

## 📜 Future Improvements

Here are some ideas to enhance the project:

1. **Authentication**: Add login for admins to clear messages.
2. **Pagination**: Add pagination to display messages in chunks.
3. **Improved UI**: Style the pages with Bootstrap or Tailwind CSS.
4. **Message Editing**: Allow users to edit or delete their messages.
5. **Email Integration**: Send confirmation emails to users after submission.

---

## 💡 Learning Outcomes

This project helps you learn:

- Setting up a **Flask** application.
- Using **SQLite** for data storage.
- Handling **form submissions** securely.
- Rendering dynamic content with Flask templates.
- Managing **GET and POST routes** in Flask.

---

## 👤 Author

- Aaryan Pradhan
- GitHub: [[Your GitHub Profile](#)](https://github.com/aaryan4985)
- Email: pradhanaaryan@gmail.com

---

## 📜 License

This project is licensed under the MIT License.

