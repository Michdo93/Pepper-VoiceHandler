var cards = ['A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'C', 'D', 'E', 'F'];
var moves = 0;
var hasFlippedCard = false;
var lockBoard = false;
var firstCard, secondCard;

var row1 = document.getElementById('row1');
var row2 = document.getElementById('row2');
var row3 = document.getElementById('row3');
var row4 = document.getElementById('row4');
var moveCounter = document.getElementById('move-counter');

function shuffle(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array;
}

function createBoard() {
    row1.innerHTML = '';
    row2.innerHTML = '';
    row3.innerHTML = '';
    row4.innerHTML = '';
    moves = 0;
    moveCounter.textContent = moves;
    lockBoard = false;

    var shuffledCards = shuffle(cards);
    var rows = [row1, row2, row3, row4];
    var rowIndex = 0;

    shuffledCards.forEach(function (card) {
        var memoryCard = document.createElement('div');
        memoryCard.className = 'card hidden';
        memoryCard.dataset.framework = card;

        var front = document.createElement('div');
        front.className = 'front';
        front.textContent = card;

        var back = document.createElement('div');
        back.className = 'back';

        memoryCard.appendChild(front);
        memoryCard.appendChild(back);

        memoryCard.addEventListener('click', flipCard);

        rows[rowIndex].appendChild(memoryCard);
        rowIndex = (rowIndex + 1) % rows.length;
    });
}

function flipCard() {
    if (lockBoard) return;
    if (this === firstCard) return;

    this.classList.add('flipped');
    this.classList.remove('hidden');

    if (!hasFlippedCard) {
        hasFlippedCard = true;
        firstCard = this;
        return;
    }

    secondCard = this;
    checkForMatch();
}

function checkForMatch() {
    var isMatch = firstCard.dataset.framework === secondCard.dataset.framework;
    updateMoves();
    isMatch ? disableCards() : unflipCards();
}

function disableCards() {
    firstCard.removeEventListener('click', flipCard);
    secondCard.removeEventListener('click', flipCard);
    resetBoard();
}

function unflipCards() {
    lockBoard = true;

    setTimeout(function () {
        firstCard.classList.add('hidden');
        secondCard.classList.add('hidden');
        firstCard.classList.remove('flipped');
        secondCard.classList.remove('flipped');
        resetBoard();
    }, 1000);
}

function resetBoard() {
    hasFlippedCard = false;
    lockBoard = false;
    firstCard = null;
    secondCard = null;
}

function updateMoves() {
    moves++;
    moveCounter.textContent = moves;
}

function restartGame() {
    createBoard();
}

createBoard();
