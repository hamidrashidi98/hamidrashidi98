## Welcome to My GitHub Profile!
![Hamid Rashidi SVG](./hamidrashidi.svg)
## Hi there !🫡🙌 
## I’m Hamid, a developer from Iran.
Hi, I'm Hamid Rashidi (he/him)! I'm a passionate developer, and here's a fun Tic-Tac-Toe game you can play right on my profile! Try to beat the computer! 🎮

## 🎲 Play Tic-Tac-Toe

Click on an empty cell (⬜) to place your **X**. The computer will respond with **O**. *Wait a few seconds and refresh the page to see the updated board!*

|   |   |   |
|---|---|---|
|[⬜](#move-0)|[⬜](#move-1)|[⬜](#move-2)|
|[⬜](#move-3)|[⬜](#move-4)|[⬜](#move-5)|
|[⬜](#move-6)|[⬜](#move-7)|[⬜](#move-8)|

<script>
document.querySelectorAll('a[href^="#move-"]').forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const move = link.getAttribute('href').split('-')[1];
    fetch(`https://api.github.com/repos/hamidrashidi98/hamidrashidi98/actions/workflows/update_game.yml/dispatches`, {
      method: 'POST',
      headers: {
        'Authorization': `token ${localStorage.getItem('github-token') || 'YOUR_PERSONAL_ACCESS_TOKEN'}`,
        'Accept': 'application/vnd.github.v3+json'
      },
      body: JSON.stringify({ ref: 'main', inputs: { move: move } })
    }).then(() => alert('Move sent! Refresh the page in a few seconds.'));
  });
});
</script>

*Note*: After clicking a cell, wait 10-30 seconds and refresh the page to see the updated board. To reset the game, click [here](#reset).

## 🛠️ Skills
- HTML, CSS, JavaScript
- Python
- SVG Animations

## 📫 Connect with Me
- [LinkedIn](https://www.linkedin.com/in/your-linkedin-profile) *(Replace with your LinkedIn URL)*
- [Email](mailto:your.email@example.com) *(Replace with your email)*

Enjoy the game and explore my projects below! 🚀
