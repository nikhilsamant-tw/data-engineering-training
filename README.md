[![Built with Devbox](https://www.jetify.com/img/devbox/shield_galaxy.svg)](https://www.jetify.com/devbox/docs/contributor-quickstart/)

## Apache Spark Hands-On Practice
This repository was created to provide a hands-on environment for practicing and learning Apache Spark. It includes various examples, exercises, and projects to help users understand and master the concepts of distributed data processing using Apache Spark. By using Devbox, we ensure a consistent and reproducible development environment, making it easier for contributors to get started and collaborate effectively.

### Local setup using Devbox

#### Prerequisites
- Ensure you have [Devbox](https://jetify-com.vercel.app/docs/devbox/installing_devbox/) installed on your machine.
- (Optional)Ensure you have [Direnv](https://direnv.net/#basic-installation) installed and hooked into you shell.

#### Setting up the environment
1. Clone the repository:
    ```sh
    git clone https://github.com/nikhilsamant-tw/data-engineering-training.git
    cd data-engineering-training
    ```

2. Initialize the Devbox environment:
    ```sh
    devbox shell
    ```

3. The Devbox environment will automatically set up the required packages specified in [devbox.json](http://_vscodecontentref_/1):
    - Python 3.11
    - JDK 11
    - Spark 3.5.4

4. To activate the virtual environment, run:
    ```sh
    source .venv/bin/activate
    pip3 install pyspark py4j IPython pandas pyarrow
    ```

5. You can now run your Apache Spark applications or any other scripts within this environment.

### Creating Your Own Devbox
If you want to create your own Devbox setup, follow these steps:

1. Install Devbox by following the installation guide.

2. Create a new directory for your project:
    ```sh
    mkdir my-devbox-project
    cd my-devbox-project
    ```

3. Initialize a new Devbox project:
    ```sh
    devbox init
    ```

4. Add the required packages to your ```devbox.json``` file. For example, to add Python 3.11 and JDK 11:
    ```json
    {
    "$schema": "https://raw.githubusercontent.com/jetify-com/devbox/0.13.7/.schema/devbox.schema.json",
    "packages": [
        "python@3.11",
        "jdk@11",
        "spark@3.5.4"
    ],
    "shell": {
        "init_hook": [
        "echo 'Welcome to devbox!' > /dev/null"
        ],
        "scripts": {
        "test": [
            "echo \"Error: no test specified\" && exit 1"
        ]
        }
    }
    }
    ```

5. Start the Devbox shell:
    ```sh
    devbox shell
    ```

6. Create and activate a virtual environment:
    ```sh
    python -m venv .venv
    source .venv/bin/activate
    pip3 install pyspark py4j IPython pandas pyarrow
    ```
You can now install additional Python packages using pip or add more packages to your ```devbox.json``` file as needed.

For more detailed instructions, refer to the [Devbox documentation](https://www.jetify.com/devbox/docs/contributor-quickstart/).