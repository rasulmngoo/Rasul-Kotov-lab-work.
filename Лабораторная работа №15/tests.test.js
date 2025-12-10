import { filterTasks } from "./utils.js";

test("Фильтрация задач", () => {
    const tasks = ["apple", "banana", "carrot"];
    expect(filterTasks(tasks, "a")).toEqual(["apple", "banana", "carrot"]);
    expect(filterTasks(tasks, "ap")).toEqual(["apple"]);
    expect(filterTasks(tasks, "x")).toEqual([]);
});
