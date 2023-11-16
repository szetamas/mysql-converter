<h1>mysql-converter</h1>
<p>a python app for converting mysql database tables into CSV files</p>
<h3>for this app you need:</h3>
<p><code>pip install mysql-connector-python</code><br>
<code>pip install wxPython</code></p>
<p>You could use app with these command from root in win:<br>
<code>python.exe .\src\main.py</code><br>
<code>python.exe .\src\main.py -dbname=test</code><br>
<code>python.exe .\src\main.py -dbname=test -sizex=900</code><br>
<code>python.exe .\src\main.py -size_x=900 -sizey=500 -dbname=test</code><br>
in linux:<br>
<code>python3 ./src/main.py</code><br>
<code>python3 ./src/main.py -dbname=test</code><br>
<code>python3 ./src/main.py -dbname=test -sizex=900</code><br>
<code>python3 ./src/main.py -size_x=900 -sizey=500 -dbname=test</code><br></p>
<h2>You could find mysql server settings in src/config.py</h2>
and you could modify the databasename with commandline argument:<br>
<code>-dbname=example</code><br>
You could modify the windowsize x and y with:<br>
<code>-sizex=200</code><br>
<code>-size_x=600</code><br>
<code>-sizey=300</code><br>
<code>-size_y=800</code><br>
(If you have too much tables or have to long similar names of tables)</p>
<h3>Todos:</h3>
<ul>
    <li>more error handling with messageboxes</li>
    <li>scrollbar if db has real lot table</li>
    <li>check that the csv already exists</li>
</ul>
