# advent-of-code-downloader

Simple CLI tool, written in Python, for downloading the input file and instructions for Advent of Code. Works anywhere where Python works (which includes Windows, Mac, and Linux).

# Usage

- Make sure the [latest version of Python](https://www.python.org/) is installed. `3.10` will work; `3.9` will probably work (but I haven't tested it); anything older may need some tweaking to the code.
- Download this code from Releases. I recommend putting it in its own folder.
- Run `pip install -r requirements.txt` to install the required packages.
- Find your session key. These instructions should work for Edge, Chrome, Firefox, and possibly other browsers.
    - Press Ctrl+Shift+I to open the Developer Tools.
    - Click on the `Network` tab.
    - Go to an Advent of Code page, like [Day 1](https://adventofcode.com/2021/day/1). Or, reload the page if you were already on one.
    - You'll see a table of requests. Click the one that has your day number. For example, for the Day 1 page, this request will say simply `1`.
    - You'll see a new section pop up. It should have the `Headers` tab selected by default. Select that tab if it isn't already selected.
    - Look for the line that says `cookie:`. Scroll down if you don't see it. Or, try toggling open the label that says `Request Headers.`
    - Copy all the text **after** `session=`. You'll need it soon!
    - **IMPORTANT**: This session key is unique to you. Keep it secret!
- Run the app using this format: `main.py [year] [day number] [session ID]`
- For example: `main.py 2021 1 12345notarealsessionkey67890`
- The input will be in the same folder, called `input.txt`. The first set of instructions will be called `instructions-one.md`. The second set of instructions, if you've unlocked it, will be called `instructions-two.md`.