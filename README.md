<h1>metalage</h1>
<p>
This is a GraphQL API for querying trace element data from Bronze and Iron Age artifacts, and ore sources from Earth.  The data is collected from peer-reviewed academic journals, the Oxford Archaeological Lead Isotope Database from the Isotrace Laboratory (OXALID), and the Mark Hill Laboratory's database on Old Copper Culture artifacts and North American ore sources.
</p>

<h3>Settup</h3>

<p>1) Clone the repo</p>
<pre>
https://github.com/jchiefelk/metalage.git
</pre>

<p>2) Change directory and setup virtualenv</p>
<pre>
cd metalage
python3 -m venv myenv
source myenv/bin/activate
</pre>

<p>3) Install dependencies</p>
<pre>
pip install -r requirements.txt
</pre>

<p>4) Run migrations</p>
<pre>
./manage.py makemigrations
</pre>

<p>5) Download trace element data from my dropbox account <a href="https://www.dropbox.com/s/vaj90we8el44jgb/metal_age_dump_2019_20190111.json?dl=0">https://www.dropbox.com/s/vaj90we8el44jgb/metal_age_dump_2019_20190111.json?dl=0</a></p>


<p>6) Install postgres on your machine and create metal_age.conf and save in root project directory</p>
<pre>
[database]
host=localhost
port=5432
user=postgres
password=
name=metal_age

[secret]
key=*4pz7m&#4-vlkwcy25z=_ns&svtju9r9^l8d&0mmmf80q(hco%
</pre>

<p>7) Import data into postgres by using runscripts in scripts folder</p>

<pre>
./manage.py runscripts import_element_trace_to_psql --script-args /dirname/csv_data_from_dropbox
</pre>

<p>8)Start server and go to http://localhost:8000/api/graphql to start making queries</p>
<pre>
./manage.py runserver
</pre>
