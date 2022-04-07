from main import db, app , Job
import csv

db.create_all(app=app)

with open('./App/jobs.csv',newLine='') as f:
    jobs=csv.DictReader(f)

    for job in jobs:
        row=Job(name=job['name'], company=job['company'], email=job['email'], experience=job['experience'], details=job['details'])
    db.session.add(row)
db.session.commit()
