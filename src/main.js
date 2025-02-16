import './style.css';

// Custom algorithm to generate a valid 6-digit code
function generateValidCode() {
  let code = Math.floor(Math.random() * 10000).toString().padStart(4, '0');
  let digits = code.split('').map(Number);
  let check = digits[0] * digits[1] + digits[2] * digits[3];
  code = code + (check%100).toString().padStart(2,'0');
  return code;
}

// Checks if a code is valid
function validateCode(code) {
  if (code > 999999 || code < 0) {
    return false;
  }
  let digits = code.split('').map(Number);
  if ((digits[0] * digits[1] + digits[2] * digits[3]) % 100 == (digits[4] * 10 + digits[5])){
    return true;
  }
  return false;
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
