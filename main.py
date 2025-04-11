import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("C:/Users/tmorris/Documents/Trevaye Morris/BYU-I/ToDoList/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()
tasks_ref = db.collection("tasks")

# Create a new task
def add_task(task_name):
    tasks_ref.add({
        'task': task_name,
        'completed': False
    })

# View all tasks
def view_tasks():
    tasks = tasks_ref.stream()
    for task in tasks:
        print(f"{task.id} => {task.to_dict()}")

# Sample usage
add_task("Finish cloud project")
view_tasks()
