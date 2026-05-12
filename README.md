# MineScript Client

MineScript Client is a hack client built with MineScript and PyJinn.

## To Run Do ```\hack```

## Usage

Modules are stored inside `hacks.py`.

To enable or disable a module, press its keybind or change its value inside `inputs.py`.

Default keybinds:

* G → Aimbot
* V → Auto Hit
* C → Scaffold
* B → Hit Dir (make the opponent take kb to the right instead of left)
* R → Aim Assist

When a module is enabled, the client automatically runs its function from `hacks.py`.

Example module:

```python
def example():

    if not inputs.example_enabled:
        return

    print("enabled")
```

To create your own module:

1. Create a function in `hacks.py`
2. Add a toggle in `inputs.py`
3. Call the function in the main script

## Vulcan Detection

- G → Aimbot gets flagged by Vulcan
- V → Auto Hit usually does not get flagged by Vulcan
- C → Scaffold rarely gets flagged by Vulcan
- B → Hit Dir (makes opponents take knockback to the right instead of forwards) almost never gets flagged by Vulcan
- R → Aim Assist has not been flagged by Vulcan
