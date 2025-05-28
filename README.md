## Welcome to My GitHub Profile!
![Hamid Rashidi SVG](./hamidrashidi.svg)
## Hi there !🫡🙌 
## I’m Hamid, a developer from Iran.
## 🎮 Auto-Moving Snake Game

Watch the snake 🐍 chase and eat the fish 🐟! The snake moves automatically to find the fish. When it eats the fish, the score increases, and a new fish appears. The game stops if the snake hits the walls or itself.

<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 30 30" style="background-color: #1a1a1a;">
  <defs>
    <style>
      .snake { fill: #40E0D0; }
      .fish { fill: #FF0000; }
      .grid { stroke: #333; stroke-width: 0.1; }
    </style>
  </defs>
  <rect width="30" height="30" fill="#1a1a1a" />
  <g id="grid">
    <path d="M0,0 H30 M0,1 H30 M0,2 H30 M0,3 H30 M0,4 H30 M0,5 H30 M0,6 H30 M0,7 H30 M0,8 H30 M0,9 H30 M0,10 H30 M0,11 H30 M0,12 H30 M0,13 H30 M0,14 H30 M0,15 H30 M0,16 H30 M0,17 H30 M0,18 H30 M0,19 H30 M0,20 H30 M0,21 H30 M0,22 H30 M0,23 H30 M0,24 H30 M0,25 H30 M0,26 H30 M0,27 H30 M0,28 H30 M0,29 H30" class="grid" />
    <path d="M0,0 V30 M1,0 V30 M2,0 V30 M3,0 V30 M4,0 V30 M5,0 V30 M6,0 V30 M7,0 V30 M8,0 V30 M9,0 V30 M10,0 V30 M11,0 V30 M12,0 V30 M13,0 V30 M14,0 V30 M15,0 V30 M16,0 V30 M17,0 V30 M18,0 V30 M19,0 V30 M20,0 V30 M21,0 V30 M22,0 V30 M23,0 V30 M24,0 V30 M25,0 V30 M26,0 V30 M27,0 V30 M28,0 V30 M29,0 V30" class="grid" />
  </g>
  <g id="snake"></g>
  <text id="fish" x="15" y="15" class="fish" font-size="1.5">🐟</text>
  <text id="score" x="1" y="1" fill="#FFFFFF" font-size="1">Score: 0</text>
  <script>
    <![CDATA[
    const svg = document.querySelector('svg');
    const snakeGroup = document.getElementById('snake');
    const fish = document.getElementById('fish');
    const scoreText = document.getElementById('score');
    let snake = [{x: 10, y: 10}];
    let fishPos = {x: 15, y: 15};
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

    function getNextMove() {
      const head = snake[0];
      const dx = fishPos.x - head.x;
      const dy = fishPos.y - head.y;
      let direction = {x: 0, y: 0};

      // Prioritize moving in the direction with the largest distance
      if (Math.abs(dx) > Math.abs(dy)) {
        direction.x = dx > 0 ? 1 : -1; // Move right if fish is to the right, left if to the left
      } else {
        direction.y = dy > 0 ? 1 : -1; // Move down if fish is below, up if above
      }

      // Check if the move is valid (not hitting the snake body)
      const nextHead = {x: head.x + direction.x, y: head.y + direction.y};
      if (snake.some(seg => seg.x === nextHead.x && seg.y === nextHead.y)) {
        // If the preferred move hits the snake, try the other axis
        direction = {x: 0, y: 0};
        if (Math.abs(dx) <= Math.abs(dy)) {
          direction.x = dx > 0 ? 1 : -1;
        } else {
          direction.y = dy > 0 ? 1 : -1;
        }
      }

      return direction;
    }

    function moveSnake() {
      const direction = getNextMove();
      const head = {x: snake[0].x + direction.x, y: snake[0].y + direction.y};

      // Check for collision with walls or self
      if (head.x < 0 || head.x >= 30 || head.y < 0 || head.y >= 30 || snake.some(seg => seg.x === head.x && seg.y === head.y)) {
        clearInterval(gameInterval);
        alert('Game Over! Your score: ' + score);
        return;
      }

      snake.unshift(head);
      if (head.x === fishPos.x && head.y === fishPos.y) {
        score++;
        scoreText.textContent = 'Score: ' + score;
        fishPos = {x: Math.floor(Math.random() * 30), y: Math.floor(Math.random() * 30)};
        // Ensure fish doesn't spawn on snake
        while (snake.some(seg => seg.x === fishPos.x && seg.y === fishPos.y)) {
          fishPos = {x: Math.floor(Math.random() * 30), y: Math.floor(Math.random() * 30)};
        }
        fish.setAttribute('x', fishPos.x);
        fish.setAttribute('y', fishPos.y + 0.5);
      } else {
        snake.pop();
      }
      drawSnake();
    }

    gameInterval = setInterval(moveSnake, 200);
    drawSnake();
    ]]>
  </script>
</svg>

## درباره بازی
- **زمین بازی**: یه مربع 30x30 که با SVG ساخته شده.
- **مار**: با رنگ فیروزه‌ای (#40E0D0) نمایش داده می‌شه و خودش به سمت ماهی حرکت می‌کنه.
- **ماهی**: یه ماهی قرمز (🐟) که وقتی مار می‌خوردش، جای جدید ظاهر می‌شه.
- **امتیاز**: بالای زمین بازی نشون داده می‌شه.

## 🛠️ مهارت‌ها
- HTML، CSS، جاوااسکریپت
- پایتون
- انیمیشن‌های SVG

## 📫 با من در ارتباط باش
- [لینکدین](https://www.linkedin.com/in/your-linkedin-profile) *(لینک لینکدینت رو بذار)*
- [ایمیل](mailto:your.email@example.com) *(ایمیلت رو بذار)*

از تماشای بازی لذت ببر و پروژه‌هام رو پایین‌تر ببین! 🚀
