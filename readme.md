
# Recipe Management Application

A Django-based web application that allows users to create, view, update, search, and manage recipes efficiently. The application also supports image uploads, making recipe organization simple and convenient.

## Project Description

The Recipe Management Application is a full-stack web application developed using Python and Django.

It provides a platform for managing cooking recipes by storing recipe information and associated images. Users can perform CRUD (Create, Read, Update, Delete) operations and search for recipes easily.

### Key Features

- **Add Recipes:** Create and save new recipes.
- **View Recipes:** Browse and view available recipes.
- **Update Recipes:** Modify existing recipe details.
- **Delete Recipes:** Remove unwanted recipes.
- **Image Upload:** Upload and manage recipe images.
- **Search Functionality:** Search for recipes easily.
- **CRUD Operations:** Manage recipe data efficiently.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Django | Backend web framework |
| HTML | Web page structure |
| CSS | Styling and presentation |
| SQLite | Default Django database (if configured) |
| Git | Version control |
| GitHub | Repository hosting and collaboration |

## Prerequisites

Before installing the application, make sure you have the following:

- Python 3.x
- pip (Python package installer)
- Git
- Visual Studio Code or any suitable code editor
- A modern web browser

## Installation

Follow these steps to install and run the project locally.

### Step 1: Clone the repository

```bash
git clone https://github.com/Mukes-07/Receipe-Management-Application.git
```

### Step 2: Navigate to the project directory

```bash
cd Receipe-Management-Application
```

### Step 3: Create a virtual environment

```bash
python -m venv myenv
```

### Step 4: Activate the virtual environment

**For Windows:**

```bash
myenv\Scripts\activate
```

**For Linux / macOS:**

```bash
source myenv/bin/activate
```

### Step 5: Install Django

```bash
python -m pip install django
```

If a `requirements.txt` file is available, install the project dependencies using:

```bash
pip install -r requirements.txt
```

### Step 6: Navigate to the Django project directory

```bash
cd core
```

Locate the directory containing `manage.py` and execute the following commands from that directory.

### Step 7: Apply database migrations

```bash
python manage.py migrate
```

### Step 8: Start the development server

```bash
python manage.py runserver
```

### Step 9: Open the application

Open your web browser and visit:

```text
http://127.0.0.1:8000/
```

The application should now be accessible locally.

## Usage Examples

Once the application is running, users can perform the following operations:

### 1. Add a Recipe

- Open the application.
- Navigate to the recipe creation section.
- Enter the recipe details.
- Upload an image if required.
- Save the recipe.

### 2. View Recipes

- Open the recipe listing page.
- Browse the available recipes.
- Select a recipe to view its details.

### 3. Update a Recipe

- Select an existing recipe.
- Choose the edit or update option.
- Modify the required information.
- Save the changes.

### 4. Delete a Recipe

- Select the recipe to be removed.
- Choose the delete option.
- Confirm the deletion if prompted.

### 5. Search Recipes

- Use the available search functionality.
- Enter the recipe name or relevant keyword.
- View the matching results.

## Project Structure

The repository contains the following main components:

```text
Receipe-Management-Application/
│
├── core/
│   └── Django project files
│
├── .gitignore
├── README.md
└── myenv/
```

Note: The internal structure of the `core` directory contains the Django application files, configuration, views, templates, and other project resources.

## Contribution Guidelines

Contributions are welcome! Follow these steps to contribute to the project.

### Step 1: Fork the repository

Fork the original repository to your GitHub account.

Original Repository:

https://github.com/linkun42/Receipe-Management-Application

### Step 2: Clone your fork

```bash
git clone https://github.com/YOUR_USERNAME/Receipe-Management-Application.git
```

### Step 3: Create a new branch

```bash
git checkout -b feature/your-feature-name
```

### Step 4: Make your changes

Implement your improvements or bug fixes.

### Step 5: Test your changes

Run the application and verify that your modifications work correctly.

### Step 6: Stage and commit your changes

```bash
git add .
git commit -m "Describe your changes"
```

### Step 7: Push changes to GitHub

```bash
git push origin feature/your-feature-name
```

### Step 8: Create a Pull Request

- Open your fork on GitHub.
- Select the Pull Requests tab.
- Click New Pull Request.
- Select the original repository as the base repository.
- Select your fork and feature branch as the compare source.
- Provide a meaningful title and description.
- Click Create Pull Request.

Your contribution will be submitted to the original repository for review.

## License

This project is maintained in the original repository by its contributors. Refer to the repository for applicable licensing information.

## 👨Author

Developed as a Recipe Management Application using Python and Django.

---

If you find this project useful, consider giving the repository a star!