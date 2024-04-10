document.addEventListener("DOMContentLoaded", () => {
  const worldH2 = document.getElementById("world-h2");

  document.querySelector("select").onchange = (e) => {
    worldH2.style.color = e.target.value;
  };

  const helloH1 = document.getElementById("hello-h1");

  const buttons = document.querySelectorAll("button");

  const clearOtherButtonsColor = (color) => {
    buttons.forEach((button) => {
      if (color !== button.dataset.color) {
        button.style.backgroundColor = "";
      }
    });
  };

  const changeColor = (button) => {
    const buttonColor = button.dataset.color;

    const defaultButtonColor = "";
    const defaultTextColor = "black";

    const btnStyle = button.style;
    const txtStyle = helloH1.style;

    if (btnStyle.backgroundColor === defaultButtonColor) {
      btnStyle.backgroundColor = buttonColor;
      txtStyle.color = buttonColor;
      clearOtherButtonsColor(buttonColor);
    } else {
      btnStyle.backgroundColor = defaultButtonColor;
      txtStyle.color = defaultTextColor;
    }
  };

  buttons.forEach((button) => {
    button.onclick = () => {
      changeColor(button);
    };
  });
});
