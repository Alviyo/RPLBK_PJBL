from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# Data dummy untuk task
tasks = [
    {"id": 1, "name": "Task 1", "status": "Pending"},
    {"id": 2, "name": "Task 2", "status": "Completed"}
]

@app.route('/tasks', methods=['GET'])
def tasks_page():
    return render_template('tasks.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    if task_name:  # Pastikan task_name tidak kosong
        new_task = {
            "id": len(tasks) + 1,
            "name": task_name,
            "status": "Pending"
        }
        tasks.append(new_task)
    return redirect('/tasks')

@app.route('/complete_task/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Completed'
            break
    return redirect('/tasks')

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect('/tasks')

if __name__ == '__main__':
    app.run(debug=True)
