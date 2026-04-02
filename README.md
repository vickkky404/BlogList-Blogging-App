# BlogList

A modern, minimal, and aesthetic Django-based blogging platform where users can create, read, edit, and delete blog posts.

## ✨ Features

- **User Authentication** - Secure signup and login system
- **Create Posts** - Write and publish blog posts
- **Search Functionality** - Search posts by title, content, or author
- **Sort Options** - Sort posts by newest or oldest
- **Edit & Delete Posts** - Manage your own posts
- **Reading Time & Word Count** - Automatic calculation for each post
- **Post Preview** - See preview of posts on homepage
- **Dashboard Analytics** - View total posts and active users
- **Responsive Design** - Works perfectly on all devices
- **Dark Mode Support** - Automatic dark mode based on system preference
- **Professional UI** - Minimal and aesthetic design

## 🛠️ Tech Stack

- **Backend**: [Django](https://www.djangoproject.com/)
- **Frontend**: HTML5, CSS3, Bootstrap 4
- **Database**: SQLite3
- **Python**: 3.8+

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/BlogList.git
cd BlogList
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply migrations**
```bash
python manage.py migrate
```

5. **Run the development server**
```bash
python manage.py runserver
```

6. **Access the application**
Open your browser and navigate to `http://127.0.0.1:8000`

## 🚀 Usage

### Creating an Account
1. Go to the signup page
2. Enter your name, email, and password
3. Click "Sign Up"
4. You'll be redirected to login page

### Creating a Post
1. Login to your account
2. Click "New Post" in the navbar
3. Enter post title and content
4. Click "Publish Post"

### Searching Posts
1. Use the search bar in the navbar
2. Search by post title, content, or author name
3. Use sorting options (Newest/Oldest)

### Managing Your Posts
1. Go to "My Posts" section
2. View all your published posts
3. Click "Edit" to modify a post
4. Click "Delete" to remove a post

## 📁 Project Structure

```
BlogList/
├── blog/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   ├── auth.css
│   │   │   ├── home.css
│   │   │   └── posts.css
│   │   └── image/
│   ├── templates/
│   │   └── blog/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── signup.html
│   │       ├── newpost.html
│   │       ├── mypost.html
│   │       └── editpost.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── blog_app/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── db.sqlite3
```

## 🎨 Design Features

- **Minimal Aesthetic** - Clean and simple user interface
- **Professional Colors** - Blue gradient theme with consistent styling
- **Smooth Animations** - Hover effects and transitions
- **Dark Mode** - Automatic dark mode support
- **Mobile Responsive** - Optimized for all screen sizes

## 📝 Models

### Post Model
- `title` - Blog post title
- `content` - Blog post content
- `author` - User who created the post
- `date_posted` - Date and time when post was created

## 🔐 Security

- User authentication required for creating/editing/deleting posts
- Only post authors can edit or delete their posts
- CSRF protection enabled
- Secure password hashing

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created with ❤️ by BlogList Team

## 📧 Support

For support, open an issue in the repository.

---

**Happy Blogging!** 📝✨
