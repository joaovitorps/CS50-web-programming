document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("form");
  form.onsubmit = (e) => {
    e.preventDefault();
    alert(`Hello ${e.target.name.value}`);
  };
});
