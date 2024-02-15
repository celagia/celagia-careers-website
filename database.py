from sqlalchemy import create_engine, text

dbConnectionString = "mysql+pymysql://d0jl1sxf0cqrjv845rlg:pscale_pw_r5ougDgSsGrgkvfDkrfkoXtMZd0RnIxXFpKutjvZDII@aws.connect.psdb.cloud/hikingcareers?charset=utf8mb4"

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
