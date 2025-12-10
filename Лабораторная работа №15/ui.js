export function renderList(listElem, tasks, removeFn) {
    listElem.innerHTML = "";

    tasks.forEach((task, i) => {
        const li = document.createElement("li");
        li.innerHTML = `${task} <button data-id="${i}" class="removeBtn">Удалить</button>`;
        listElem.appendChild(li);
    });

    document.querySelectorAll(".removeBtn").forEach(btn => {
        btn.addEventListener("click", () => {
            removeFn(parseInt(btn.dataset.id));
        });
    });
}
