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

    # Combine task description into a single prompt for solution generation
    prompt = (
        f"Based on the following task description, generate a complete and functional Java solution that meets all the requirements. "
        f"The solution should be well-structured, use meaningful variable names, include necessary comments for clarity, "
        f"and be ready to pass a comprehensive set of unit tests.\n\n"
        f"### Task Description\n\n"
        f"{task_description}\n\n"
        "IMPORTANT: The response must be plain Java code with no markdown formatting or ```java blocks. "
        "Ensure that the response is ready to be saved directly as .java files. "
        "Each class should be placed in an appropriately named file."
    )

    # Call OpenAI API to generate the solution code
    response_content = generate_with_retries(client, prompt, max_retries=3)
    if response_content is None:
        print("Error: Failed to generate solution code after multiple retries.")
        sys.exit(1)

    # Ensure the gen_src directory exists
    gen_src_dir = os.path.join("gen_src")
    os.makedirs(gen_src_dir, exist_ok=True)

    # Write the generated code to Java files in gen_src
    write_generated_code_to_files(gen_src_dir, response_content)

    # Commit and push changes
    commit_and_push_changes(branch_name, gen_src_dir)

def write_generated_code_to_files(directory, code_content):
    """Write generated Java code to appropriate files in the specified directory."""
    file_blocks = code_content.split("class ")
    for block in file_blocks:
        if block.strip():  # Ensure there's content
            # Validate and extract class name
            lines = block.splitlines()
            class_declaration = lines[0].strip() if lines else ""
            if "{" in class_declaration:
                class_name = class_declaration.split()[0]
                if class_name.isidentifier():  # Ensure valid class name
                    file_name = f"{class_name}.java"
                    file_path = os.path.join(directory, file_name)
                    try:
                        with open(file_path, "w") as java_file:
                            java_file.write("class " + block)
                    except IOError as e:
                        print(f"Error writing file {file_name}: {e}")
                else:
                    print(f"Invalid class name detected: '{class_name}'. Skipping block.")
            else:
                print(f"Malformed class declaration detected: {class_declaration}. Skipping block.")


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
    if not branch_name:
        print("Error: Branch name is empty.")
        sys.exit(1)

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
