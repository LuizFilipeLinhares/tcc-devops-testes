// ─── Auth ────────────────────────────────────────────────────────────────────

function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const errorMessage = document.getElementById("error-message");

  const validEmail = "admin@test.com";
  const validPassword = "123456";

  if (!email || !password) {
    errorMessage.innerText = "Preencha todos os campos";
    return;
  }

  if (email === validEmail && password === validPassword) {
    localStorage.setItem("logged", "true");
    window.location.href = "index.html";
  } else {
    errorMessage.innerText = "Email ou senha inválidos";
  }
}

function logout() {
  localStorage.removeItem("logged");
  window.location.href = "login.html";
}

// ─── Tasks ───────────────────────────────────────────────────────────────────

function getTasks() {
  return JSON.parse(localStorage.getItem("tasks") || "[]");
}

function saveTasks(tasks) {
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

function addTask() {
  const input = document.getElementById("task-input");
  const errorEl = document.getElementById("task-error");
  const text = input.value.trim();

  if (!text) {
    errorEl.innerText = "Digite o nome da tarefa";
    return;
  }

  errorEl.innerText = "";
  const tasks = getTasks();
  tasks.push({ id: Date.now(), text, done: false });
  saveTasks(tasks);
  input.value = "";
  renderTasks();
}

function toggleTask(id) {
  const tasks = getTasks().map(t =>
    t.id === id ? { ...t, done: !t.done } : t
  );
  saveTasks(tasks);
  renderTasks();
}

function deleteTask(id) {
  const tasks = getTasks().filter(t => t.id !== id);
  saveTasks(tasks);
  renderTasks();
}

function renderTasks() {
  const tasks = getTasks();
  const list = document.getElementById("task-list");
  const empty = document.getElementById("empty-state");

  if (!list) return;

  list.innerHTML = "";

  if (tasks.length === 0) {
    empty.style.display = "block";
    return;
  }

  empty.style.display = "none";

  tasks.forEach(task => {
    const li = document.createElement("li");
    li.className = `task-item${task.done ? " done" : ""}`;
    li.dataset.taskId = task.id;
    li.innerHTML = `
      <input type="checkbox" ${task.done ? "checked" : ""} onchange="toggleTask(${task.id})">
      <span class="task-text">${task.text}</span>
      <button class="btn-delete" onclick="deleteTask(${task.id})" title="Remover">✕</button>
    `;
    list.appendChild(li);
  });
}

if (document.getElementById("task-list")) {
  renderTasks();
}