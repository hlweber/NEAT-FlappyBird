<h1 align="center">
   <a href="#"> NEAT - Flappy Bird </a>
</h1>

<h3 align="center">
    💻🐤 Your computer playing Flappy Bird! 🐤💻
</h3>

<h4 align="center"> 
	 Status: Finished
</h4>

<p align="center">
 <a href="#about">About</a> •
 <a href="#how-it-works">How it works</a> • 
 <a href="#results">Results</a> • 
 <a href="#author">Author</a> • 

</p>


## About

🐤	Flappy Bird - NEAT

This project consists on building an flappy bird like game and training a NEAT model for the computer learn how to play the game.

The whole project was written in python (pygame and neat).

There are two main python files, main_flappy.py - where you can control the bird | main_neat.py - where you can see the evolution of the model generations

---

## How it works

This project is divided into two parts:
1. Game Building
2. Model Training

### 1. Game Building

**The rules**:

On this game the player controls the flight of bird, the objective is to travel as far as possible without hitting the pipes that will surge along the way.

The further the bird travels, the harder it gets - the pipes will come faster and the gap between the pipes will get narrow.
 
--

**Mechanics**:

The game is built in a way where the bird can't move on the x-axis, the pipes and ground will move on the x-axis, but not the bird.

The bird is only allowed to move in y-axis, if the player press the button to 'jump' the bird goes up else it goes down

Once the bird hits a pipe, he dies and the game ends.

--

**Objects**:

There are three objects on the game:
1. Bird 
2. Pipes
3. Floor

--

### 2. Model Training

NEAT is a model that mutates and evolves given a fitness value - in this case, the greatest the fitness, the better.

In this model, the birds that travel the furthest have a bigger fitness value.

---

## Results

As Flappy Bird is a fairly simple game (you just have to decide either the bird should jump or not), training the model with a population of 100 birds will generate some random species that perform pretty well, which is not the best to see how the evolution of the model works.

That being said, the model population is set to be 10 birds, so it's easier to perceive the evolution of the generations.


COLOCAR GIF

---

## Author

#### Henrique L. Weber

[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/henrique-weber/)](https://www.linkedin.com/in/henrique-weber/) 
[![Gmail Badge](https://img.shields.io/badge/-Email-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:hlweber@uol.com.br)](mailto:hlweber@uol.com.br)
