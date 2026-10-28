# Topographic-Dynamic

Dynamic topographic wallpaper generator using Python.  
This program creates a real-time animated topographic contour display.

## Preview
The animation shows white contour lines on a black background, with smooth circular wave patterns that continuously evolve.

## Features
- Real-time animation (≈60 FPS target)
- Dynamic topographic patterns based on mathematical functions
- Lightweight and easy to run

## How It Works
The program builds a 2D grid using NumPy, then computes height values (Z) from
warped coordinates and several moving wave functions.

Core concepts:
- Uses sine and cosine functions
- Computes Euclidean distance
- Combines multiple wave layers for complex patterns

The result is rendered using Matplotlib contour plots.

## Requirements
Install the following dependencies:

```bash
pip install matplotlib numpy
```

The animation continues until its window is closed.

## Running as an app without a console window

Open the [`app`](./app) folder and double-click
[`Topographic Dynamic.vbs`](./app/Topographic%20Dynamic.vbs). It uses the virtual
environment at `Documents\Program buatan\.venv` and starts the animation with
`pythonw.exe`, so no terminal window remains open.

To see error messages while troubleshooting, run the script from a terminal:

```powershell
& "$env:USERPROFILE\Documents\Program buatan\.venv\Scripts\python.exe" .\topographic.py
```
