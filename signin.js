document.getElementById("signinForm").addEventListener("submit", function(e) {
    // You can add custom validation or visual feedback here
    const username = document.querySelector("input[name='username']").value.trim();
    const password = document.querySelector("input[name='password']").value.trim();
  
    if (!username || !password) {
      e.preventDefault();
      alert("Please fill in all fields.");
    }
  });
  