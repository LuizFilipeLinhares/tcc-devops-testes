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
    // 🔥 salva no navegador
    localStorage.setItem("logged", "true");

    window.location.href = "index.html";
  } else {
    errorMessage.innerText = "Email ou senha inválidos";
  }
}

// 🚪 logout
function logout() {
  localStorage.removeItem("logged");
  window.location.href = "login.html";
}