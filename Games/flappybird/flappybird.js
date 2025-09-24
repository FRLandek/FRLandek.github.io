const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');


ctx.beginPath();

function getRandomInt(min, max) {
    min = Math.ceil(min); // Ensures min is an integer
    max = Math.floor(max); // Ensures max is an integer
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
  
  // Example: Generate a random integer between 1 and 10 (inclusive)
var y1 = getRandomInt(-500, 0);
var y2 = getRandomInt(-500, 0);
var y3 = getRandomInt(-500, 0);
var x1 = 700
var x2 = 1000
var x3 = 1300
const pipeGap = 700

const intervalId = setInterval(() => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "green"

    //pipes 1
    ctx.fillRect(x1, y1, 75, 500);
    ctx.fillRect(x1, y1 + pipeGap, 75, 500);
    x1 -= 1

    //pipes 2
    ctx.fillRect(x2, y2, 75, 500);
    ctx.fillRect(x2, y2 + pipeGap, 75, 500);
    x2 -= 1

    //pipes 3
    ctx.fillRect(x3, y3, 75, 500);
    ctx.fillRect(x3, y3 + pipeGap, 75, 500);
    x3 -= 1
}, 10);