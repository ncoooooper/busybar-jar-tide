# Jar Tide

Follow one monobank jar, its remaining goal and the latest balance change.

Set MONO_TOKEN in the environment of the companion and set jar in config.json to the specific jar ID or sendId. Tokens stay on your computer. The selected balance is returned in major currency units, including cents. A missing or zero target is shown as no goal. The personal client-info endpoint is read at most once per 65 seconds. See https://api.monobank.ua/docs/.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run locally

From this folder, run `~/.busy-emulator/bin/busy-emulator dev --once` with BUSY Bar Emulator open. Back exits.

![BUSY Bar front display](screenshots/front-1.png)
