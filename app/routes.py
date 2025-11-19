from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

# Temporary in-memory list of tasks
tasks = []

@main.route('/', methods=['GET','POST'])

def index():
    if request.method == 'POST':
        new_task = request.form.get('task')
        if new_task:
            tasks.append({"text": new_task, "done": False})
        return redirect(url_for('main.index'))

    return render_template('index.html', tasks = tasks)

@main.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('main.index'))


@main.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = not tasks[task_id]["done"]
    return redirect(url_for('main.index'))