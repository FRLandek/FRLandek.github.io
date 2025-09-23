const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');


ctx.beginPath();

function getRandomInt(min, max) {
    min = Math.ceil(min); // Ensures min is an integer
    max = Math.floor(max); // Ensures max is an integer
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
  
  // Example: Generate a random integer between 1 and 10 (inclusive)
var y = getRandomInt(100, -400);
var x = 700
const pipeGap = 600

const intervalId = setInterval(() => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "green"
    // Draw a filled rectangle at (50, 50) with a width of 100 and height of 75
    ctx.fillRect(x, y, 75, 400);
    ctx.fillRect(x, y + pipeGap, 75, 400);
    x -= 1
}, 10);