# MPK Mini MIDI Project Setup (macOS & Windows)

This README explains how to set up this project on **macOS and Windows**, including:

* Python version alignment
* Virtual environment (`venv`) setup
* Installing dependencies
* MIDI input verification
* **Microphone / Discord audio routing**

This project assumes you are using **Python 3.12.x** for compatibility with `pygame.midi`.

---

## 1. Python Version (Required)

⚠️ **Important**: Do NOT use Python 3.13 or newer. MIDI support in pygame is broken there.

### Target version

```
Python 3.12.x
```

---

## 2. Repository Setup (All Platforms)

Clone your repository:

```bash
git clone <your-repo-url>
cd MPKMiniFun
```

---

## 3. Virtual Environment Setup

### macOS

```bash
python3.12 -m venv venv
source venv/bin/activate
```

Deactivate later with:

```bash
deactivate
```

Remove venv if needed:

```bash
rm -rf venv
```

---

### Windows (PowerShell)

```powershell
py -3.12 -m venv venv
venv\Scripts\activate
```

Deactivate:

```powershell
deactivate
```

Remove venv:

```powershell
rmdir /s /q venv
```

---

## 4. Install Dependencies

Inside the activated venv:

```bash
pip install --upgrade pip
pip install pygame
```

(Optional but recommended) lock versions:

```bash
pip freeze > requirements.txt
```

---

## 5. Verify pygame MIDI

Run this test script:

```bash
python - <<EOF
import pygame
import pygame.midi
pygame.midi.init()
print("pygame.midi OK")
print(pygame.midi.get_count(), "MIDI devices detected")
EOF
```

If this succeeds, MIDI support is working.

---

## 6. Verify MPK Mini Detection

Temporarily add this debug code:

```python
import pygame.midi
pygame.midi.init()

for i in range(pygame.midi.get_count()):
    print(i, pygame.midi.get_device_info(i))
```

Confirm your MPK Mini appears as an **input device**.

---

## 7. Microphone / Discord Audio Setup

Your MIDI controller does **not** produce audio by itself.
Your program must generate audio and route it to Discord via a **virtual microphone**.

### macOS Audio Routing

1. Install a virtual audio device (e.g. BlackHole or Loopback)
2. Open **Audio MIDI Setup**
3. Create a **Multi-Output Device** (optional)
4. Set your program to output audio to the virtual device
5. In Discord:

   * Settings → Voice & Video
   * Input Device → virtual audio device

macOS may prompt for **Microphone permission** — allow it.

---

### Windows Audio Routing

1. Install a virtual audio cable (e.g. VB-Audio Virtual Cable)
2. Set your program to output audio to the virtual cable
3. In Discord:

   * Settings → Voice & Video
   * Input Device → virtual cable

If audio is distorted:

* Disable Discord noise suppression
* Disable echo cancellation

---

## 8. Project Workflow

Typical dev loop:

```bash
source venv/bin/activate   # macOS
# or venv\Scripts\activate  # Windows

python main.py
```

Stop with `Ctrl+C`, then:

```bash
deactivate
```

---

## 9. Common Issues

### pygame.midi import error

* Ensure Python version is **3.12.x**
* Recreate the venv

### MPK Mini not detected

* Close DAWs or MIDI software
* Replug USB
* Restart Python

### No audio in Discord

* Confirm Discord input device
* Confirm app outputs to virtual mic
* Check OS microphone permissions

---

## 10. Notes

* Keep macOS and Windows environments aligned
* Do not commit `venv/`
* Commit `requirements.txt`

---

You are now ready to use the MPK Mini as a programmable input devic
