import os
import sys
import subprocess
from openai import OpenAI

def main(api_key, branch_name):
    if not api_key:
        print("Error: OpenAI API key is missing.")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    # Read the new task description
    try:
        with open("tasks/new_task.md", "r") as file:
            task_description = file.read()
    except FileNotFoundError:
        print("Error: new_task.md file not found.")
        sys.exit(1)

    # Inspirational code snippet for the solution
    inspirational_code = """
    //REPOBEE-SANITIZER-SHRED
    class Indamon {

        // Put your fields here!
        private String name;
        private int hp;
        private int attack;
        private int defense;
        boolean fainted;

        public Indamon(){
          // :)
        }

        public Indamon(String name, int hp, int attack, int defense) {
           this.name = name;
           this.hp = hp;
           this.attack = attack;
           this.defense = defense;
           this.fainted = false;
        }

        public String getName() {
          return name;
        }

        public void setName(String name) {
          this.name = name;
        }

        public int getHp() {
          return hp;
        }

        public void setHp(int hp) {
          this.hp = hp;
        }

        public int getAttack() {
          return attack;
        }

        public void setAttack(int attack) {
          this.attack = attack;
        }

        public int getDefense() {
          return defense;
        }

        public void setDefense(int defense) {
          this.defense = defense;
        }

        public boolean isFainted() {
          return fainted;
        }

        public void setFainted(boolean fainted) {
          this.fainted = fainted;
        }

        public void attack(Indamon foe){
          int attackDamage = this.attack / foe.getDefense();
          foe.setHp(foe.getHp()-attackDamage);
        }

        public static void main(String[] args) {
          // create a new "Student" object
          Indamon glassey = new Indamon();

          // assign the instance variables to meaningful values
          glassey.name = "glassey";
          glassey.hp = 10;
          glassey.attack = 5;
          glassey.defense = 5;

          // get the information of the assigned values
          System.out.println(glassey.name);
          System.out.println(glassey.hp);
          System.out.println(glassey.attack);
          System.out.println(glassey.defense);
        } // end main method

    } // end class
    """

    # Combine task description and inspirational code into a single prompt for solution generation
    prompt = (
        f"Based on the following task description, generate a complete and functional Java solution that meets all the requirements. "
        f"The solution should be well-structured, use meaningful variable names, include necessary comments for clarity, "
        f"and be ready to pass a comprehensive set of unit tests.\n\n"
        f"### Task Description\n\n"
        f"{task_description}\n\n"
        f"### Inspirational Code Snippet\n\n"
        f"{inspirational_code}\n\n"
        "IMPORTANT: The response must be plain Java code with no markdown formatting or ```java blocks. "
        "Ensure that the response is ready to be saved directly as .java files. "
        "Each class should be placed in an appropriately named file."
    )

    # Call OpenAI API to generate the solution code
    response_content = generate_with_retries(client, prompt, max_retries=3)
    if response_content is None:
        print("Error: Failed to generate solution code after multiple retries.")
        sys.exit(1)

    # Ensure the .hidden_tasks directory exists
    hidden_tasks_dir = os.path.join(".hidden_tasks")
    os.makedirs(hidden_tasks_dir, exist_ok=True)

    # Write the generated code to a Java file
    write_generated_code_to_files(hidden_tasks_dir, response_content)

    # Commit and push changes
    commit_and_push_changes(branch_name, hidden_tasks_dir)

def write_generated_code_to_files(directory, code_content):
    """Write generated Java code to appropriate files in the specified directory."""
    file_blocks = code_content.split("class ")
    for block in file_blocks:
        if block.strip():  # Ensure there's content
            class_name = block.split("{")[0].strip().split()[0]
            if not class_name.isidentifier():  # Check if the class name is valid
                print(f"Invalid class name detected: '{class_name}'. Skipping block.")
                continue
            
            file_name = f"{class_name}.java"
            file_path = os.path.join(directory, file_name)

            try:
                with open(file_path, "w") as java_file:
                    java_file.write("class " + block)
            except IOError as e:
                print(f"Error writing file {file_name}: {e}")

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
            print(f"Error generating solution code: {e}")
            if attempt < max_retries - 1:
                print("Retrying...")
    return None

def commit_and_push_changes(branch_name, directory_path):
    try:
        subprocess.run(["git", "config", "--global", "user.email", "actions@github.com"], check=True)
        subprocess.run(["git", "config", "--global", "user.name", "github-actions"], check=True)

        subprocess.run(["git", "add", directory_path], check=True)
        subprocess.run(["git", "commit", "-m", "Add generated solution"], check=True)
        subprocess.run(
            ["git", "push", "--set-upstream", "origin", branch_name],
            check=True,
            env=dict(os.environ, GIT_ASKPASS='echo', GIT_USERNAME='x-access-token', GIT_PASSWORD=os.getenv('GITHUB_TOKEN'))
        )
    except subprocess.CalledProcessError as e:
        print(f"Error committing and pushing changes: {e}")
        sys.exit(1)

if len(sys.argv) != 3:
    print("Error: Missing required command line arguments 'api_key' and 'branch_name'")
    sys.exit(1)

api_key = sys.argv[1]
branch_name = sys.argv[2]

main(api_key, branch_name)
