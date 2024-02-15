from sqlalchemy import create_engine, text
import os

my_secret = os.environ.get('DB_PASSWORD')

dbConnectionString = "mysql+pymysql://eo4ymj8ct317cjcw98bx:" + my_secret + "@aws.connect.psdb.cloud/hikingcareers?charset=utf8mb4"

engine = create_engine(dbConnectionString,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs where id = {id}"))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0]._mapping)
