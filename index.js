const slider = document.querySelector('.slider');
const stressValue = document.getElementById('stressValue');

slider.addEventListener('input', () => {
  stressValue.textContent = slider.value;
});
