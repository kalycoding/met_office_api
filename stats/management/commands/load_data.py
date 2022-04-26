import contextlib
from django.core.management.base import BaseCommand
import pandas as pd
from stats.models import MaxTemp

class Command(BaseCommand):
    help = 'Load a txt file containing data info from met UK weather'
    
    def add_arguments(self, parser):
        parser.add_argument('-m', '--max', type=str, help='Load data to Max Temp table', required=True)
        parser.add_argument('-c', '--city', type=str, help='City of the data', required=True)
    
    def handle(self, *args, **kwargs):
        print("Articles Published in last 5 hours = ")
        print("Comments per Article in last 5 hours")
        t = kwargs['max']
        c = kwargs['city']
        format_data(t,c)
        
        

        
def format_data(data,city):
    df = pd.read_fwf(data)
    df = df.set_index('year')
    transpose_data = df.T
    columns = list(transpose_data.columns)
    for col in columns:
        print(transpose_data[col])
        with contextlib.suppress(Exception):
            MaxTemp.objects.create(
                year=col,
                data={
                    "jan":transpose_data[col]["jan"],
                    "feb":transpose_data[col]["feb"],
                    "mar":transpose_data[col]["mar"],
                    "apr":transpose_data[col]["apr"],
                    "amy":transpose_data[col]["may"],
                    "jun":transpose_data[col]["jun"],
                    "jul":transpose_data[col]["jul"],
                    "aug":transpose_data[col]["aug"],
                    "sep":transpose_data[col]["sep"],
                    "oct":transpose_data[col]["oct"],
                    "nov":transpose_data[col]["nov"],
                    "win":transpose_data[col]["win"],
                    "spr":transpose_data[col]["spr"],
                    "sum":transpose_data[col]["sum"],
                    "aut":transpose_data[col]["aut"],
                    "ann":transpose_data[col]["ann"],

                    },
                city=city
            )
        print("finished loading data to database")