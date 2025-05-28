## Welcome to My GitHub Profile!
![Hamid Rashidi SVG](./hamidrashidi.svg)
## Hi there !🫡🙌 
## I’m Hamid, a developer from Iran.
## 🎮 Play Snake

Use the arrow keys (↑, ↓, ←, →) to control the snake. Eat the food (🍎) to grow and increase your score. Avoid hitting the walls or the snake's own body!

<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 30 30" style="background-color: #1a1a1a;">
  <defs>
    <style>
      .snake { fill: #40E0D0; }
      .food { fill: #FF0000; }
      .grid { stroke: #333; stroke-width: 0.1; }
      .score { fill: #FFFFFF; font-size: 1; font-family: Arial; }
    </style>
  </defs>
  <rect width="30" height="30" fill="#1a1a1a" />
  <g id="grid">
    <path d="M0,0 H30 M0,1 H30 M0,2 H30 M0,3 H30 M0,4 H30 M0,5 H30 M0,6 H30 M0,7 H30 M0,8 H30 M0,9 H30 M0,10 H30 M0,11 H30 M0,12 H30 M0,13 H30 M0,14 H30 M0,15 H30 M0,16 H30 M0,17 H30 M0,18 H30 M0,19 H30 M0,20 H30 M0,21 H30 M0,22 H30 M0,23 H30 M0,24 H30 M0,25 H30 M0,26 H30 M0,27 H30 M0,28 H30 M0,29 H30" class="grid" />
    <path d="M0,0 V30 M1,0 V30 M2,0 V30 M3,0 V30 M4,0 V30 M5,0 V30 M6,0 V30 M7,0 V30 M8,0 V30 M9,0 V30 M10,0 V30 M11,0 V30 M12,0 V30 M13,0 V30 M14,0 V30 M15,0 V30 M16,0 V30 M17,0 V30 M18,0 V30 M19,0 V30 M20,0 V30 M21,0 V30 M22,0 V30 M23,0 V30 M24,0 V30 M25,0 V30 M26,0 V30 M27,0 V30 M28,0 V30 M29,0 V30" class="grid" />
  </g>
  <g id="snake"></g>
  <text id="food" x="15" y="15.5" class="food" font-size="1.5">🍎</text>
  <text id="score" x="1" y="1" class="score">Score: 0</text>
  <script>
    <![CDATA[
    const svg = document.querySelector('svg');
    const snakeGroup = document.getElementById('snake');
    const food = document.getElementById('food');
    const scoreText = document.getElementById('score');
    let snake = [{x: 10, y: 10}];
    let direction = {x: 1, y: 0};
    let foodPos = {x: 15, y: 15};
    let score = 0;
    let gameInterval;

    function drawSnake() {
      snakeGroup.innerHTML = '';
      snake.forEach(segment => {
        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('x', segment.x);
        rect.setAttribute('y', segment.y);
        rect.setAttribute('width', 1);
        rect.setAttribute('height', 1);
        rect.setAttribute('class', 'snake');
        snakeGroup.appendChild(rect);
      });
    }

    function moveSnake() {
      const head = {x: snake[0].x + direction.x, y: snake[0].y + direction.y};
      if (head.x < 0 || head.x >= 30 || head.y < 0 || head.y >= 30 || snake.some(seg => seg.x === head.x && seg.y === head.y)) {
        clearInterval(gameInterval);
        alert('Game Over! Your score: ' + score);
        snake = [{x: 10, y: 10}];
        direction = {x: 1, y: 0};
        score = 0;
        scoreText.textContent = 'Score: 0';
        foodPos = {x: 15, y: 15};
        food.setAttribute('x', foodPos.x);
        food.setAttribute('y', foodPos.y + 0.5);
        drawSnake();
        gameInterval = setInterval(moveSnake, 200);
        return;
      }
      snake.unshift(head);
      if (head.x === foodPos.x && head.y === foodPos.y) {
        score++;
        scoreText.textContent = 'Score: ' + score;
        foodPos = {x: Math.floor(Math.random() * 30), y: Math.floor(Math.random() * 30)};
        food.setAttribute('x', foodPos.x);
        food.setAttribute('y', foodPos.y + 0.5);
      } else {
        snake.pop();
      }
      drawSnake();
    }

    function changeDirection(event) {
      const key = event.key;
      if (key === 'ArrowUp' && direction.y === 0) {
        direction = {x: 0, y: -1};
      } else if (key === 'ArrowDown' && direction.y === 0) {
        direction = {x: 0, y: 1};
      } else if (key === 'ArrowLeft' && direction.x === 0) {
        direction = {x: -1, y: 0};
      } else if (key === 'ArrowRight' && direction.x === 0) {
        direction = {x: 1, y: 0};
      }
    }

    document.addEventListener('keydown', changeDirection);
    gameInterval = setInterval(moveSnake, 200);
    drawSnake();
    ]]>
  </script>
</svg>

## 🛠️ Skills
- HTML, CSS, JavaScript
- Python
- SVG Animations

## 📫 Connect with Me
- [LinkedIn](https://www.linkedin.com/in/your-linkedin-profile) *(Replace with your LinkedIn URL)*
- [Email](mailto:your.email@example.com) *(Replace with your email)*

Enjoy the game and explore my projects below! 🚀
