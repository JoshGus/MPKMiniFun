import subprocess


def handle_action(event):

    if event["type"] == "pad":

        pad = event["pad"]

        print(f"{pad} pressed")

        if pad == "PAD_1":
            print("Running tests")
            subprocess.run(["python", "run_tests.py"])

        if pad == "PAD_2":
            print("Opening VSCode")
            subprocess.run(["code", "."])

    elif event["type"] == "note_on":

        print(f"Key pressed: {event['note']}")

    elif event["type"] == "knob":

        print(f"Knob {event['control']} → {event['value']}")