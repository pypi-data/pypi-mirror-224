from typing import Union, Callable, Optional, List
import asyncio
import types


class RegisteredOperation:
    # Static counter to keep track of order
    _counter = 0

    def __init__(self, func: Union[Callable, types.CoroutineType], description: str, priority: Optional[int] = None, asyncness: bool = False):
        if not hasattr(func, "__call__"):
            raise ValueError(f"{func} is not a function or async function.")

        if not isinstance(description, str):
            raise ValueError(
                "Description must be provided and should be a string.")

        self.func = func
        self.description = description
        self.priority = 0 if priority is None else priority
        self.asyncness = asyncness

        # Increment the static counter and assign order
        RegisteredOperation._counter += 1
        self.order = RegisteredOperation._counter


# List to hold registered operations
registered_operations = []


def register_operation(func: Union[Callable, types.CoroutineType], description: str, priority: Optional[int] = None):
    asyncness = asyncio.iscoroutinefunction(func)
    operation = RegisteredOperation(func, description, priority, asyncness)
    registered_operations.append(operation)


def reset_operations():
    registered_operations.clear()


def list_operations() -> List[RegisteredOperation]:
    # Sort based on priority first (higher values first), and then by order (ascending)
    sorted_operations = sorted(
        registered_operations,
        key=lambda op: (op.priority == 0, -op.priority, op.order)
    )
    return sorted_operations


async def start_listening_async():
    operation_dict = {index + 1: operation for index,
                      operation in enumerate(list_operations())}

    _print_operations(operation_dict)
    while True:
        try:
            # check for "help" inpit
            choice_str = input().lower()
            if choice_str == "help":
                _print_operations(operation_dict)
                continue

            # check for "exit" input
            choice = int(choice_str)
            if choice == 0:
                print("Exiting...")
                break

            # Check if the choice is valid
            selected_operation = operation_dict.get(choice)
            if not selected_operation:
                print(
                    f"Invalid choice {choice}. Please select a valid operation.")
                continue
            print()  # Empty line before operation outputs

            # If the function is asynchronous, run it using the event loop
            print(f"Running operation: {selected_operation.description}")
            if selected_operation.asyncness:
                result = await selected_operation.func()
            else:
                result = selected_operation.func()

            if result is not None:
                print(result)
            print("\nDone\n")  # Empty line after operation outputs
            _request_selection()

        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")


def start_listening():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_listening_async())
    loop.close()


def _print_operations(operation_dict):
    print("\nAvailable operations:")
    print("0. Exit")
    for index, operation in operation_dict.items():
        print(f"{index}. {operation.description}")
    _request_selection()


def _request_selection():
    print('\nSelect an operation (\'help\' for list of operations)')
