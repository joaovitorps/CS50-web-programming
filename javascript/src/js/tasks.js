document.addEventListener("DOMContentLoaded", () => {
  const tasksUl = document.getElementById("tasks-ul");
  const taskInput = document.getElementById("task");
  const form = document.getElementById("form");
  const submitButton = document.getElementById("submit-button");

  taskInput.oninput = (e) => {
    submitButton.disabled = e.target.value === "";
  };

  form.onsubmit = (e) => {
    e.preventDefault();
    const newtask = e.target.task.value;

    const li = document.createElement("li");
    li.innerHTML = newtask;
    tasksUl.appendChild(li);

    e.target.task.value = "";
    submitButton.disabled = true;
  };
});
