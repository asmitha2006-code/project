from datetime import datetime
from study_planner import (
    load_data, save_data,
    add_tasks, list_tasks,
    mark_task_completed, show_progress
)

def test_add_and_list_tasks():
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")

    print("\n--- Testing Add Tasks ---")
    data["tasks"][today] = [
        {"task": "Test Task 1", "completed": False, "priority": "High"},
        {"task": "Test Task 2", "completed": False, "priority": "Low"}
    ]
    save_data(data)

    print("\n--- Listing Tasks ---")
    list_tasks(data, today)

def test_mark_completed():
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")

    print("\n--- Testing Mark Completed ---")
    data["tasks"][today][0]["completed"] = True
    save_data(data)

    list_tasks(data, today)

def test_progress():
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")

    print("\n--- Testing Progress ---")
    show_progress(today, data)


if __name__ == "__main__":
    test_add_and_list_tasks()
    test_mark_completed()
    test_progress()
