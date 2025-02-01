# volume_controller
Open-source app to lock audio volume on Steam Deck, preventing accidental changes in Game/Desktop Mode.   Features a SteamOS-themed UI, volume persistence, and systemd auto-start support.   Free to use, modify, and share under MIT License.

# Steam Deck Volume Lock 🔒

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/Python-3.9%2B-green)

A Steam Deck app to lock audio volume to a specific level, preventing accidental changes in **Game Mode** or **Desktop Mode**. Perfect for avoiding random volume spikes!

![App Screenshot](SteamVolumeLock.png)


## Features ✨
- 🔒 Lock/Unlock toggle with visual feedback
- SteamOS-inspired dark theme UI
- Real-time volume percentage display
- Gamepad-friendly controls in Game Mode
- Auto-start on boot (systemd service)
- Safe exit handling
- Lightweight (~200 lines of Python)

## Installation 🛠️

### 1. Install Required Packages (Desktop Mode)
```bash
sudo pacman -Syu tk python-pip python-pmw  # Ensure Tkinter is fully installed
```
# 2. Get the App
~~~
git clone https://github.com/yourusername/steam-deck-volume-lock.git
cd steam-deck-volume-lock
chmod +x volume_controller.py
~~~
# Usage 🎮

## Desktop Mode

~~~
python3 volume_controller.py
~~~

## Game Mode Setup

## 1. Open Steam in Desktop Mode

## 2. Add volume_controller.py as non-Steam game

## 3. In Properties:

Set Launch Options: python3 /path/to/volume_controller.py

Controller Layout: Gamepad with Mouse Trackpad

## Configuration ⚙️
Create Shortcuts
Desktop Shortcut (~/.local/share/applications/volume_lock.desktop):

~~~
[Desktop Entry]
Name=Volume Lock
Comment=Steam Deck Volume Limiter
Exec=python3 /home/deck/volume_controller.py
Icon=audio-volume-high
Terminal=false
Type=Application
Categories=Utility;
StartupWMClass=volume_controller.py
~~~
## Auto-Start (Optional)

~~~
# Create systemd service
echo "[Unit]
Description=Volume Lock Service
After=graphical.target

[Service]
ExecStart=python3 /home/deck/volume_controller.py
Restart=always
User=deck

[Install]
WantedBy=default.target" | sudo tee /etc/systemd/system/volume-lock.service

sudo systemctl enable volume-lock.service
sudo systemctl start volume-lock.service
~~~
## Troubleshooting 🔧
If volume doesn't stick:
~~~
sudo pacman -S pulseaudio-alsa  # Ensure audio control
chmod +x volume_controller.py
~~~

## Contributing 🤝

Fork the repository

Create your feature branch (git checkout -b feature/awesome-feature)

Commit changes (git commit -am 'Add awesome feature')

Push to branch (git push origin feature/awesome-feature)

Open a Pull Request

## License 📄
MIT License - See LICENSE for details.

## Made with ❤️ for the Steam Deck community
If this helped you, consider starring the repo! ⭐

MIT License

Copyright (c) 2023 xatusbetazx17

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



