const timerDisplay = document.querySelector('#timer');
const timerDiv = document.querySelector("#timerDiv");

const card = document.querySelector(".card");
const displayBtn = document.querySelector("#displayBtn");
displayBtn.addEventListener("click", displayCard);

const finishedBtn = document.querySelector("#finished");
finishedBtn.addEventListener("click", displayTimer);

const anotherBtn = document.querySelector("#another");
anotherBtn.addEventListener("click", newQuery);

const cardExplanation = document.querySelector(".card-text");
const cardTitle = document.querySelector(".card-title");
const cardCategory = document.querySelector(".card-subtitle");

const minInput = document.querySelector("#minInput");
const secInput = document.querySelector("#secInput");

const startBtn = document.querySelector("#start");
startBtn.addEventListener("click", timer);


window.addEventListener("DOMContentLoaded", newQuery);

function newQuery() {
    let query = "SELECT * FROM Prompts ORDER BY RANDOM() LIMIT 1;";
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/query", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            let response = JSON.parse(this.responseText);
            // Do something with the response data (e.g. display it on the page)
            setCardInformation(response[0][0], response[0][1], response[0][2]);
            console.log(response[0]);
        }
    };
    xhr.send(JSON.stringify({ query: query }));
}


function timer() {
    var min = minInput.value;
    var sec = secInput.value;

    console.log("min here" + min);

    var timer = setInterval(function () {
        var result = "";
        if (min < 10) {
            result += "0" + min;
        } else {
            result += min;
        }
        if (sec < 10) {
            result += ":0" + sec;
        } else {
            result += ":" + sec;
        }
        timerDisplay.innerHTML = result;

        sec--;
        if (sec < 0) {
            if (min > 0) {
                min--;
                sec = 59;
            } else {
                clearInterval(timer);
                displayBtn.style.display = "block";
            }
        }
    }, 1000);
}

function setCardInformation(title, category, explanation) {
    cardTitle.innerHTML = title;
    cardCategory.innerHTML = category;
    cardExplanation.innerHTML = explanation;

}

function displayCard() {
    displayBtn.style.display = "none";
    timerDiv.style.display = "none";
    card.style.display = "block";

}

function displayTimer() {
    timerDiv.style.display = "block";
    card.style.display = "none";
}

// async function fetchAsync(url) {
//     let response = await fetch(url);
//     let data = await response.json();
//     return data;
// }