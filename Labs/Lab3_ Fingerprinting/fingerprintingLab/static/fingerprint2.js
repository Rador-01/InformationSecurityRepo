const sentence = document.getElementById("target-sentence").textContent;
const input = document.getElementById("typing-input");
const results = document.getElementById("typing-results");

let startTime = null;
let corrections = 0;

input.addEventListener("keydown", function (event) {
  if (startTime === null && event.key.length === 1) startTime = performance.now();
  if (event.key === "Backspace") corrections++;
});


input.addEventListener("input", function () {
  if (input.value !== sentence) return;

  const time = (performance.now() - startTime) / 1000;
  const speed = sentence.length / time;
  input.disabled = true;

  results.textContent =
    "Time: " + time.toFixed(2) + " s\n" +
    "Speed: " + speed.toFixed(2) + " chars/s\n" +
    "Corrections: " + corrections;

  fetch("/collect", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ time: time.toFixed(2), speed: speed.toFixed(2), corrections: corrections })
  });
});


document.getElementById("restart-button").addEventListener("click", function () {
  startTime = null;
  corrections = 0;
  input.value = "";
  input.disabled = false;
  results.textContent = "";
  input.focus();
});