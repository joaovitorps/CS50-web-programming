document.addEventListener("DOMContentLoaded", () => {
  const myCountButton = document.getElementById("count-button");
  myCountButton.addEventListener("click", count);

  const myResetButton = document.getElementById("reset-button");
  myResetButton.addEventListener("click", reset);

  const counterH1 = document.getElementById("counter");
  counterH1.innerHTML = localStorage.getItem("counter");

  setInterval(startCount, 1000, 15);
});

function startCount(max) {
  const nextNumber = count();
  if (nextNumber > max) {
    reset();
  }
}

// function count() {
//   const currentNumber = document.getElementById("counter");
//   const nextNumber = parseInt(currentNumber.innerHTML) + 1;

//   currentNumber.innerHTML = nextNumber;
//   document.getElementById("reset-button").disabled = false;

//   return nextNumber;
// }

function count() {
  if (!localStorage.getItem("counter")) {
    localStorage.setItem("counter", 0);

    return;
  }

  const counterH1 = document.getElementById("counter");

  let counter = localStorage.getItem("counter");
  counter++;

  localStorage.setItem("counter", counter);
  counterH1.innerHTML = counter;

  document.getElementById("reset-button").disabled = false;

  return localStorage.getItem("counter");
}

function reset() {
  localStorage.setItem("counter", 0);
  document.getElementById("counter").innerHTML =
    localStorage.getItem("counter");
  document.getElementById("reset-button").disabled = true;
}
