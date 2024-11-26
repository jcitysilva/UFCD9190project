<h1 align="center">UFCD 9190: Syms Utility & PyCracker</h1>

<p align="center">
  <i>A project for UFCD 9190: Introduction to Programming Applied to Cybersecurity</i>
</p>

---

<h2>📄 Overview</h2>

<p>
This project is part of UFCD 9190: <i>Introduction to Programming Applied to Cybersecurity</i>. It includes two main utilities:
</p>

<ul>
  <li><code>syms.py</code>: A script to identify and group duplicate files in a directory based on specific criteria.</li>
  <li><code>pycracker.py</code>: A password-cracking utility currently under development.</li>
</ul>

<p>
The <code>syms.py</code> script helps identify duplicates by:
</p>

<ul>
  <li>File names</li>
  <li>File extensions</li>
  <li>Binary content</li>
  <li>Regex patterns</li>
</ul>

<p>
The script uses the <code>docopt</code> library to parse command-line arguments, <code>os.walk</code> to traverse directories, and implements validation steps to ensure correct usage. The inclusion of <code>sys.argv[0]</code> dynamically adjusts the displayed usage instructions based on the script name or path.
</p>

---

<h2>🚀 Usage Instructions</h2>

<h3>🛠️ Preparing the Scripts</h3>

<p>To make the scripts executable, set the correct file permissions:</p>

<pre>
<code>chmod 755 src/syms.py
chmod 755 src/pycracker.py</code>
</pre>

<p>After setting the permissions, you can run the scripts directly:</p>

<pre>
<code>./src/syms.py [OPTIONS] [DIR_PATH]</code>
</pre>

<p>Alternatively, you can run the scripts using Python:</p>
<pre>
<code>python src/syms.py</code>
</pre>

---

<h3>⚠️ Note for Windows Users</h3>

<p>This project is optimized for macOS and Linux systems. Windows users can use one of the following methods to run the scripts:</p>

<ul>
  <li><b>WSL (Windows Subsystem for Linux)</b>: Install WSL and run the scripts in a Linux-like environment. Learn more: <a href="https://learn.microsoft.com/en-us/windows/wsl/install">WSL Installation Guide</a>.</li>
  <li><b>Git Bash</b>: Use Git Bash, which provides a Unix-like terminal and supports commands such as <code>chmod</code>.</li>
  <li>Run the scripts directly using <code>python</code>:
    <pre>
    <code>python src/syms.py</code>
    </pre>
  </li>
</ul>

---

<h2>📦 Requirements</h2>

<h3>1. Create and Activate a Virtual Environment</h3>

<pre>
<code>
# Create the virtual environment
python3 -m venv .env

# Activate the virtual environment
# On Linux/macOS:
source .env/bin/activate
# On Windows:
.env\Scripts\activate
</code>
</pre>

<h3>2. Install Required Libraries</h3>

<p>Once the virtual environment is activated, install the dependencies:</p>

<pre>
<code>
pip install docopt passlib cryptography
</code>
</pre>

<h3>3. Use a requirements.txt File</h3>

<p>Alternatively, you can install all dependencies from the <code>requirements.txt</code> file:</p>

<pre>
<code>
pip install -r requirements.txt
</code>
</pre>

---

<h3>Note:</h3>
<p>The <code>.env</code> folder is excluded from the repository using a <code>.gitignore</code> file, as it is specific to each user’s environment. Ensure your virtual environment is activated before running the scripts.</p>

---

<h2>📂 Future Work</h2>

<p>In addition to <code>syms.py</code>, the repository includes the <code>pycracker.py</code> utility, which is currently under development. This script aims to perform password cracking using dictionaries and hash comparisons. Stay tuned for its progress!</p>

---

<p align="center">Made with ❤️ for UFCD 9190.</p>
