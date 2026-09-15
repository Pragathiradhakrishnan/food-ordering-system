# 🍔 Food Ordering System

A full-stack **Food Ordering System** built using **Python and Django**. The application allows users to browse food items, add items to their cart, place orders, and track their order status. An admin panel is included for managing food categories, food items, and customer orders.

## 🌐 Live Demo

**Live Website:** https://foodorderingsystem.pythonanywhere.com/

## 📌 Project Overview

The Food Ordering System is a web-based application designed to simplify the process of ordering food online.

Users can explore the available menu, select food items, add them to their cart, and place orders. Administrators can manage food items, categories, and orders through the Django admin panel.

## ✨ Features

### 👤 User Features

* Browse available food items
* View food categories
* View food item details and prices
* Add food items to cart
* Update cart items
* Place food orders
* View order details
* Track order status

### 🛠️ Admin Features

* Django Admin Panel
* Add, update, and delete food categories
* Add, update, and delete food items
* Manage customer orders
* Update order status
* Manage application data

## 📋 Order Status

Orders can be managed through different stages:

* 🕐 Pending
* 👨‍🍳 Preparing
* 🛵 Out For Delivery
* ✅ Delivered
* ❌ Cancelled

## 💻 Technologies Used

* **Python**
* **Django**
* **HTML5**
* **CSS3**
* **Bootstrap**
* **SQLite**
* **JavaScript**
* **Git & GitHub**
* **PythonAnywhere**

## 🗂️ Project Structure

```text
FoodOrderingSystem/
│
├── food/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── FoodOrderingSystem/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/FoodOrderingSystem.git
```

### 2. Navigate to the Project

```bash
cd FoodOrderingSystem
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## 🔐 Admin Panel

After creating a superuser, access the Django admin panel at:

```text
http://127.0.0.1:8000/admin/
```

From the admin panel, you can manage categories, food items, and customer orders.

## ☁️ Deployment

The project is deployed using **PythonAnywhere**.

🔗 **Live Application:** https://foodorderingsystem.pythonanywhere.com/

## 🎯 What I Learned

Through this project, I gained practical experience with:

* Django project and app structure
* Django models and database relationships
* CRUD operations
* Django forms
* User interaction and order management
* Shopping cart functionality
* Django Admin
* Template inheritance
* Static files and Bootstrap
* Database migrations
* Git and GitHub
* Deploying a Django application on PythonAnywhere

## 🔮 Future Improvements

* User authentication and personalized profiles
* Online payment integration
* Order history
* Email/SMS order notifications
* Restaurant/food search and filtering
* Improved cart and checkout experience
* Responsive UI enhancements

## 👩‍💻 Author

**Pragathi R**

Built as a practical **Python Django Full Stack Development** project.

---

⭐ If you find this project useful, feel free to star the repository!
