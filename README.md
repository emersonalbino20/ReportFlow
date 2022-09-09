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

## Usage

Run the application:

```
python3 main.py
```

The system simulates REST-like operations through function calls, allowing you to:

- Create users (professor / coordinator)
- Authenticate users
- Create and manage reports
- Filter reports based on user roles

## License

**GNU General Public License:**

- [x] Commercial use
- [x] Modification
- [x] Distribution
- [x] Patent use
- [x] Private use

## Contact

Email: emersonalbino019@gmail.com
