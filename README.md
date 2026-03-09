<!DOCTYPE html>
<html>
<head>
<title>AI Fitness Coach</title>

<style>

body{
font-family: Arial;
background:#0f172a;
color:white;
text-align:center;
padding:20px;
}

.container{
max-width:700px;
margin:auto;
background:#1e293b;
padding:25px;
border-radius:10px;
box-shadow:0 0 10px black;
}

input,select,button{
padding:10px;
margin:8px;
border-radius:5px;
border:none;
}

button{
background:#22c55e;
color:white;
cursor:pointer;
}

button:hover{
background:#16a34a;
}

.section{
margin-top:25px;
padding:15px;
border-top:1px solid gray;
}

#chatbox{
height:200px;
overflow-y:auto;
background:black;
padding:10px;
border-radius:5px;
text-align:left;
}

.timer{
font-size:30px;
margin:10px;
}

</style>

</head>

<body>

<h1>🤖 AI Fitness Coach</h1>

<div class="container">

<!-- BMI CALCULATOR -->

<div class="section">

<h2>BMI Calculator</h2>

<input type="number" id="height" placeholder="Height (cm)">
<input type="number" id="weight" placeholder="Weight (kg)">

<br>

<button onclick="calculateBMI()">Calculate</button>

<p id="bmiResult"></p>

</div>

<!-- WORKOUT PLAN -->

<div class="section">

<h2>AI Workout Plan</h2>

<select id="goal">
<option value="weightloss">Weight Loss</option>
<option value="muscle">Muscle Gain</option>
<option value="fitness">General Fitness</option>
</select>

<br>

<button onclick="getWorkout()">Generate Workout</button>

<p id="workoutResult"></p>

</div>

<!-- DIET PLAN -->

<div class="section">

<h2>AI Diet Plan</h2>

<select id="dietGoal">

<option value="loss">Weight Loss</option>
<option value="gain">Muscle Gain</option>

</select>

<br>

<button onclick="generateDiet()">Generate Diet</button>

<p id="dietResult"></p>

</div>

<!-- WORKOUT TIMER -->

<div class="section">

<h2>Workout Timer</h2>

<div class="timer" id="timer">30</div>

<button onclick="startTimer()">Start</button>
<button onclick="resetTimer()">Reset</button>

</div>

<!-- PROGRESS TRACKER -->

<div class="section">

<h2>Progress Tracker</h2>

<input id="workoutDay" placeholder="Workout done today">

<button onclick="saveProgress()">Save</button>

<p id="progress"></p>

</div>

<!-- AI CHAT -->

<div class="section">

<h2>AI Fitness Chat</h2>

<div id="chatbox"></div>

<input id="userInput" placeholder="Ask fitness question">

<button onclick="sendMessage()">Send</button>

</div>

</div>

<script>

function calculateBMI(){

let h=document.getElementById("height").value;
let w=document.getElementById("weight").value;

let bmi=w/((h/100)*(h/100));

let status="";

if(bmi<18.5)
status="Underweight";

else if(bmi<25)
status="Normal";

else if(bmi<30)
status="Overweight";

else
status="Obese";

document.getElementById("bmiResult").innerHTML=
"Your BMI: "+bmi.toFixed(2)+" ("+status+")";

}

function getWorkout(){

let goal=document.getElementById("goal").value;

let workout="";

if(goal=="weightloss")
workout="Running, Jump Rope, HIIT, Cycling, Plank";

if(goal=="muscle")
workout="Pushups, Squats, Deadlift, Bench Press, Pullups";

if(goal=="fitness")
workout="Yoga, Walking, Stretching, Light Cardio";

document.getElementById("workoutResult").innerHTML=workout;

}

function generateDiet(){

let goal=document.getElementById("dietGoal").value;

let diet="";

if(goal=="loss")
diet="Oats, Fruits, Vegetables, Lean Chicken, Green Tea";

if(goal=="gain")
diet="Eggs, Milk, Rice, Chicken, Peanut Butter, Bananas";

document.getElementById("dietResult").innerHTML=diet;

}

let time=30;
let timerInterval;

function startTimer(){

timerInterval=setInterval(function(){

time--;
document.getElementById("timer").innerHTML=time;

if(time<=0){

clearInterval(timerInterval);
alert("Workout Time Completed!");

}

},1000);

}

function resetTimer(){

clearInterval(timerInterval);
time=30;
document.getElementById("timer").innerHTML=time;

}

function saveProgress(){

let workout=document.getElementById("workoutDay").value;

localStorage.setItem("progress",workout);

document.getElementById("progress").innerHTML=
"Saved: "+workout;

}

function sendMessage(){

let input=document.getElementById("userInput").value;

let chatbox=document.getElementById("chatbox");

chatbox.innerHTML+="<p><b>You:</b> "+input+"</p>";

let reply="";

if(input.includes("belly"))
reply="Try cardio, plank, leg raises, and reduce sugar.";

else if(input.includes("muscle"))
reply="Do strength training and eat protein.";

else if(input.includes("diet"))
reply="Eat balanced meals with protein, carbs, and vegetables.";

else
reply="Stay consistent with workouts and drink enough water.";

chatbox.innerHTML+="<p><b>AI Coach:</b> "+reply+"</p>";

document.getElementById("userInput").value="";

chatbox.scrollTop=chatbox.scrollHeight;

}

</script>

</body>
</html>
