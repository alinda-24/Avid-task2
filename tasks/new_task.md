# Alien Adventure: Simple Java Game

For the second exercise of your programming course, you will delve into the basic modeling of a simple game application using Java. You will familiarize yourself with designing Java classes and explore essential components including player movement, a scoring system, and enemy interactions.

### 💀 Deadline

This assignment should be completed and submitted by **Friday 10th November**.

### 👩‍🏫 Instructions

Please refer to the [assignments section of the course instructions](https://example.com/course-instructions#assignments) for submission guidelines.

### 📝 Preparation

You must read and complete the questions provided in Module 3 before beginning this assignment:

- Read [Building Simple Java Games](https://example.com/module3).
- Ensure your environment is set up with Java Development Kit (JDK).

> **Assistant's Note:** The learning materials are crucial for understanding how to model simple game elements using Java.

### ✅ Learning Goals

This week's learning goals include:

* Designing Java classes
* Adding instance fields
* Adding a constructor method
* Creating *getters* and *setters*
* Printing to the terminal
* Using the `main` method
* Scope (or *variable shadowing*)

### 🚨 Troubleshooting Guide

If you encounter any issues, follow this guide:

1. Check the week's [posted issues](https://example.com/help/issues) to see if others have the same problem.
2. If not, post a new question with a descriptive title, starting with "Task *x*: *summary of problem here*".
3. Discuss with peers or ask a Teaching Assistant during the weekly lab sessions. Remember not to share your solutions.

### 🏛 Assignment

You are tasked with creating a simple game where you will model game entities such as players and enemies. Use your creativity to build these elements and their interactions in Java!

#### Exercise 1: Designing Game Entities

Create a new class called `Player` in the `src` directory. Model its attributes using instance fields with the following types:

- `String` name
- `int` score
- `int` positionX
- `int` positionY

Similarly, create another class `Enemy` with:

- `String` name
- `int` damage
- `int` positionX
- `int` positionY

#### Exercise 2: Fields and Constructor

Define the fields in both `Player` and `Enemy` classes and implement a constructor for each class to initialize these fields. The constructors should allow you to set initial values for the attributes when creating new objects.

<details>
  <summary> 🛠 Example </summary>

  ```java
  public class Player {
      private String name;
      private int score;
      private int positionX;
      private int positionY;

      public Player(String name, int positionX, int positionY) {
          this.name = name; // Be cautious of Variable Shadowing!
          this.positionX = positionX;
          this.positionY = positionY;
          this.score = 0; // Initialize score to 0
      }

      // Add getters and setters here
  }

  public class Enemy {
      private String name;
      private int damage;
      private int positionX;
      private int positionY;

      public Enemy(String name, int damage, int positionX, int positionY) {
          this.name = name;
          this.damage = damage;
          this.positionX = positionX;
          this.positionY = positionY;
      }

      // Add getters and setters here
  }
  ```
</details>

#### Exercise 3: Getters and Setters

For encapsulation, ensure your fields are private and create *getters* and *setters* for accessing and modifying these fields. Make sure you have *getters* and *setters* for each field in both `Player` and `Enemy` classes.

#### Exercise 4: Interactions and Printing

Implement a method `move(int deltaX, int deltaY)` in the `Player` class that updates the player's position fields and prints the new position to the terminal. Also, add a `printStatus()` method that prints the player's name and current score.

Similarly, add similar methods to the `Enemy` class to print its status including damage capabilities and position.

<details>
  <summary> 🛠 Example of Interaction </summary>

  ```java
  public void move(int deltaX, int deltaY) {
      this.positionX += deltaX;
      this.positionY += deltaY;
      System.out.println(name + " moved to position (" + positionX + "," + positionY + ")");
  }

  public void printStatus() {
      System.out.println("Player: " + name + ", Score: " + score);
  }
  ```
</details>

#### Exercise 5: Using `main` Method

Create a `GameApp` class with a `main` method. Create instances of `Player` and `Enemy` and demonstrate their interactions by calling methods you implemented in the previous exercises. Update the score when an interaction happens, such as the player defeating an enemy or reaching a target.

<details>
  <summary> 🛠 Example `main` Method </summary>

  ```java
  public class GameApp {
      public static void main(String[] args) {
          Player player = new Player("Hero", 0, 0);
          Enemy enemy = new Enemy("Villain", 10, 5, 5);

          player.move(2, 3);
          player.printStatus();

          enemy.printStatus();
      }
  }
  ```
</details>

#### Exercise 6: Variable Shadowing

Understand and demonstrate variable shadowing. Review the following examples and be prepared to discuss them in class. Use the `this` keyword where necessary to correct shadowing issues.

```java
public class ShadowExample {
    private int value = 0;

    public void printValue() {
        int value = 100; // This causes shadowing
        System.out.println(this.value); // Use 'this' to refer to the field value
    }

    public static void main(String[] args) {
        new ShadowExample().printValue();
    }
}
```

> **Assistant's Note:** Pay attention to how local variables with the same name as instance fields can lead to unexpected behavior.

By completing these exercises, you will gain a holistic understanding of handling basic game functionalities within a Java application.