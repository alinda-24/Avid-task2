import os
import sys
import subprocess
from datetime import datetime
from openai import OpenAI
import pytz
from pytz import timezone

def main(api_key):
    if not api_key:
        print("Error: OpenAI API key is missing.")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    # Extract theme and language from environment variables
    theme = os.getenv("TASK_THEME", "Create a basic Java application with the following requirements.")
    language = os.getenv("TASK_LANGUAGE", "English")

    # Combine theme into a single prompt
    learning_goals = """
              "* Designing Java classes\n"
              "* Adding instance fields\n"
              "* Adding a constructor method\n"
              "* Creating *getters* and *setters*\n"
              "* Printing to the terminal\n"
              "* Using the `main` method\n"
              "* Scope (or *variable shadowing*)\n\n"
              """
    
    original_structure = """
            "# Indamon, I choose you!\n\n"
              "For the second exercise of INDA, you are going to practice on modelling objects in Java. You are going to acquaint yourself with the components of a Java class.\n\n"
              "### 💀 Deadline\n"
              "This work should be completed before the exercise, on **Friday 16th September**.\n\n"
              "### 👩‍🏫 Instructions\n"
              "For instructions on how to do and submit the assignment, please see the "
              "[assignments section of the course instructions](https://gits-15.sys.kth.se/inda-22/course-instructions#assignments).\n\n"
              "### 📝 Preparation\n"
              "You must read and answer the questions in the OLI material for Module 2.\n\n"
              "- Read [Looking Inside Classes](https://kth.oli.cmu.edu/jcourse/webui/syllabus/module.do?context=f5e5a808ac1f088812f2a8ce315bac60)\n"
              "- If you have not done so, goto https://kth.oli.cmu.edu/, signup and register for the course key `dd1337-ht22`\n\n"
              "> **Assistant's Note:** The OLI material and tasks might be slightly out of line this year, so it is ok to read ahead if you did not find all the material.\n\n"
              "### ✅ Learning Goals\n\n"
              "This weeks learning goals include:\n"
              "* Designing Java classes\n"
              "* Adding instance fields\n"
              "* Adding a constructor method\n"
              "* Creating *getters* and *setters*\n"
              "* Printing to the terminal\n"
              "* Using the `main` method\n"
              "* Scope (or *variable shadowing*)\n\n"
              "### 🚨 Troubleshooting Guide\n"
              "If you have any questions or problems, follow this procedure:\n\n"
              "1. Look at this week's [posted issues](https://gits-15.sys.kth.se/inda-22/help/issues). Are other students asking about your problem?\n"
              "2. If not, post a question yourself by creating a [New Issue](https://gits-15.sys.kth.se/inda-22/help/issues/new). Add a descriptive title, beginning with \"Task *x*: *summary of problem here*\"\n"
              "3. Ask a TA in person during the [weekly lab](https://queue.csc.kth.se/Queue/INDA). Check your schedule to see when the next lab is.\n\n"
              "We encourage you to discuss with your course friends, but **do not share answers**!\n\n"
              "### 🏛 Assignment\n\n"
              "At the Campus of the Royal Institute of Technology in Stockholm, Sweden, there exists a mythical creature called *Indamon*. Your task at hand is to model these mythical creatures in Java! No one is alive to tell the story of how these creatures look, but with the help of [modern technology](https://huggingface.co/spaces/dalle-mini/dalle-mini) we have generated some picture to spur your imagination:\n\n"
              "<img src=\"images/dallemini-indamons.png\" width=\"800\">\n\n"
              "#### Exercise 2.0 -- Fields\n"
              "In the [`src`](src) folder, create a new class called `Indamon.java`. In Java, you model attributes of real-world objects with [fields](https://docs.oracle.com/javase/tutorial/java/javaOO/variables.html). The *Indamon*-class is supposed to have:\n\n"
              "- `String` name\n"
              "- `int` hp (**hit points**)\n"
              "- `int` attack\n"
              "- `int` defense\n"
              "- `boolean` fainted\n\n"
              "If done correctly, the main method provided in Example 1 should compile, if added to `Indamon.java`.\n\n"
              "<details>\n"
              "  <summary> 🛠 Example 1 </summary>\n\n"
              "  ```java\n"
              "  class Indamon {\n\n"
              "    // Put your fields here!\n\n"
              "    public static void main(String[] args) {\n"
              "      // create a new \"Student\" object\n"
              "      Indamon glassey = new Indamon();\n\n"
              "      // assign the instance variables to meaningful values\n"
              "      glassey.name = \"Glassey\";\n"
              "      glassey.hp = 10;\n"
              "      glassey.attack = 5;\n"
              "      glassey.defense = 5;\n\n"
              "      // get the information of the assigned values\n"
              "      System.out.println(\"Name: \" + glassey.name);\n"
              "      System.out.println(\"HP: \" + glassey.hp);\n"
              "      System.out.println(\"Attack value: \" + glassey.attack);\n"
              "      System.out.println(\"Defense value: \" + glassey.defense);\n"
              "    } // end main method\n\n"
              "  } // end class\n"
              "  ```\n"
              "</details>\n\n"
              "#### Exercise 2.1 -- Getters and Setters\n"
              "A defining concept in object-oriented programming is [encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)).\n"
              "Encapsulations means preventing direct access to the state of your Indamon.\n"
              "This can be done by setting the [access modifiers](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html) of the fields in the Indamon class to `private`.\n"
              "However, we still want to be able to read from and write to the fields.\n"
              "We can do this by adding **accessors** and **mutators** (so called *getters* and *setters* methods).\n"
              "All fields should be accompanied with *getters* and *setters*, which makes a total of ten methods!\n"
              "If done correctly, the provided main method in Example 2 should compile, if added to `Indamon.java`.\n\n"
              "<details>\n"
              "  <summary> 🛠 Example 2 </summary>\n\n"
              "  ```java\n"
              "  class Indamon {\n\n"
              "    // Put your fields here!\n\n"
              "    // Put your getters and setters here!\n\n"
              "    public static void main(String[] args) {\n"
              "      // create a new \"Indamon\" object\n"
              "      Indamon glassey = new Indamon();\n\n"
              "      // assign the instance variables to meaningful values\n"
              "      glassey.setName(\"Glassey\");\n"
              "      glassey.setHp(10);\n"
              "      glassey.setAttack(5);\n"
              "      glassey.setDefense(2);\n\n"
              "      // get the information of the assigned values\n"
              "      System.out.println(\"Name: \" + glassey.getName());\n"
              "      System.out.println(\"HP: \" + glassey.getHp());\n"
              "      System.out.println(\"Attack value: \" + glassey.getAttack());\n"
              "      System.out.println(\"Defense value: \" + glassey.getDefense());\n"
              "      System.out.println(\"Is fainted: \" + glassey.isFainted());\n"
              "    } // end main method\n\n"
              "  } // end class\n"
              "  ```\n"
              "</details>\n\n"
              "> **Assistant's Note:** The getters and setters of a field of `boolean` type follows a different naming convention from the usual `getXXX()` and `setXXX`: `isFainted()` and `setFainted()`.\n\n"
              "#### Exercise 2.2 -- Constructor\n"
              "Example 2 is a bit tedious; you dont want to add attributes to each object you create in this way. Instead, you should use a *constructor*. Implement a constructor following the examples in the OLI material (or the [Official Oracle tutorial](https://docs.oracle.com/javase/tutorial/java/javaOO/constructors.html)), and repeat example 2 with this implementation.\n\n"
              "#### Exercise 2.3 -- `printInfo()`\n"
              "You want a way to print all the info about the indamon to the terminal. Take a look at Example 3 and implement a method called `printInfo()`. The return type should be `void`.\n\n"
              "<details>\n"
              "  <summary> 🛠 Example 3 </summary>\n\n"
              "  ```java\n"
              "  public static void main(String[] args){\n"
              "    // create a new \"Indamon\" object\n"
              "    Indamon glassey = new Indamon();\n\n"
              "    // assign the instance variables to meaningful values\n"
              "    // NOTE: if Exercise 2.3 is done correctly, you should use the constructor instead!\n"
              "    glassey.setName(\"Glassey\");\n"
              "    glassey.setHp(10);\n"
              "    glassey.setAttack(5);\n"
              "    glassey.setDefense(2);\n\n"
              "    // print information\n"
              "    glassey.printInfo();\n"
              "  }\n"
              "  ```\n\n"
              "  This call should print a message to the terminal:\n\n"
              "  ```\n"
              "  > INFO\n"
              "  > Indamon: Glassey.\n"
              "  > HP: 10\n"
              "  > Attack: 5\n"
              "  > Defense: 2\n"
              "  > Fainted: false\n"
              "  ```\n"
              "</details>\n\n"
              "#### Exercise 2.4 -- Indamon, attack!\n"
              "Indamons are fierce creatures, and now we want to model a fight between them. In order to abstract this new functionality you must implement a method called `attack` which will receive an Indamon object that represents the opponent in battle. If indamon *A* is attacking indamon *B*, the damage done is following the formula:\n\n"
              "<img src=\"images/indamon-attack.png\" alt=\"Indamon, attack!\" width=\"400\"/>\n\n"
              "It should print the status to the terminal.\n\n"
              "> **Assistant's Note:** to define the return type of the method think about what it's expecting to happen and what the instructions says about returning. Use the `getters` and `setters`to change the value of the object.\n\n"
              "<details>\n"
              "  <summary> 🛠 Example 4 </summary>\n\n"
              "  ```java\n"
              "  public static void main(String[] args){\n"
              "    // create two new \"indamon\" objects\n"
              "    Indamon glassey = new Indamon(\"Glassey\", 10, 5, 5);\n"
              "    Indamon siberov = new Indamon(\"Siberov\", 10, 5, 5);\n\n"
              "    // call the \"attack\" method on glassey with siberov as an argument\n"
              "    glassey.attack(siberov);\n\n"
              "  }\n"
              "  ```\n\n"
              "  This call should print a similar message to the terminal:\n\n"
              "  ```\n"
              "  > Indamon Glassey attacked indamon Siberov för 1.0 damage!\n"
              "  > Indamon Siberov has 9 hp left!\n"
              "  ```\n"
              "</details>\n\n"
              "#### Exercise 2.5 -- Variable Shadowing\n"
              "Take a look at the *Variable shadowing*-examples below. You might be asked to explained on how to fix this example in class, so be prepared.\n"
              "You can look at the article of Variable Shadowing on [Wikipedia](https://en.wikipedia.org/wiki/Variable_shadowing) and how the Java keyword [this](https://docs.oracle.com/javase/tutorial/java/javaOO/thiskey.html) works.\n\n"
              "```Java\n"
              "public class Shadow1 {\n"
              "    private int number = 0; // I want this number printed :(\n\n"
              "    public void printShadow() {\n"
              "        int number = 5;\n"
              "        System.out.println(number); // It is printing the wrong number :(\n"
              "    }\n\n"
              "    public static void main(String[] args){\n"
              "        new Shadow().printShadow();\n"
              "    }\n"
              "}\n"
              "```\n\n"
              "Here is another example:\n\n"
              "```Java\n"
              "import java.awt.Color;\n\n"
              "public class Horse {\n"
              "  private String name;\n"
              "  private Color color;\n\n"
              "  public Horse(String name, Color color) {\n"
              "    name = name; // this doesn't work :( Why?\n"
              "    color = color;\n"
              "  }\n\n"
              "  public neigh(){\n"
              "    String name = \"Uncle Dolan\";\n"
              "    System.out.println(name + \" neighs! Eiiigha!\"); // It is printing the wrong name :( \n"
              "  }\n"
              "}\n"
              "```\n\n"
              "> **Assistant's Note:** Think about the *local scope*, *global variables* and *instance fields* of the provided examples.\n\n"

              """

    prompt = (f"Create a new programming task in {language} with the following theme: {theme}. "
              f"It is paramount that the generted task description includes and integrates the concepts of {learning_goals}"
              f"The task should follow a similar structure and format to the provided example {original_structure} , including detailed instructions, preparation steps, learning goals, and assignment description with exercises. "
              f"Make sure to include the title, subtitle, and emojis for aesthetics. "
              f"The description should be detailed, well-structured, and aesthetically pleasing to provide thorough instructions for the students."
             )

    # Call OpenAI API to generate the task description
    response_content = generate_with_retries(client, prompt, max_retries=3)
    if response_content is None:
        print("Error: Failed to generate task description after multiple retries.")
        sys.exit(1)

    # Create a new branch with a unique name
    stockholm_tz = timezone('Europe/Stockholm')
    branch_name = f"task-{datetime.now(stockholm_tz).strftime('%Y%m%d%H%M')}"
    create_branch(branch_name)

    # Write the response content to a markdown file
    task_file_path = os.path.join("tasks", "new_task.md")
    with open(task_file_path, "w") as file:
        file.write(response_content)

    # Commit and push changes
    commit_and_push_changes(branch_name, task_file_path)

    # Output the branch name for the next job
    print(f"::set-output name=branch_name::{branch_name}")

