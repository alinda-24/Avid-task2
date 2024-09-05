# SimpleJavaGame: Let's Code a Mini Game!

For this exercise, you will dive into the world of Java programming by building a simple game application. You'll learn how to model different components using Java classes and bring them to life with exciting functionalities including player movement, scoring systems, and enemy interactions. Your task is to encapsulate various aspects of a game using object-oriented principles in Java and practice designing Java classes comprehensively. Let's get started!

### 📅 Deadline

Please ensure this task is completed prior to the next exercise session on **Friday, 20th October**.

### 💻 Instructions

For detailed information on how to complete and submit your assignment, refer to the [assignments section of the course instructions](URL_TO_COURSE_INSTRUCTIONS).

### 📚 Preparation

Before tackling the assignment, make sure to read and answer questions in Module 3 of the OLI material:

- Read [Exploring Object-Oriented Programming](https://kth.oli.cmu.edu/jcourse/webui/syllabus/module.do?context=f5e5a808ac1f088812f2a8ce315bac60).
- If you haven't done so, register at https://kth.oli.cmu.edu/ using course key `java_game-ht23`.

> **Assistant's Note:** The content of this course material may adapt over time. It's recommended to read ahead if you encounter gaps.

### 🎯 Learning Goals

This week's primary learning goals are:

- Designing Java classes
- Adding instance fields
- Adding a constructor method
- Creating *getters* and *setters*
- Printing to the terminal
- Using the `main` method
- Understanding scope (or *variable shadowing*)

### 🔧 Troubleshooting Guide

If you experience any issues or have questions, follow this procedure:

1. Review this week's [posted issues](https://gits-15.sys.kth.se/inda-23/help/issues). Are others discussing your problem?
2. If not, create a [New Issue](https://gits-15.sys.kth.se/inda-23/help/issues/new) with a descriptive title beginning with "Task *x*: *summary of problem*".
3. Consult a TA during the [weekly lab](https://queue.csc.kth.se/Queue/INDA). Refer to your schedule for lab times.

You are encouraged to discuss with peers, but **do not share answers**!

### 🏆 Assignment

In this assignment, you will model a simple Java game set in a world where players, scores, and enemies interact. Using OO principles, you'll implement classes, constructors, fields, and methods to facilitate player movement, track scoring, and define enemy interactions!

#### Step 1 -- Designing the Player Class

You'll first create a `Player` class. Players have various attributes that we need to define for gameplay. Use the fields listed below:

- `String name`
- `int position`
- `int score`

These fields will represent the player's name, current position on a grid, and score.

Create your `Player` Java class and add these fields privately.

#### Step 2 -- Constructor and Getters/Setters

- Implement a **constructor** to initialize the player's name, starting position, and score.
- Add **getters** and **setters** for each field to allow interaction while maintaining encapsulation.

Here's a small example of your class's structure:

```java
public class Player {
    private String name;
    private int position;
    private int score;

    public Player(String name, int position, int score) {
        this.name = name;
        this.position = position;
        this.score = score;
    }

    // Getter and Setter methods
}
```

#### Step 3 -- Printing Information

Add a `printInfo()` method that prints a summary of the player's current state (name, position, and score) to the terminal.

#### Step 4 -- Main Method: Game Setup

Use a `main` method in which you instantiate one or more `Player` objects and test their methods.

Example:

```java
public static void main(String[] args) {
    Player hero = new Player("Hero", 0, 0);
    hero.printInfo(); // Ensure all info prints correctly
}
```

#### Step 5 -- Game Mechanics: Movement and Scoring

- Implement a `move(int distance)` method in the `Player` class that updates the player's position.
- Create a `updateScore(int points)` method to change the player's score.
- Use these methods in your `main` to simulate a player's actions.

#### Step 6 -- Introducing Enemies

Model an `Enemy` class. Enemies also have a position and can affect the player's score. Implement fields and methods similar to those in the `Player` class to represent enemies.

#### Step 7 -- Implement Interactions

- Introduce an `interact(Player player)` method in the `Enemy` class. If the `Player` is at the same position as the `Enemy`, reduce the player's score.
- Test interactions in your `main` method, simulating gameplay.

#### Step 8 -- Variable Shadowing

Consider the code below. Why does the example not work as intended? Think about *scope* and how the `this` keyword can resolve such conflicts.

```java
public class Example {
    private int data = 1;

    public void updateData(int data) {
        data = data; // Why doesn't this work?
    }
}
```

### 💡 Tips and Guidance

Refer to Java documentation and course material for detailed explanations on each concept. Understanding object-oriented principles like encapsulation, constructors, and accessors is crucial.

Happy coding, and may your players conquer their enemies!