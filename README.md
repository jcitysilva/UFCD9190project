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
  <li><code>pycracker.py</code>: A password-cracking utility designed to work with files formatted like <code>/etc/shadow</code>.</li>
</ul>

<h3>Features of <code>syms.py</code>:</h3>
<ul>
  <li>Identify duplicate files by name.</li>
  <li>Group files by extension.</li>
  <li>Check for duplicate binary content (e.g., identical files).</li>
  <li>Use regex patterns to filter specific files.</li>
</ul>

<h3>Features of <code>pycracker.py</code>:</h3>
<ul>
  <li>Cracks password hashes using a dictionary file.</li>
  <li>Supports multiple hashing algorithms like SHA-512, SHA-256, MD5, and bcrypt.</li>
  <li>Validates account statuses, ignoring locked or invalid accounts.</li>
  <li>Verbose output for better debugging and analysis.</li>
</ul>

<p>
The scripts demonstrate real-world applications of Python for file and cybersecurity tasks. They include proper error handling, support for multiple hashing schemes, and the ability to adapt to various input file structures.
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
<code>./src/syms.py [OPTIONS] [DIR_PATH]
./src/pycracker.py [DICTIONARY] [PASSWORDS]</code>
</pre>

<p>Alternatively, you can run the scripts using Python:</p>
<pre>
<code>python src/syms.py
python src/pycracker.py</code>
</pre>

---

<h3>💡 Example Commands for <code>syms.py</code></h3>

<p>Here are some examples using the <code>tests</code> directory:</p>

<h4>1. Group Files by Name:</h4>
<pre>
<code>./src/syms.py -n tests</code>
</pre>

<h4>2. Group Files by Extension:</h4>
<pre>
<code>./src/syms.py -e tests</code>
</pre>

<h4>3. Group Files by Content:</h4>
<pre>
<code>./src/syms.py -c tests</code>
</pre>

<h4>4. Search Using Regex:</h4>
<p>Find all files in <code>tests</code> starting with "test" or "Test" and ending with <code>.txt</code>:</p>
<pre>
<code>./src/syms.py -r '^(test|Test).*\.txt$' tests</code>
</pre>

<h4>5. Display Help:</h4>
<pre>
<code>./src/syms.py --help</code>
</pre>

---

<h3>💡 Example Commands for <code>pycracker.py</code></h3>

<h4>1. Crack All Passwords:</h4>
<p>Run <code>pycracker.py</code> with a dictionary file and a shadow-like password file:</p>
<pre>
<code>python src/pycracker.py ../tests/dict.txt ../tests/shadow.txt</code>
</pre>
<p>Output:</p>
<pre>
<code>
[+]  jgalamba  : 'Lmxy20#a'        (SHA-512)
[+]  formando  : 'abc'            (SHA-256)
</code>
</pre>

<h4>2. Crack Passwords for a Specific User:</h4>
<p>Use the <code>-u</code> flag to target a specific user:</p>
<pre>
<code>python src/pycracker.py ../tests/dict.txt ../tests/shadow.txt -u jgalamba</code>
</pre>
<p>Output:</p>
<pre>
<code>
[+]  jgalamba  : 'Lmxy20#a'        (SHA-512)
</code>
</pre>

<h4>3. Enable Verbose Output:</h4>
<p>Use the <code>-v</code> flag to see additional debug information:</p>
<pre>
<code>python src/pycracker.py ../tests/dict.txt ../tests/shadow.txt -v</code>
</pre>
<p>Output:</p>
<pre>
<code>
[!] Skipping user root: Account status is BLOCKED
[+]  jgalamba  : 'Lmxy20#a'        (SHA-512)
</code>
</pre>

<h4>4. Display Help:</h4>
<pre>
<code>python src/pycracker.py --help</code>
</pre>

---

<h3>🌀 Virtual Environment Management</h3>

<p>This project uses a Python virtual environment for managing dependencies. Follow these steps:</p>

<h4>1. Create the Virtual Environment:</h4>
<pre>
<code>python3 -m venv .venv</code>
</pre>

<h4>2. Activate the Virtual Environment:</h4>

<p>To activate the environment, run:</p>

<h5>On macOS/Linux:</h5>
<pre>
<code>source .venv/bin/activate</code>
</pre>

<h5>On Windows:</h5>
<pre>
<code>.venv\Scripts\activate</code>
</pre>

<h4>3. Deactivate the Virtual Environment:</h4>
<p>To deactivate the environment:</p>
<pre>
<code>deactivate</code>
</pre>

<h4>4. Reactivate the Virtual Environment:</h4>
<p>If the terminal is closed, navigate to the project directory and activate it again using the commands above.</p>

---

<h3>⚠️ Troubleshooting</h3>

<p>If you encounter <code>zsh: permission denied: .venv/bin/activate</code>, follow these steps:</p>

<ol>
  <li>Check permissions:
    <pre>
    <code>chmod +x .venv/bin/activate</code>
    </pre>
  </li>
  <li>Reactivate the environment:
    <pre>
    <code>source .venv/bin/activate</code>
    </pre>
  </li>
  <li>If the issue persists, recreate the virtual environment:
    <pre>
    <code>
    rm -rf .venv
    python3 -m venv .venv
    source .venv/bin/activate
    </code>
    </pre>
  </li>
</ol>

---

<h2>📦 Requirements</h2>

<h3>1. Install Required Libraries</h3>

<p>After activating the virtual environment, install the dependencies:</p>

<pre>
<code>pip install docopt passlib cryptography</code>
</pre>

<p>To avoid conflicts, use the following command if needed:</p>
<pre>
<code>python3 -m pip install passlib</code>
</pre>

<h3>2. Use a requirements.txt File</h3>

<p>Alternatively, you can install all dependencies from the <code>requirements.txt</code> file:</p>

<pre>
<code>pip install -r requirements.txt</code>
</pre>

---

<h3>4. Recommended Development Tools</h3>

<p>To maintain code quality and ensure consistent formatting, the following tools are recommended:</p>

<ul>
  <li><b>Black</b>: A Python code formatter that enforces PEP 8 compliance.
    <pre>
    <code>pip install black</code>
    </pre>
  </li>
  <li><b>Flake8</b>: A Python linter for checking code style and potential errors.
    <pre>
    <code>pip install flake8</code>
    </pre>
  </li>
</ul>

<p>To apply Black and check linting, use the following commands:</p>

<pre>
<code>
# Format all files with Black
black .

# Check for linting issues with Flake8
flake8 .
</code>
</pre>

---

<h2>📂 Future Work</h2>

<p>In addition to <code>syms.py</code>, the repository includes the <code>pycracker.py</code> utility, which is currently under development. This script aims to perform password cracking using dictionaries and hash comparisons. Stay tuned for its progress!</p>

---

<h2>💻 Recommended Extensions</h2>

<p>For an optimized development experience in VS Code, we recommend the following extensions:</p>

<ul>
  <li><b>Python</b>: Provides IntelliSense, debugging, and tool integration. Install via:
    <pre><code>code --install-extension ms-python.python</code></pre>
  </li>
  <li><b>Pylance</b>: Adds enhanced IntelliSense and type-checking. Install via:
    <pre><code>code --install-extension ms-python.vscode-pylance</code></pre>
  </li>
</ul>

<p>Project-specific recommendations are included in the <code>.vscode/extensions.json</code> file.</p>

---

<p align="center">Made with ❤️ for UFCD 9190.</p>