def generate_with_retries(client, prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-2024-08-06",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating task description: {e}")
            if attempt < max_retries - 1:
                print("Retrying...")
    return None

def create_branch(branch_name):
    try:
        subprocess.run(["git", "checkout", "-b", branch_name], check=True)
        subprocess.run(
            ["git", "push", "-u", "origin", branch_name],
            check=True,
            env=dict(os.environ, GIT_ASKPASS='echo', GIT_USERNAME='x-access-token', GIT_PASSWORD=os.getenv('GITHUB_TOKEN'))
        )
    except subprocess.CalledProcessError as e:
        print(f"Error creating branch: {e}")
        sys.exit(1)

def commit_and_push_changes(branch_name, task_file_path):
    try:
        subprocess.run(["git", "config", "--global", "user.email", "actions@github.com"], check=True)
        subprocess.run(["git", "config", "--global", "user.name", "github-actions"], check=True)

        subprocess.run(["git", "add", task_file_path], check=True)
        subprocess.run(["git", "commit", "-m", f"Add new task description: {branch_name}"], check=True)
        subprocess.run(
            ["git", "push", "--set-upstream", "origin", branch_name],
            check=True,
            env=dict(os.environ, GIT_ASKPASS='echo', GIT_USERNAME='x-access-token', GIT_PASSWORD=os.getenv('GITHUB_TOKEN'))
        )
    except subprocess.CalledProcessError as e:
        print(f"Error committing and pushing changes: {e}")
        sys.exit(1)

if len(sys.argv) != 2:
    print("Error: Missing required command line argument 'api_key'")
    sys.exit(1)

api_key = sys.argv[1]

main(api_key)
