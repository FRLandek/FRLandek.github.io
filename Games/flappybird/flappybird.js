const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

var x = 0
var y = 0
ctx.beginPath();


const intervalId = setInterval(() => {
    ctx.lineTo(x, y);
    ctx.stroke();
    x += 1
    y += 1
}, 10);