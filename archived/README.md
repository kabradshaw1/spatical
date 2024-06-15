```bash
conda install ipython
```

### python basics
List: changeable, ordered, indexed
```python
mylist = ["apple", "banana", "cherry"]
```
Tuple: unchangeable, ordered, indexed
```python
myTuple = ("apple", "banana", "cherry")
```

Dictionary: used in store data in key:value pairs
```python
myDictionary = {"fruit_1": "apple"}
```

```bash
conda activate Kyle
```

```bash
ipython
```

```python
range()
```

The issue you're experiencing with Visual Studio Code (VS Code) is likely related to the Python interpreter configuration or the environment that VS Code is using. Here are the steps to ensure VS Code is using the correct Conda environment where `matplotlib` is installed:

### Step 1: Open VS Code

Launch Visual Studio Code.

### Step 2: Select the Correct Python Interpreter

1. **Open the Command Palette**:
   - You can open the Command Palette by pressing `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS).

2. **Search for "Python: Select Interpreter"**:
   - Type `Python: Select Interpreter` and select it from the dropdown.

3. **Choose the Correct Conda Environment**:
   - You should see a list of available Python interpreters. Look for the one that corresponds to your Conda environment where you installed `matplotlib`. It should look something like `/path/to/your/conda/env/bin/python`.

### Step 3: Verify the Environment in VS Code Terminal

1. **Open a Terminal in VS Code**:
   - You can open a terminal in VS Code by navigating to `Terminal > New Terminal` or pressing ``Ctrl+` ``.

2. **Check the Conda Environment**:
   - Ensure the terminal is using the correct Conda environment by running:

     ```bash
     conda activate your_environment_name
     ```

3. **Verify `matplotlib` Installation**:
   - In the terminal, try importing `matplotlib` to make sure it works:

     ```bash
     python -c "import matplotlib; print(matplotlib.__version__)"
     ```

### Step 4: Reload VS Code

Sometimes, VS Code needs to be reloaded for changes to take effect. You can reload the window by:

- Pressing `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS) to open the Command Palette.
- Typing `Reload Window` and selecting it from the dropdown.

### Step 5: Check Python Path in Settings

Ensure that the Python path in the VS Code settings is pointing to the correct Conda environment.

1. **Open Settings**:
   - Go to `File > Preferences > Settings` or press `Ctrl+,` (Windows/Linux) or `Cmd+,` (macOS).

2. **Search for "Python Path"**:
   - Type `python.pythonPath` in the search bar.

3. **Set the Python Path**:
   - Make sure the path is set to the Python executable within your Conda environment, for example: `/path/to/your/conda/env/bin/python`.

### Step 6: Ensure `pylance` is Installed

Make sure the `pylance` extension is installed and enabled in VS Code.

1. **Open Extensions View**:
   - Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS) to open the Extensions view.

2. **Search for `pylance`**:
   - Ensure the `Pylance` extension is installed and enabled.

### Example to Import `matplotlib`

Create a new Python file, for example `test_matplotlib.py`, and add the following code to test the import:

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```

### Summary

1. Ensure `matplotlib` is installed in your Conda environment.
2. Select the correct Python interpreter in VS Code.
3. Verify the environment in the VS Code terminal.
4. Reload VS Code.
5. Check the Python path in the settings.
6. Ensure `pylance` is installed and enabled.

These steps should resolve the issue and allow you to use `matplotlib` in VS Code without errors. If the problem persists, ensure that the Conda environment is correctly set up and that `matplotlib` is indeed installed in that environment.