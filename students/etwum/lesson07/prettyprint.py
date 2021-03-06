import pprint
from create_personjobdept import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
database = SqliteDatabase('personjobdept.db')


def print_data():

    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')
    logger.info("get data")

    data = (Job.select(Job.job_name, Job.salary, Job.start_date))
    for x in data:

        pprint.pprint(x.job_name)
        pprint.pprint(x.salary)
        pprint.pprint(x.start_date)

    database.close()


print_data()