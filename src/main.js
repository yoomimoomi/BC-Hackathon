import './style.css';

// Custom algorithm to generate a valid 6-digit code
function generateValidCode() {
  while (true) {
    let code = Math.floor(Math.random() * 1000000).toString().padStart(6, '0');
    let digits = code.split('').map(Number);
    
    let sum = digits.reduce((a, b) => a + b, 0);
    let product1 = digits[0] * digits[1] * digits[2];
    let product2 = digits[3] * digits[4] * digits[5];

    if (sum % 7 === 0 && product1 === product2) {
      return code;
    }
  }
}

function displayCode() {
  const code = generateValidCode();
  document.getElementById('code').innerText += `${code}`;
}

function startJourney() {
  const name = document.getElementById('name').value;
  if (name) {
    alert(`Welcome, ${name}! Your journey begins now.`);
    // You can add navigation to the next page here
  } else {
    alert('Please enter your name.');
  }
}

document.addEventListener('DOMContentLoaded', (event) => {
  displayCode();
});
