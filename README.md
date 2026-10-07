# Enhanced Calculator

An enhanced command-line calculator built in Python for IS601: Python for Web API Development.

The application supports multiple arithmetic operations, persistent calculation history, undo and redo functionality, automatic history saving, environment-based configuration, and several object-oriented design patterns. Automated testing is implemented with pytest and maintains 100% test coverage.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Power calculations
- Root calculations
- Interactive command-line REPL
- Calculation history using pandas
- Save and load history using CSV files
- Automatic history saving
- Undo and redo functionality
- Environment variable configuration with python-dotenv
- Input validation and error handling
- Automated testing with pytest
- 100% test coverage
- Continuous Integration with GitHub Actions

## Project Structure

```text
module5_is601/
├── .github/
│   └── workflows/
│       └── tests.yml
├── app/
│   ├── __init__.py
│   ├── calculation.py
│   ├── calculator.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── calculator_repl.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   ├── observers.py
│   └── operations.py
├── data/
├── tests/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Design Patterns

The calculator uses several software design patterns to keep the application modular and maintainable.

### Strategy Pattern

Arithmetic operations are implemented as separate strategy classes. This allows the calculator to perform different operations through a common interface.

### Factory Pattern

`CalculationFactory` creates calculation objects based on the requested operation.

### Facade Pattern

The `Calculator` class provides a simplified interface for calculations, history management, undo/redo, and saving or loading history.

### Observer Pattern

Observers respond to calculator events. This is used for functionality such as logging and automatic history saving.

### Memento Pattern

The Memento pattern stores previous history states, allowing the user to undo and redo changes without exposing the internal implementation of the history object.

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/kak67-netizen/module5_is601.git
cd module5_is601
```

Create a Python virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Environment Configuration

The project includes an `.env.example` file containing the supported configuration options.

Create your local `.env` file:

```bash
cp .env.example .env
```

Example configuration:

```text
CALCULATOR_HISTORY_FILE=data/history.csv
CALCULATOR_AUTO_SAVE=true
```

## Running the Calculator

From the project root, run:

```bash
python -m app.calculator_repl
```

The calculator will start an interactive REPL where you can enter operations and commands.

## Calculator Operations

The following arithmetic operations are supported:

```text
add
subtract
multiply
divide
power
root
```

After selecting an operation, enter the two requested numeric values.

## REPL Commands

The calculator also supports these commands:

```text
help
history
clear
undo
redo
save
load
exit
```

- `help` displays available operations and commands.
- `history` displays previous calculations.
- `clear` removes calculation history.
- `undo` restores the previous history state.
- `redo` reapplies an undone history state.
- `save` saves history to the configured CSV file.
- `load` loads history from the configured CSV file.
- `exit` closes the calculator.

## Testing

Run all automated tests with:

```bash
python -m pytest
```

Run the complete test suite with coverage:

```bash
python -m pytest --cov=app --cov-report=term-missing --cov-fail-under=100 tests/
```

The project is configured to require 100% test coverage.

## Continuous Integration

GitHub Actions automatically runs the test suite whenever code is pushed to the `main` branch or a pull request is opened against `main`.

The workflow installs the required dependencies, runs pytest, calculates code coverage, and fails if coverage drops below 100%.

## Error Handling

The calculator validates user input and handles errors such as:

- Invalid numeric input
- Unsupported operations
- Division by zero
- Invalid root calculations
- History save or load failures
- Invalid configuration values

This prevents common errors from unexpectedly terminating the application.

## Technologies

- Python
- pandas
- python-dotenv
- pytest
- pytest-cov
- Git
- GitHub
- GitHub Actions