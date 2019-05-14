# eInk display emulator

This is a simple emulator of a 4.3 inch e-Paper display module developed by Waveshare.

Full specification can be found [here](https://download.kamami.pl/p560206-4.3inch-e-Paper-UserManual.pdf).

## Quickstart:

* download the code
* run `python main.py`

This will start a Tkinter GUI (600x800 white canvas) and a HTTP server on `localhost:9999`.

To communicate with the module, send a GET request to `localhost:9999/{UART}` (e.g. `localhost:9999/001001001`).
In the current version, GUI display every received UART command as text in the middle of the canvas. In the future it will parse the command according to the module's specification.
