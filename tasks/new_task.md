# 🚀 Simple Java Game: Player vs. Enemies

Dive into the exciting world of game development with this Java assignment! You will create a basic game application with player movement, a scoring system, and enemy interactions.

### 💀 Deadline
Complete this assignment by **Friday, November 30th**.

### 👩‍🏫 Instructions
For detailed instructions on how to complete and submit this assignment, please refer to the [course instructions](https://yourcourse.edu/assignments).

### 📝 Preparation
Before you start, ensure you've completed the following readings and exercises:

- [Understanding Classes and Objects in Java](https://yourcourse.edu/module3/classes-and-objects)
- If you haven't already, register for the course platform with the key `game-dev-23` at [our learning site](https://yourcourse.edu).

> **Note:** The material may slightly differ from last year, so moving ahead is helpful if needed.

### ✅ Learning Goals

After finishing this assignment, you should be able to:

* Design Java classes
* Add instance fields
* Add a constructor method
* Create *getters* and *setters*
* Print to the terminal
* Use the `main` method
* Understand Scope (or *variable shadowing*)

### 🚨 Troubleshooting Guide
Follow these steps if you encounter issues:

1. Review this week's [frequently asked questions](https://yourcourse.edu/help/faqs).
2. Post your question in the forum by creating a [New Topic](https://yourcourse.edu/forum/new).
3. Reach out to a Teaching Assistant during [lab hours](https://yourcourse.edu/lab-schedule).

Collaborate with peers, but **do not share code directly**!

### 🎮 Assignment: Build Your Game!

In this assignment, you will develop a simple 2D game featuring player movement, a dynamic scoring system, and exciting enemy interactions. Let's begin your journey to become a game developer!

#### Exercise 1 -- Player Class
Begin by creating a `Player.java` class in the `src` folder. This class should have the following fields:

- `String name`
- `int score`
- `int positionX`
- `int positionY`

<details>
  <summary> 🛠 Example Code </summary>

  ```java
  public class Player {
  
      private String name;
      private int score;
      private int positionX;
      private int positionY;
  
      public Player(String name) {
          this.name = name;
          this.score = 0; // Starting score
          this.positionX = 0; // Starting position
          this.positionY = 0;
      }
  
      // Getter and Setter methods for each field
      public String getName() { return name; }
      public int getScore() { return score; }
      public int getPositionX() { return positionX; }
      public int getPositionY() { return positionY; }
      
      public void setPositionX(int x) { this.positionX = x; }
      public void setPositionY(int y) { this.positionY = y; }
      public void increaseScore(int points) { this.score += points; }
  
      public void printInfo() {
          System.out.println("Player: " + name);
          System.out.println("Score: " + score);
          System.out.println("Position: (" + positionX + ", " + positionY + ")");
      }
  }
  ```

  Use the provided structure to create player objects with initial values and methods to modify their state.
</details>

#### Exercise 2 -- Enemy Class
Create an `Enemy.java` class to represent game adversaries. It should include:

- `String type`
- `int positionX`
- `int positionY`
- `int damage`

<details>
  <summary> 🛠 Example Code </summary>

  ```java
  public class Enemy {

      private String type;
      private int positionX;
      private int positionY;
      private int damage;

      public Enemy(String type, int damage) {
          this.type = type;
          this.damage = damage;
          this.positionX = (int) (Math.random() * 100); // Random initial position
          this.positionY = (int) (Math.random() * 100);
      }

      // Getter methods
      public String getType() { return type; }
      public int getDamage() { return damage; }
      public int getPositionX() { return positionX; }
      public int getPositionY() { return positionY; }
  }
  ```

  These enemies will randomly appear and interact with the player. Implement and test basic movement logic by using constructors and methods.
</details>

#### Exercise 3 -- Player Movement
Implement a `move` method in the `Player` class allowing the player to navigate the game world. Movement options include:

- Up
- Down
- Left
- Right

<details>
  <summary> 🛠 Implementation Example </summary>

  ```java
  public void move(String direction) {
      switch (direction.toLowerCase()) {
          case "up": positionY++; break;
          case "down": positionY--; break;
          case "left": positionX--; break;
          case "right": positionX++; break;
          default: System.out.println("Invalid move!"); break;
      }
      System.out.println("Player moved " + direction + ". New position: (" + positionX + ", " + positionY + ")");
  }
  ```

  This method allows your player objects to interact with their environment by moving around.
</details>

#### Exercise 4 -- Interaction with Enemies
Develop an interaction method where if a `Player` comes within a certain distance (e.g., `1` unit) of an `Enemy`, the player's score decreases by the enemy's damage value.

<details>
  <summary> 🛠 Interaction Implementation </summary>

  ```java
  public void interact(Enemy enemy) {
      if (Math.abs(this.positionX - enemy.getPositionX()) <= 1 && 
          Math.abs(this.positionY - enemy.getPositionY()) <= 1) {
          this.score -= enemy.getDamage();
          System.out.println("Hit by " + enemy.getType() + "! Score decreased to: " + this.score);
      }
  }
  ```

  This ensures realistic interactions, reflecting adversaries' proximity impact.
</details>

#### Exercise 5 -- Variable Shadowing
Consider potential variable shadowing issues with similar field and method parameters. Ensure correct usage of `this` to reference instance fields. Analyze these examples:

```java
public class Example {
    private int sampleValue = 42;

    public void showValue(int sampleValue) {
        System.out.println(sampleValue); // It prints method parameter instead of instance field.
    }
}
```

Utilize these insights to prevent variable shadowing issues in your game classes.

### 🐞 Encounter a Bug or Error?
Notify us by opening a [New Issue](https://yourcourse.edu/help/issues/new) with "Game Assignment Error:" followed by a summary. Acknowledgments will be given for reporting valid bugs!

Good luck, and have fun creating your game! 🎮