import MySQLdb as mdb
import sys
from geopy.geocoders import Nominatim

db = None

try:

    db = mdb.connect("localhost","root", "root", "your_database")

    cur = db.cursor()
    cur.execute("SELECT * FROM your_table")
    rows = cur.fetchall()
    for row in rows:
    	geolocator = Nominatim()
        print row

except mdb.Error, e:

    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)