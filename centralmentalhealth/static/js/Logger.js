const stressSlider = document.getElementById("stressRange");
const stressValue = document.getElementById("stressValue");
const submitBtn = document.getElementById("submitBtn");
const mindfulnessCard = document.getElementById("mindfulnessCard");

stressSlider.addEventListener("input", () => {
  stressValue.textContent = stressSlider.value;
});

submitBtn.addEventListener("click", () => {
  const level = parseInt(stressSlider.value);

  if (level >= 7) {
    mindfulnessCard.style.display = "block";
  } else {
    mindfulnessCard.style.display = "none";
    alert("You're doing okay today. Keep it up! 😊");
  }
});
