# MineScript Client

MineScript Client is a lightweight modular Minecraft client built using MineScript and PyJinn.

The project is designed to be simple to edit, easy to expand, and useful for learning how client-side Minecraft modules work.

---

# Features

* Aim Assist
* TriggerBot / Auto Hit
* Hit Direction manipulation
* Bridge Assist / Ninja Bridge
* Movement utilities
* Modular system
* Python-style scripting
* Easy feature creation

---

# Requirements

* MineScript
* PyJinn support
* Minecraft 1.21+

---

# How It Works

Each module is its own function.

Example:

```python
def aim_assist():
    pass
```

The main loop simply calls enabled modules repeatedly.

Example:

```python
aim_assist()
auto_hit()
scaffold()
```

This makes editing and creating modules extremely easy.

---

# Creating Modules

## 1. Create a function

```python
def example_module():

    if not inputs.example_enabled:
        return

    print("enabled")
```

---

## 2. Add a toggle

In `inputs.py`:

```python
example_enabled = False
```

---

## 3. Call the module

Inside your main loop:

```python
example_module()
```

---

# Keybind System

Most modules use booleans inside `inputs.py`.

Example:

```python
aim_assist_enabled = True
scaffold_enabled = False
```

You can connect these to your own GUI or keybind handler.

---

# Example Module

```python
def auto_jump():

    if not inputs.auto_jump_enabled:
        return

    if mc.player.onGround():

        mc.player.jumpFromGround()
```

---

# Design Goals

MineScript Client focuses on:

* simplicity
* modularity
* fast testing
* learning
* customization

The codebase is intentionally easy to modify.

---

# Notes

Some advanced features may require:

* packet handling
* JavaClass access
* MineScript internals
* PyJinn integration
