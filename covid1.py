from os import listdir
from os.path import exists
import fnmatch
import sqlite3 as lite
import csv

data_source_dir = "/home/diego/programming/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports"
data_source_ext = "*.csv"
data_tracker = "/home/diego/programming/learning_python/lpthw/covid_data_tracker.txt"
covid_db_file = "/home/diego/programming/learning_python/covid19.db"

def list_data_files(source_dir, file_pattern):
    data_files = []

    for file in listdir(source_dir):
        if fnmatch.fnmatch(file, file_pattern):
            data_files.append(file)

    return data_files

def check_imported_data_files():
    list = []
    if exists(data_tracker):
        tracker = open(data_tracker).read()
        list = tracker.split("\n")

    return list

def track_imported_data():
    tracker = open(data_tracker, "a")
    for file in list_data_files(data_source_dir, data_source_ext):
        test = False
        for old in check_imported_data_files():
            if old == file:
                test = True
                break

        if test == False:
            load_data(data_source_dir+"/"+file)
            tracker.write(file)
            tracker.write("\n")

    tracker.close()

def load_data(file):
    print("Entering load_data")
    db_file_exist = exists(covid_db_file)
    print("DB File: ", db_file_exist)
    con = lite.connect(covid_db_file)

    with con:
        cur = con.cursor()
        if db_file_exist == False:
            cur.execute("CREATE TABLE daily(FIPS TEXT, Admin2 TEXT, Province_State TEXT, Country_Region TEXT, Last_Update TEXT, Lat REAL, Long_ REAL ,Confirmed INT, Deaths INT, Recovered INT, Active INT, Combined_Key TEXT, Incidence_Rate REAL, Case_Fatality_Ratio REAL)")

        with open(file) as csvDataFile:
            print(file)
            csvReader = csv.reader(csvDataFile,dialect="excel")
            i = 0
            for row in csvReader:
                print(len(row))
                if i == 0:
                    i += 1
                    continue
                qry = f'INSERT INTO daily VALUES("{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}", "{row[6]}", "{row[7]}", "{row[8]}", "{row[9]}", "{row[10]}", "{row[11]}", "{row[12]}", "{row[13]}")'
                print(qry)
                cur.execute(qry)
                i += 1


        con.commit()
#        con.close()

track_imported_data()
