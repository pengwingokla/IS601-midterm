# Advanced Python Calculator for Software Engineering Graduate Course

## Project Overview

This midterm requires the development of an advanced Python-based calculator application. Designed to underscore the importance of professional software development practices, the application integrates clean, maintainable code, the application of design patterns, comprehensive logging, dynamic configuration via environment variables, sophisticated data handling with Pandas, and a command-line interface (REPL) for real-time user interaction.
## Instructor Video - [here](https://youtu.be/hu9YFdeSkV8)

## Project Submission

- Create a NEW repository from scratch and transfer any relevant work as you complete the assignment, **you need to show a clear history of work through your commits, or your project could be given as low as a 0 for not showing your work.**
- Submit through a GitHub repository link containing the necessary documentation, configuration examples, and a coherent commit history.
- You are required to write a short description and link to your implememtation of the design patterns you use.
- You need to provide a description of how you used environment variables and link to your code to illustrate.
-  You need to explain and link to how you are using logging.
-  You need to link to and explain how you are using try/catch / exceptions to illustrate  "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP)/
- Create a 3-5 minute video demonstration of using the calculator, highlighting its key features and functionalities. Link the video to the repository readme.
-  Submit a link to your repository to Canvas.  
-  Keep your repository private while working on it, so people don't copy your work.  Make the repository public within a day of the project being due, so we can grade it.
- **REQUIRED - YOU MUST USE GITHUB ACTIONS AND YOUR CODE MUST PASS ALL THE TESTS ON GITHUB**

## Core Functionalities

### Command-Line Interface (REPL)

Implement a Read-Eval-Print Loop (REPL) to facilitate direct interaction with the calculator. This interface should support:
- Execution of arithmetic operations (Add, Subtract, Multiply, and Divide)
- Management of calculation history.
- Access to extended functionalities through dynamically loaded plugins.

#### Checklist:
✅ REPL implemented in `app/__init__.py`.
<br>✅ Supports arithmetic operations (`add`, `sub`, `mul`, `div`).
<br>✅ Manages calculation history via `HistoryManager`.
<br>✅ Loads plugins dynamically via `load_plugins()`.

### Plugin System

Create a flexible plugin system to allow seamless integration of new commands or features. This system should:
- Dynamically load and integrate plugins without modifying the core application code.
- Include a REPL  "Menu" command to list all available plugin commands, ensuring user discoverability and interaction.

#### Checklist:
✅ Plugins dynamically loaded from `app/plugins/`.
<br>✅ Commands from plugins can be executed without modifying core code.
<br>✅ Implemented a `menu` command that lists available commands.

### Calculation History Management with Pandas

Utilize Pandas to manage a robust calculation history, enabling users to:
- Load, save, clear, and delete history records through the REPL interface.

#### Checklist:
✅ Pandas used to manage history (`history_manager.py`).
<br>✅ Supports `history`, `clrhis`, and `delhis` commands.
<br>✅ History is saved to and loaded from CSV using Pandas.

### Professional Logging Practices

Establish a comprehensive logging system to record:
- Detailed application operations, data manipulations, errors, and informational messages.
- Differentiate log messages by severity (INFO, WARNING, ERROR) for effective monitoring.
- Dynamic logging configuration through environment variables for levels and output destinations.

#### Checklist:
✅ Implemented logging (`logging.conf`, logging statements across modules).
<br>✅ Logs different severity levels (`INFO`, `WARNING`, `ERROR`).
<br>✅ Dynamic logging configuration through environment variables (`load_dotenv()`).

### Advanced Data Handling with Pandas

Employ Pandas for:
- Efficient data reading and writing to CSV files.
- Managing calculation history.

#### Checklist:
✅ Efficient data reading/writing using Pandas (`history_manager.py`).
<br>✅ History stored in CSV (`data/history.csv`).
<br>✅ Supports CRUD operations on history (Load, Save, Clear, Delete records).

### Design Patterns for Scalable Architecture
#### Checklist:
Incorporate key design patterns to address software design challenges, including:
<br>✅ **Facade Pattern:** Offer a simplified interface for complex Pandas data manipulations.
<br>✅ **Command Pattern:** Structure commands within the REPL for effective calculation and history management.
<br>✅ **Factory Method, Singleton, and Strategy Patterns:** Further enhance the application's code structure, flexibility, and scalability.
