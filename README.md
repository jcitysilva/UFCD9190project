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

<p>To execute <code>syms.py</code> or <code>pycracker.py</code>, ensure Python 3 is installed and the required dependencies are available. You can run the scripts directly or in a Python REPL environment.</p>

<h3>🛠️ Preparing the Scripts</h3>

<p>To make the scripts executable, set the correct file permissions:</p>

<pre>
<code>chmod 755 src/syms.py
chmod 755 src/pycracker.py</code>
</pre>

<p>After setting the permissions, you can run the scripts directly without needing to specify <code>python</code>:</p>

<pre>
<code>./src/syms.py [OPTIONS] [DIR_PATH]</code>
</pre>

---

<h3>🛠️ General Syntax for syms.py</h3>

<pre>
<code>src/syms.py [OPTIONS] [DIR_PATH]</code>
</pre>

<h3>Options</h3>
<ul>
  <li><code>-c, --content</code>: Search for files with identical binary content.</li>
  <li><code>-n, --name</code>: Search for files with the same name.</li>
  <li><code>-e, --extension</code>: Search for files with the same extension.</li>
  <li><code>-r PATTERN, --regex=PATTERN</code>: Search for files matching a regex pattern.</li>
</ul>
<p><code>DIR_PATH</code> is optional. If omitted, the current directory (<code>.</code>) is used.</p>

<p>If incorrect or missing options are provided, the script will display the usage instructions and exit gracefully.</p>

---

<h2>🔧 Example Commands for syms.py</h2>

<h3>1. Group Files by Name</h3>
<pre>
<code>./src/syms.py -n tests</code>
</pre>

<h3>2. Group Files by Extension</h3>
<pre>
<code>./src/syms.py -e tests</code>
</pre>

<h3>3. Search Using Regex</h3>
<p>To search for files with "test" or "Test" at the start of their name and a <code>.txt</code> extension:</p>
<pre>
<code>./src/syms.py -r '^(test|Test).*\.txt$' tests</code>
</pre>

<h3>4. Display Help</h3>
<p>To display usage instructions, simply run:</p>
<pre>
<code>./src/syms.py</code>
</pre>

---

<h2>💻 Running in a Python REPL</h2>

<p>You can also execute <code>syms.py</code> interactively in a Python REPL:</p>

<ol>
  <li>Open a terminal and start the REPL:
    <pre>
    <code>python3</code>
    </pre>
  </li>
  <li>Import <code>syms.py</code>:
    <pre>
    <code>from src.syms import main</code>
    </pre>
  </li>
  <li>Call the <code>main</code> function to parse arguments and execute the script:
    <pre>
    <code>main()</code>
    </pre>
  </li>
</ol>

---

<h2>📦 Requirements</h2>

<p>To run the scripts, it's recommended to set up a Python virtual environment to isolate dependencies. Follow these steps:</p>

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

<p>Alternatively, you can install all dependencies from the <code>requirements.txt</code> file (if provided):</p>

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
s