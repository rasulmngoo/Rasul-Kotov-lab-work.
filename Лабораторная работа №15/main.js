import { saveTasks, loadTasks } from "./storage.js";
import { renderList } from "./ui.js";
import { filterTasks } from "./utils.js";

let tasks = loadTasks();

const input = document.getElementById("taskInput");
const listElem = document.getElementById("taskList");
const searchInput = document.getElementById("searchInput");

function refresh() {
    const query = searchInput.value.trim();
    const filtered = filterTasks(tasks, query);
    renderList(listElem, filtered, removeTask);
}

function removeTask(index) {
    tasks.splice(index, 1);
    saveTasks(tasks);
    refresh();
}

document.getElementById("addBtn").addEventListener("click", () => {
    const text = input.value.trim();
    if (text) {
        tasks.push(text);
        saveTasks(tasks);
        input.value = "";
        refresh();
    }
});

searchInput.addEventListener("input", refresh);

// первый рендер
refresh();
