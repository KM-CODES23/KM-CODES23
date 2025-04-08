 const form = document.getElementById('checkinForm');
    const recommendation = document.getElementById('recommendation');
    const confirmationMessage = document.getElementById('confirmationMessage');
    const modifyForm = document.getElementById('modifyForm');
    const planDetails = document.getElementById('planDetails');

    form.addEventListener('submit', function(e) {
      e.preventDefault();
      recommendation.style.display = 'block';
      confirmationMessage.style.display = 'none';
      modifyForm.style.display = 'none';
    });

    function confirmPlan() {
      recommendation.style.display = 'none';
      confirmationMessage.style.display = 'block';
    }

    function modifyPlan() {
      recommendation.style.display = 'none';
      modifyForm.style.display = 'block';
    }

    document.getElementById('customPlanForm').addEventListener('submit', function(e) {
      e.preventDefault();
      const study = document.getElementById('customStudy').value;
      const activity = document.getElementById('customActivity').value;

      planDetails.innerHTML = `
        <li>${study}</li>
        <li>${activity}</li>
      `;
      modifyForm.style.display = 'none';
      recommendation.style.display = 'block';
    });