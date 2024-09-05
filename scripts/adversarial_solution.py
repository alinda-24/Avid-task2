import os
import sys
from openai import OpenAI

def main(api_key, task_file, solution_dir):
    client = OpenAI(api_key=api_key)

    # Read the task description
    try:
        with open(task_file, "r") as file:
            task_description = file.read()
    except FileNotFoundError:
        print("Error: task description file not found.")
        sys.exit(1)

    # Read the existing solution files in .hidden_tasks
    solution_files = []
    for filename in os.listdir(solution_dir):
        if filename.endswith(".java"):
            with open(os.path.join(solution_dir, filename), "r") as file:
                solution_files.append(file.read())

    solution_content = "\n\n".join(solution_files)

    # Prompt to improve the solution
    prompt = (
        f"Given the following task description and solution code, analyze the solution and improve it. "
        f"Correct any issues or missing requirements that might be present in the solution.\n\n"
        f"### Task Description\n{task_description}\n\n"
        f"### Current Solution\n{solution_content}\n\n"
        "IMPORTANT: Provide an improved version of the solution with corrections, if necessary, and ensure that the updated code is complete and functional."
        "The response must be in plain Java code with no markdown formatting or ```java blocks."
    )

    # Generate the improved solution
    improved_solution = generate_with_retries(client, prompt, max_retries=3)
    if improved_solution is None:
        print("Error: Failed to generate an improved solution.")
        sys.exit(1)

    # Overwrite the existing solution files with the improved solution
    write_improved_solution(solution_dir, improved_solution)

def generate_with_retries(client, prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating improved solution: {e}")
            if attempt < max_retries - 1:
                print("Retrying...")
    return None

def write_improved_solution(directory, improved_solution):
    """Overwrite the existing solution files with the improved solution."""
    file_blocks = improved_solution.split("class ")
    for block in file_blocks:
        if block.strip():
            class_name = block.split("{")[0].strip().split()[0]
            file_name = f"{class_name}.java"
            file_path = os.path.join(directory, file_name)

            with open(file_path, "w") as java_file:
                java_file.write("class " + block)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Error: Missing required command line arguments 'api_key', 'task_file', and 'solution_dir'")
        sys.exit(1)

    api_key = sys.argv[1]
    task_file = sys.argv[2]
    solution_dir = sys.argv[3]

    main(api_key, task_file, solution_dir)
