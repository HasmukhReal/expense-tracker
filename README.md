# Expense Tracker (CLI)

A simple command-line expense tracker written in Python that allows users to record daily expenses, view them by date, and store them in a text file.

## Screenshots
<p align="center">
  <img width="570" height="317" alt="image" src="https://github.com/user-attachments/assets/718a9c7a-c6df-4408-a2b5-78e1f7810d1f" />
  <br>
  <em>Main Menu</em>
</p>
<p align="center">
  <img width="693" height="348" alt="image" src="https://github.com/user-attachments/assets/4387c41a-3976-4330-9bc6-b1b0b4be7641" />
  <br>
  <em>Adding Mode</em>
</p>
<p align="center">
  <img width="356" height="260" alt="image" src="https://github.com/user-attachments/assets/b9d0cc48-11e7-417d-a236-8a87c2c502ad" />
  <br>
  <em>Viewing Mode with empty/no file</em>
</p>
<p align="center">
  <img width="1081" height="235" alt="image" src="https://github.com/user-attachments/assets/db503954-cf22-4262-80e9-391b406b4e45" />
  <br>
  <em>Quit without save warning</em>
</p>
<p align="center">
  <img width="589" height="934" alt="image" src="https://github.com/user-attachments/assets/d4a9652e-35c6-4f27-9966-d5457bf2be4c" />
  <br>
  <em>Viewing Mode</em>
</p>

## Status

This project is actively being improved and developed as I learn more Python and software development concepts.

## Features

- Add expenses with amount and reason
- View expenses grouped by date
- Save expenses to a file
- Load existing expenses from file
- Simple CLI menu system

## File Format

Expenses are stored in `data.txt` using this format:

`date|amount|reason`

Example:

```
12-12-2025|120|food
12-12-2025|50|bus
```

## Project Structure

```
expense-tracker
│
├── main.py      # Main program
├── data.txt     # Expense data
└── README.md    # Project documentation
```

## Installation

Clone the repository:

```bash
git clone https://github.com/HasmukhReal/expense-tracker.git
cd expense-tracker
```

## How to Run

1. Make sure Python is installed
2. Run the script:

```bash
python main.py
```

## Technologies Used

- Python
- File Handling
- Command Line Interface (CLI)

## Future Improvements

### Project Structure
- Modular Project Structure

### Core Features
- Show total expenses per day
- Edit expenses
- Search expenses
- Input validation

### Data Improvements
- CSV support
- Backup file
- AutoSave

### Analytics
- Graphs and charts
- Trend lines & pie charts
- Automatic Daily Summary (Using Real-Date and Real-Time)
- Monthly summary reports

### UI Improvements
- Back option in every screen
- Clean CLI dashboard
- Colored CLI Interface

### Advanced Features
- Budget alerts
- Category tracking
