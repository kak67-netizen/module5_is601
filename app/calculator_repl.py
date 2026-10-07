"""Command-line REPL interface for the calculator."""

from app.calculator import Calculator
from app.input_validators import validate_number


HELP_TEXT = """
Available operations:
  add
  subtract
  multiply
  divide
  power
  root

Available commands:
  help     Show this help menu
  history  Display calculation history
  clear    Clear calculation history
  undo     Undo the last history change
  redo     Redo the last undone change
  save     Save history to CSV
  load     Load history from CSV
  exit     Exit the calculator
"""


def run_repl() -> None:
    """Run the calculator Read-Eval-Print Loop."""
    calculator = Calculator()

    print("Enhanced Calculator")
    print("Type 'help' to see available commands.")

    while True:
        try:
            command = input("\nEnter operation or command: ").strip().lower()

            if command == "exit":
                print("Goodbye!")
                break

            if command == "help":
                print(HELP_TEXT)
                continue

            if command == "history":
                if calculator.history.data.empty:
                    print("History is empty.")
                else:
                    print(calculator.history.data)
                continue

            if command == "clear":
                calculator.clear_history()
                print("History cleared.")
                continue

            if command == "undo":
                calculator.undo()
                print("Undo complete.")
                continue

            if command == "redo":
                calculator.redo()
                print("Redo complete.")
                continue

            if command == "save":
                calculator.save_history()
                print("History saved.")
                continue

            if command == "load":
                calculator.load_history()
                print("History loaded.")
                continue

            first = validate_number(input("Enter first number: "))
            second = validate_number(input("Enter second number: "))

            result = calculator.calculate(
                command,
                first,
                second,
            )

            print(f"Result: {result}")

        except (ValueError, ZeroDivisionError) as exc:
            print(f"Error: {exc}")

        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    run_repl()  # pragma: no cover