from sqlalchemy import create_engine, text
import os

my_secret = os.environ['DB_PASSWORD']

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
