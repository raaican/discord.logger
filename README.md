# discord.logger
A simple Discord logger app using the discord.py module.
This project is currently a work in progress.
## Features
* Log Events to a specified mod-logs channel such as:
  * a User deleted a message
  * a User Interacted with voice channel(s):
    * joined,
    * left,
    * switched,
    * created (using [Voice Master](https://voicemaster.xyz/))

 * Simple slash command to send a Discord Server invite link

## DISCLAIMER
To run this APP smoothly, you'll need to be familiar with reading and understanding the source code. The APP may require adjustments or customization based on your specific needs and environment, and being able to navigate and modify the code will be essential for proper setup and operation.

## Installation
1. Clone the repo:

    ```sh
    git clone "https://github.com/dREADEDbIRD/discord.logger"
    cd discord.logger/
    ```

2. Copy `config-example.py` to `config.py` file:
    ```sh
    cp config-example.py config.py
    ```

3. Edit `config.py` using your editor of choice to fill the required fields

    * Create a [discord bot](https://discordpy.readthedocs.io/en/stable/discord.html) if you haven't already to grab your token

4. Setup python venv to run the bot:

    ```sh
    python3 -m venv venv
    or
    python -m venv venv
    ```

5. Enter python venv:

    * **Unix**:

    ```sh
    source venv/bin/activate
    ```

    * **Windows**:
    **Note: delete the *shebang* on main.py if you are on Windows**
        * **cmd.exe**:

        ```sh
        venv\Scripts\activate.bat
        ```

        * **PowerShell**:
    
        ```sh
        venv\Scripts\Activate.ps1
        ```

6. Install requirements:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run `main.py`

    * **Unix**:
        ```sh
        chmod +x main.py
        ./main.py
        ```

    * **Windows**:
        * Enter venv if you haven't and run main.py:

            ```sh
            python main.py
            ```
 ## Running with Docker

 I have provided a [Dockerfile](Dockerfile) to build the image.

 1. Build the image

 ```sh
 docker build -t logger .
 ```

 2. Run the container

 ```sh
 docker run -d --name discord.logger logger
 ```

## License
Copyright (c) 2024 raican

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
