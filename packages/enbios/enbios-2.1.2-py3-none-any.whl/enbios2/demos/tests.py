from random import choice
from enbios2.base.experiment import Experiment
import bw2data

from enbios2.bw2.util import report
from enbios2.models.experiment_models import ExperimentData, ExperimentActivityData

bw2data.projects.set_current("ecoinvent")
database_name = 'cutoff_3.9.1_default'
db = bw2data.Database(database_name)

wind_turbines_spain = db.search("electricity production, wind, 1-3MW turbine, onshore", filter={"location": "ES"})
print(wind_turbines_spain)


experiment_activities = []
for activity in wind_turbines_spain:
    experiment_activities.append(
        {"id":
            {
                "name": activity["name"],
                "location": activity["location"],
                "code": activity["code"]
            }
        }
    )


all_methods = list(bw2data.methods)
methods = [choice(all_methods) for _ in range(2)]
print(methods)

experiment_methods = [
    {
        "id": method
    }
    for method in methods
]


exp_data = ExperimentData(
    bw_project="ecoinvent",
    activities=experiment_activities,
    methods=experiment_methods
)

solar_spain = db.search("solar", filter={"location": "ES"})

sol_act = [
    {
        "id": {
            "name": activity["name"],
            "code": activity["code"]
        }
    }
    for activity in solar_spain[:2]
]

exp_data.activities.extend([ExperimentActivityData(**a) for a in sol_act])