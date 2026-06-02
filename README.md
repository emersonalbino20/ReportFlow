# ReportFlow

<div style="text-align: justify;">

This project is a simple simulation of client-server communication, inspired by a real-world problem related to managing daily teaching reports.

While working as an English teacher in residential settings, I noticed that instructors were required to send daily reports via WhatsApp. Although functional, this approach becomes inefficient as the number of teachers and lessons increases.

With more than 10 teachers, each handling multiple weekly sessions across different residences, tracking report submissions and ensuring consistency becomes challenging. Questions like “How many reports has each teacher submitted this week?” are difficult to answer with this method.

To address this, I started building this project as an MVP using Python. The goal is to simulate a structured system for managing users and reports, while practicing core backend concepts such as CRUD operations, validation, and REST-like architecture.

This project represents a learning step toward building a more robust and scalable platform in the future.

</div>

## Installation

### Prerequisites

You should have Python 3 installed and a programming environment set up on your computer or server.

1. **Clone the repository:**

   ```
   git clone git@github.com:emersonalbino20/ReportFlow.git
   ```

2. **Navigate to the project directory:**

   ```
   cd ReportFlow/
   ```

3. **Install dependencies (if any):**

   ```
   pip install -r requirements.txt
   ```
4. **Run for the first time**

   ```
   python3 main.py
   ```
5. **Open manually the db and introduce the first user**

   open file data/db.json and copy/paste the content below:
   ```
   {
    "users": [
        {
            "id": 1,
            "name": "emerson",
            "email": "emerson@gmail.com",
            "password": "1234",
            "role": "coordinator"
        }
    ],
    "reports": []
   }
   ```
6. **Run and log**
   ```
   python3 main.py
   ```
## Project structure

```
.
├── data
│   └── db.json
├── db
│   └── init.py
├── LICENSE
├── main.py
├── menus
│   ├── flow.py
│   ├── main_menu.py
│   ├── report_menu.py
│   └── user_menu.py
├── models
│   ├── report.py
│   └── user.py
├── README.md
├── requirements.txt
├── services
│   ├── auth_service.py
│   ├── report_service.py
│   └── user_service.py
├── utils
│   ├── clean.py
│   ├── connect.py
│   ├── utils.py
│   └── validators.py
└── views.py
```

## User Profile

### Coordinator

The coordinator is the main user who can:
- Add users:
   - coodinator
   - teacher
- List users
- List reports
   - Filter by teacher
   - Filter by date

### Teacher

The teacher is secondary user who can:
- Add report
- List their report

## Contribute

1. Fork the repository
2. Clone your fork locally
3. Create a new branch based on **main**:

   ```
    git checkout main
    git pull origin main
    git checkout -b your-feature-name
   ```
4. Make your changes and commit them
5. Push the branch to your fork
6. Open a Pull Request describing your changes following the conventional commits of the project

## Future Features

Future improvements may include:
- Migration from JSON storage to one DB manager
- Encrypt password
- Delete User
- Delete Report
- ...

## Resources

   * https://roadmap.sh/python
   * https://www.digitalocean.com/community/tutorial-series/how-to-code-in-python-3
   * https://youtu.be/4rmBOxn0PdI?si=X5yiiPtjbWNtraC4
   * https://www.conventionalcommits.org/en/v1.0.0/

## License

**GNU General Public License:**

- [x] Commercial use
- [x] Modification
- [x] Distribution
- [x] Patent use
- [x] Private use

## Contact

Email: emersonalbino019@gmail.com

LinkedIn: https://www.linkedin.com/in/emerson-albino-241390251/
