**Purpose**
As an aspiring software engineer, I’m constantly looking for opportunities to enhance my skills and create useful software solutions. For this project, I developed a task management application that integrates with Firebase Cloud Firestore, enabling users to add, view, update, and delete tasks stored in the cloud. This project aims to provide me with hands-on experience in working with cloud databases and building mobile apps.

The program allows users to interact with a task list: adding new tasks, marking them as completed, and removing them once they’re done. It also demonstrates how to connect a local application with Firebase to manage data in a cloud database, offering a seamless experience for users. By using Firebase, the app also showcases the benefits of cloud storage, such as real-time updates and reliable data syncing across multiple devices.

**Cloud Database**

For this project, I used Firebase Cloud Firestore as the cloud database. Firebase Firestore is a flexible, scalable NoSQL cloud database that supports real-time data synchronization. It allows me to store the application’s tasks and update them across users’ devices without requiring complex server-side management.

I created a simple database structure with a single collection called "tasks". Each document in the "tasks" collection represents a task and contains fields like:

task: The name of the task.

completed: A boolean that indicates whether the task has been completed or not.

This structure allows easy scaling and integration with the app, and Firestore handles the real-time synchronization of tasks between the database and the app.

**Development Environment**

To develop this application, I used the following tools:

Python 3.x for the backend logic and Firebase integration.

Firebase SDK for Python for connecting and interacting with the Firestore database.

Visual Studio Code (VS Code) as the Integrated Development Environment (IDE) for coding.

Git and GitHub for version control and hosting the project code.

I used Python as the primary programming language for this project because of its simplicity and ability to integrate easily with Firebase through the Firebase Admin SDK. Additionally, Python’s extensive library support helped speed up development.

**Useful Websites**
https://firebase.google.com/docs
https://firebase.google.com/docs/reference/admin/python
https://docs.github.com/en

**Future Work**

While this application is functional, there are several improvements and additions I would like to make in the future:

Add user authentication to allow individual user accounts, so each person has their own list of tasks.

Implement a frontend for mobile devices using a framework like Flutter or React Native to make the app accessible across platforms.

Add functionality for due dates and task categories to make the task management more comprehensive.

Introduce push notifications for task reminders and deadlines.
