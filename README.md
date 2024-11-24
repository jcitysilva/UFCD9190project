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

<p>The script uses the <code>docopt</code> library to parse command-line arguments and <code>os.walk</code> to traverse directories.</p>

---

<h2>🚀 Usage Instructions</h2>

<p>To execute <code>syms.py</code>, ensure Python 3 is installed and the required dependencies are available. You can run the script directly or in a Python REPL environment.</p>

<h3>🛠️ General Syntax</h3>

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

---

<h2>🔧 Example Commands</h2>

<h3>1. Group Files by Name</h3>
<pre>
<code>src/syms.py -n tests</code>
</pre>

<h3>2. Group Files by Extension</h3>
<pre>
<code>src/syms.py -e tests</code>
</pre>

<h3>3. Search Using Regex</h3>
<p>To search for files with "test" or "Test" at the start of their name and a <code>.txt</code> extension:</p>
<pre>
<code>src/syms.py -r '^(test|Test).*\.txt$' tests</code>
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

<p>Ensure the following are installed:</p>
<ul>
  <li><b>Python 3.8+</b></li>
  <li><b>docopt</b> library:
    <pre>
    <code>pip install docopt</code>
    </pre>
  </li>
</ul>

---

<h2>📂 Future Work</h2>

<p>In addition to <code>syms.py</code>, the repository includes the <code>pycracker.py</code> utility, which is under development. This script aims to perform password cracking using dictionaries and hash comparisons.</p>

<p align="center">Stay tuned for updates!</p>

---

<p align="center">Made with ❤️ for UFCD 9190.</p>
