# Indamon, I choose you!

For the second exercise of INDA, you are going to practice on modelling objects in Java. You are going to acquaint yourself with the components of a Java class.

### 💀 Deadline
This work should be completed before the exercise, on **Friday 16th September**.

### 👩‍🏫 Instructions
For instructions on how to do and submit the assignment, please see the
[assignments section of the course instructions](https://gits-15.sys.kth.se/inda-22/course-instructions#assignments).

### 📝 Preparation

You must read and answer the questions in the OLI material for Module 2.

- Read [Looking Inside Classes](https://kth.oli.cmu.edu/jcourse/webui/syllabus/module.do?context=f5e5a808ac1f088812f2a8ce315bac60)
- If you have not done so, goto https://kth.oli.cmu.edu/, signup and register for the course key `dd1337-ht22`

> **Assistant's Note:** The OLI material and tasks might be slightly out of line this year, so it is ok to read ahead if you did not find all the material.

### ✅ Learning Goals

This weeks learning goals include:
* Designing Java classes
* Adding instance fields
* Adding a constructor method
* Creating *getters* and *setters*
* Printing to the terminal
* Using the `main` method
* Scope (or *variable shadowing*)

### 🚨 Troubleshooting Guide
If you have any questions or problems, follow this procedure: <br/>

1. Look at this week's [posted issues](https://gits-15.sys.kth.se/inda-22/help/issues). Are other students asking about your problem?
2. If not, post a question yourself by creating a [New Issue](https://gits-15.sys.kth.se/inda-22/help/issues/new). Add a descriptive title, beginning with "Task *x*: *summary of problem here*"
3. Ask a TA in person during the [weekly lab](https://queue.csc.kth.se/Queue/INDA). Check your schedule to see when the next lab is.

We encourage you to discuss with your course friends, but **do not share answers**!

### 🏛 Assignment

At the Campus of the Royal Institute of Technology in Stockholm, Sweden, there exists a mythical creature called *Indamon*. Your task at hand is to model these mythical creatures in Java! No one is alive to tell the story of how these creatures look, but with the help of [modern technology](https://huggingface.co/spaces/dalle-mini/dalle-mini) we have generated some picture to spur your imagination:

<img src="images/dallemini-indamons.png" width="800">

#### Exercise 2.0 -- Fields
In the [`src`](src) folder, create a new class called `Indamon.java`. In Java, you model attributes of real-world objects with [fields](https://docs.oracle.com/javase/tutorial/java/javaOO/variables.html). The *Indamon*-class is supposed to have:

- `String` name  
- `int` hp (**hit points**)
- `int` attack 
- `int` defense
- `boolean` fainted

If done correctly, the main method provided in Example 1 should compile, if added to `Indamon.java`.

<details>
  <summary> 🛠 Example 1 </summary>
  <!-- it need to be a blankspace here! -->

  ```java
  class Indamon {

    // Put your fields here!

    public static void main(String[] args) {
      // create a new "Student" object
      Indamon glassey = new Indamon();

      // assign the instance variables to meaningful values
      glassey.name = "Glassey";
      glassey.hp = 10;
      glassey.attack = 5;
      glassey.defense = 5;

      // get the information of the assigned values
      System.out.println("Name: " + glassey.name);
      System.out.println("HP: " + glassey.hp);
      System.out.println("Attack value: " + glassey.attack);
      System.out.println("Defense value: " + glassey.defense);
    } // end main method

  } // end class
  ```
</details>

#### Exercise 2.1 -- Getters and Setters
A defining concept in object-oriented programming is [encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)).
Encapsulations means preventing direct access to the state of your Indamon.
This can be done by setting the [access modifiers](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html) of the fields in the Indamon class to `private`.
However, we still want to be able to read from and write to the fields.
We can do this by adding **accessors** and **mutators** (so called *getters* and *setters* methods).
All fields should be accompanied with *getters* and *setters*, which makes a total of ten methods!
If done correctly, the provided main method in Example 2 should compile, if added to `Indamon.java`.

<details>
  <summary> 🛠 Example 2 </summary>
  <!-- it need to be a blankspace here! -->

  ```java
  class Indamon {

    // Put your fields here!

    // Put your getters and setters here!

    public static void main(String[] args) {
      // create a new "Indamon" object
      Indamon glassey = new Indamon();

      // assign the instance variables to meaningful values
      glassey.setName("Glassey");
      glassey.setHp(10);
      glassey.setAttack(5);
      glassey.setDefense(2);

      // get the information of the assigned values
      System.out.println("Name: " + glassey.getName());
      System.out.println("HP: " + glassey.getHp());
      System.out.println("Attack value: " + glassey.getAttack());
      System.out.println("Defense value: " + glassey.getDefense());
      System.out.println("Is fainted: " + glassey.isFainted());
    } // end main method

  } // end class
  ```
</details>

> **Assistant's Note:** The getters and setters of a field of `boolean` type follows a different naming convention from the usual `getXXX()` and `setXXX`: `isFainted()` and `setFainted()`.

#### Exercise 2.2 -- Constructor
Example 2 is a bit tedious; you dont want to add attributes to each object you create in this way. Instead, you should use a *constructor*. Implement a constructor following the examples in the OLI material (or the [Official Oracle tutorial](https://docs.oracle.com/javase/tutorial/java/javaOO/constructors.html)), and repeat example 2 with this implementation.

#### Exercise 2.3 -- `printInfo()`
You want a way to print all the info about the indamon to the terminal. Take a look at Example 3 and implement a method called `printInfo()`. The return type should be `void`. 

<details>
  <summary> 🛠 Example 3 </summary>

  ```java
  public static void main(String[] args){
    // create a new "Indamon" object
    Indamon glassey = new Indamon();

    // assign the instance variables to meaningful values
    // NOTE: if Exercise 2.3 is done correctly, you should use the constructor instead!
    glassey.setName("Glassey");
    glassey.setHp(10);
    glassey.setAttack(5);
    glassey.setDefense(2);

    // print information
    glassey.printInfo();
  }
  ```

  This call should print a message to the terminal:

  ```
  > INFO
  > Indamon: Glassey.
  > HP: 10
  > Attack: 5
  > Defense: 2
  > Fainted: false
  ```

</details>

#### Exercise 2.4 -- Indamon, attack!
Indamons are fierce creatures, and now we want to model a fight between them. In order to abstract this new functionality you must implement a method called `attack` which will receive an Indamon object that represents the opponent in battle. If indamon *A* is attacking indamon *B*, the damage done is following the formula: 

<img src="images/indamon-attack.png" alt="Indamon, attack!" width="400"/>

It should print the status to the terminal.

> **Assistant's Note:** to define the return type of the method think about what it's expecting to happen and what the instructions says about returning. Use the `getters` and `setters`to change the value of the object.

<details>
  <summary> 🛠 Example 4 </summary>

  ```java
  public static void main(String[] args){
    // create two new "indamon" objects
    Indamon glassey = new Indamon("Glassey", 10, 5, 5); 
    Indamon siberov = new Indamon("Siberov", 10, 5, 5);

    // call the "attack" method on glassey with siberov as an argument
    glassey.attack(siberov);

  }
  ```

  This call should print a similar message to the terminal:

  ```
  > Indamon Glassey attacked indamon Siberov för 1.0 damage! 
  > Indamon Siberov has 9 hp left!
  ```

</details>

#### Exercise 2.5 -- Variable Shadowing
Take a look at the *Variable shadowing*-examples below. You might be asked to explained on how to fix this example in class, so be prepared.
You can look at the article of Variable Shadowing on [Wikipedia](https://en.wikipedia.org/wiki/Variable_shadowing) and how the Java keyword [this](https://docs.oracle.com/javase/tutorial/java/javaOO/thiskey.html) works.


```Java
public class Shadow1 {
    private int number = 0; // I want this number printed :(

    public void printShadow() {
        int number = 5;
        System.out.println(number); // It is printing the wrong number :(
    }
    
    public static void main(String[] args){
        new Shadow().printShadow();
    }
}
```

Here is another example:

```Java
import java.awt.Color;

public class Horse {
  private String name;
  private Color color;
  
  public Horse(String name, Color color) {
    name = name; // this doesn't work :( Why?
    color = color;
  }
  
  public neigh(){
    String name = "Uncle Dolan";
    System.out.println(name + " neighs! Eiiigha!"); // It is printing the wrong name :( 
  }
}
```

> **Assistant's Note:** Think about the *local scope*, *global variables* and *instance fields* of the provided examples.


### 🐞 Bugs and errors?
If you find any inconsistences or errors in this exercise, please open a [New Issue](https://gits-15.sys.kth.se/inda-22/help/issues/new) with the title "Task *x* Error: *summary of error here*". Found bugs will be rewarded by mentions in the acknowledgment section.

### 🙏  Acknowledgment
This task was designed by                <br>
[Linus Östlund](mailto:linusost@kth.se)  <br>
[Sofia Bobadilla](mailto:sofbob@kth.se)  <br>
[Gabriel Skoglund](mailto:gabsko@kth.se) <br>
[Arvid Siberov](mailto:asiberov@kth.se)  <br>
