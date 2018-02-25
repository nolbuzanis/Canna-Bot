var colors = [];
var pickedColor;
var squares = document.querySelectorAll(".square");
var colorDisplay = document.getElementById("colorDisplay");
var messageDispaly = document.querySelector("#message");
var header = document.querySelector(".header");
var btnNewColors = document.querySelector("#btnNewColors");
var btnEasy = document.querySelector("#btnEasy");
var btnHard = document.querySelector("#btnHard");

var difficulty = "hard"
btnHard.classList.add('buttonSelected');
restart();

btnEasy.addEventListener("click", function() {
	if (difficulty === "hard"){
		this.classList.toggle('buttonSelected');
		btnHard.classList.toggle('buttonSelected');
		difficulty = "easy";
		restart();
	}
});

btnHard.addEventListener("click", function() {
	if (difficulty === "easy"){
		this.classList.toggle('buttonSelected');
		btnEasy.classList.toggle('buttonSelected');
		difficulty = "hard";
		restart();
	}
});


btnNewColors.addEventListener("click", function(){
	restart();
});

btnNewColors.addEventListener("mouseenter", function() {
	this.classList.add('buttonHover');
});

btnNewColors.addEventListener("mouseleave", function() {
	this.classList.remove('buttonHover');
});

function restart(){
	if(difficulty === "hard"){
		colors = generateRandomColors(6);

		for(var i = 0; i < squares.length; i++){
			squares[i].style.display = "block";
			squares[i].style.backgroundColor = colors[i];
			squareClickEvent(i);
		}	 
	}

	else {
		colors = generateRandomColors(3);

		for(var i = 0; i < squares.length; i++){
			squares[i].style.backgroundColor = colors[i];

			if (colors[i]){
				squareClickEvent(i);
			}

			else{
				squares[i].style.display = "none";
			}
		}	 
	}

	pickedColor = colors[pickColor()];
	colorDisplay.textContent = pickedColor;
	header.style.backgroundColor = "#4278ab";
	messageDispaly.textContent = "";
	btnNewColors.innerHTML = "<strong>NEW COLORS</strong>";
}

function squareClickEvent(i) {
	squares[i].addEventListener("click", function () {
		var clickedColor = this.style.backgroundColor;

		if(clickedColor === pickedColor){
			messageDispaly.textContent = "Correct!";
			changeColors(clickedColor);
			header.style.backgroundColor = pickedColor;
			btnNewColors.innerHTML = "<strong>Play Again?</strong>"
		} 

		else {
			this.style.backgroundColor = "#232323";
			messageDispaly.textContent = "Try Again";
		}
	});
}

function changeColors(color){
	for(var i = 0; i < colors.length; i++){
		squares[i].style.backgroundColor = color;
	}
}

function pickColor() {
	var randomNum = Math.floor(Math.random() * colors.length);
	return randomNum;
}

function generateRandomColors(num){
	var colors = [];

	for(var i = 0; i < num; i++){
		colors[i] = "rgb(" + randomColor() + ", " + randomColor() + ", " + randomColor() + ")";
	}

	return colors;
}

function randomColor(){
	var random = Math.floor(Math.random() * 256);
	return random
}