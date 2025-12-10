export function filterTasks(tasks, query) {
    return tasks.filter(t => t.toLowerCase().includes(query.toLowerCase()));
}
