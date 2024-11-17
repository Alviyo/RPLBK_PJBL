document.addEventListener('DOMContentLoaded', () => {
    fetchTasks();

    document.getElementById('task-form').addEventListener('submit', (e) => {
        e.preventDefault();
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        addTask({ title, description });
    });
});

function fetchTasks() {
    fetch('/tasks')
        .then(response => response.json())
        .then(data => {
            const taskList = document.getElementById('task-list');
            taskList.innerHTML = '';
            data.forEach(task => {
                const taskItem = document.createElement('li');
                taskItem.textContent = `${task.title}: ${task.description}`;
                taskList.appendChild(taskItem);
            });
        });
}

function addTask(task) {
    fetch('/tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(task),
    })
    .then(response => response.json())
    .then(() => {
        fetchTasks();
        document.getElementById('task-form').reset();
    });
}