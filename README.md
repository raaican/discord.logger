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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
