<h1 align="center">
   <a href="#"> NEAT - Flappy Bird </a>
</h1>

<h3 align="center">
    🐤💻 Your computer playing Flappy Bird!
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

This project consists on builiding an flappy bird like game and training a NEAT model for the computer learn how to play the game.

The whole project was written in python (pygame and neat).

There are two main python files, main_flappy.py - where you can control the bird | main_neat.py - where you can see the evolution of the model generations

---

## How it works

This project is divided into two parts:
1. Game Building
2. Model Training

### 1. Game Building

**The rules**:

On this game the player control the flight of bird, the objective is to travel as far as possible without hitting the pipes that will surge along the way.

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

NEAT is a model that mutates and envolves given a fitness value - in this case, the greatest the fitness, the better.

In this model, the birds that traveled the furthest had a bigger fitness value.

---

## Results

As Flappy Bird is a fairly simple game (you just have to decide either the birds should jump or not), training the model with a population of 100 birds will generate some random species that perform pretty well.

That being said, I choose the population to be 10 birds, so it will be easier to perceive the evolution of the generations


COLOCAR GIF

---

## Author
<a href="https://blog.rocketseat.com.br/author/thiago/">
 <img style="border-radius: 50%;" src="https://avatars3.githubusercontent.com/u/380327?s=460&u=61b426b901b8fe02e12019b1fdb67bf0072d4f00&v=4" width="100px;" alt="Thiago Marinho"/>
 <br />
 <sub><b>Henrique Weber</b></sub></a>
 <br />

[![Linkedin Badge](https://img.shields.io/badge/-Henrique-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/tgmarinho/)](https://www.linkedin.com/in/tgmarinho/) 
[![Gmail Badge](https://img.shields.io/badge/-Email-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:tgmarinho@gmail.com)](mailto:tgmarinho@gmail.com)
