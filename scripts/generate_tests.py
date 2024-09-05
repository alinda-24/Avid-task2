import os
import sys
import subprocess
from openai import OpenAI

def main(api_key, branch_name):
    if not api_key:
        print("Error: OpenAI API key is missing.")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    # Ensure we are on the correct branch
    try:
        subprocess.run(["git", "checkout", branch_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error checking out branch {branch_name}: {e}")
        sys.exit(1)

    # Read the solution code from the .hidden_tasks directory
    solution_files = []
    try:
        for filename in os.listdir(".hidden_tasks"):
            if filename.endswith(".java"):
                with open(os.path.join(".hidden_tasks", filename), "r") as file:
                    solution_files.append(file.read())
    except FileNotFoundError:
        print("Error: Solution files not found in .hidden_tasks directory.")
        sys.exit(1)

    if not solution_files:
        print("Error: No Java solution files found in .hidden_tasks.")
        sys.exit(1)

    solution = "\n\n".join(solution_files)

    # Example tests to inspire the model (not to be directly copied)
    example_tests = """
    package original;
    import org.junit.Before;
    import org.junit.Test;
    import static org.junit.Assert.*;

    public class IndamonTest {
        private Indamon indamon1;
        private Indamon indamon2;

        @Before
        public void setUp() {
            indamon1 = new Indamon("Glassey", 10, 5, 5);
            indamon2 = new Indamon("Siberov", 10, 5, 5);
        }

        @Test
        public void testGetName() {
            assertEquals("Glassey", indamon1.getName());
            assertEquals("Siberov", indamon2.getName());
        }

        @Test
        public void testGetHp() {
            assertEquals(10, indamon1.getHp());
            assertEquals(10, indamon2.getHp());
        }

        @Test
        public void testGetAttack() {
            assertEquals(5, indamon1.getAttack());
            assertEquals(5, indamon2.getAttack());
        }

        @Test
        public void testGetDefense() {
            assertEquals(5, indamon1.getDefense());
            assertEquals(5, indamon2.getDefense());
        }

        @Test
        public void testGetFainted() {
            assertEquals(false, indamon1.getFainted());
            assertEquals(false, indamon2.getFainted());
        }

        @Test
        public void testSetName() {
            indamon1.setName("NewName");
            assertEquals("NewName", indamon1.getName());
        }

        @Test
        public void testSetHp() {
            indamon1.setHp(20);
            assertEquals(20, indamon1.getHp());
        }

        @Test
        public void testSetAttack() {
            indamon1.setAttack(7);
            assertEquals(7, indamon1.getAttack());
        }

        @Test
        public void testSetDefense() {
            indamon1.setDefense(8);
            assertEquals(8, indamon1.getDefense());
        }

        @Test
        public void testSetFainted() {
            indamon1.setFainted(true);
            assertEquals(true, indamon1.getFainted());
        }

        @Test
        public void testAttack() {
            indamon1 = new Indamon("Glassey", 10, 5, 5);
            indamon2 = new Indamon("Siberov", 10, 5, 5);
            indamon1.attack(indamon2);
            assertEquals(9, indamon2.getHp()); 
            assertEquals(false, indamon2.getFainted());
        }
    }
    """

    # Combine the solution into a single prompt for test generation
    prompt = (
        f"Given the following Java solution, generate a set of high-quality unit tests. "
        f"Ensure the tests are thorough, robust, and cover all edge cases, including invalid inputs, boundary conditions, and performance considerations. "
        f"The tests should follow best practices, including descriptive naming conventions, setup and teardown methods if necessary, and detailed assertions to validate expected behavior. "
        f"Ensure that the tests use the correct imports and that each class is placed in the correct file as per Java naming conventions.\n\n"
        f"### Solution\n{solution}\n\n"
        f"### Example Tests (for inspiration only)\n{example_tests}\n\n"
        "IMPORTANT: The response must be plain Java code with no markdown formatting or ```java blocks. Ensure that the response is ready to be saved directly as a .java file."
    )

    response_content = generate_with_retries(client, prompt, max_retries=3)
    if response_content is None:
        print("Error: Failed to generate the tests after multiple retries.")
        sys.exit(1)

    # Write the generated tests to appropriate Java files in the gen_test directory
    gen_test_dir = os.path.join("gen_test")
    write_generated_tests_to_files(gen_test_dir, response_content)

    # Commit and push changes
    commit_and_push_changes(branch_name, gen_test_dir)

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
            print(f"Error generating the tests: {e}")
            if attempt < max_retries - 1:
                print("Retrying...")
    return None

def write_generated_tests_to_files(directory, code_content):
    """Write generated Java tests to separate files based on class names."""
    file_blocks = code_content.split("class ")
    for block in file_blocks:
        if block.strip():  # Ensure there's content
            class_name = block.split("{")[0].strip().split()[0]
            if not class_name.isidentifier():  # Check if the class name is valid
                print(f"Invalid class name detected: '{class_name}'. Skipping block.")
                continue
            
            # Construct the file content
            package_declaration = "package test;\n\n"
            imports = (
                "import org.junit.Before;\n"
                "import org.junit.Test;\n"
                "import static org.junit.Assert.*;\n\n"
            )
            file_content = package_declaration + imports + "class " + block

            file_name = f"{class_name}.java"
            file_path = os.path.join(directory, file_name)

            # Ensure the directory exists
            os.makedirs(directory, exist_ok=True)

            try:
                with open(file_path, "w") as java_file:
                    java_file.write(file_content)
            except IOError as e:
                print(f"Error writing file {file_name}: {e}")


def commit_and_push_changes(branch_name, directory):
    try:
        subprocess.run(["git", "config", "--global", "user.email", "actions@github.com"], check=True)
        subprocess.run(["git", "config", "--global", "user.name", "github-actions"], check=True)

        subprocess.run(["git", "add", directory], check=True)
        subprocess.run(["git", "commit", "-m", "Add generated tests"], check=True)
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
