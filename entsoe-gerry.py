# %%
import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from dotenv import main

from entsoe import EntsoePandasClient

main.load_dotenv()

api_key = os.getenv("ENTSOEAPIKEY")
client = EntsoePandasClient(api_key=api_key)
start = pd.Timestamp("20230401", tz="Europe/Brussels")
end = pd.Timestamp("20230430", tz="Europe/Brussels")
country_code = "BE"  # Belgium
country_code_from = "FR"  # France
country_code_to = "DE_LU"  # Germany-Luxembourg
type_marketagreement_type = "A01"
contract_marketagreement_type = "A01"

# %%
df = client.query_wind_and_solar_forecast(
    country_code, start=start, end=end, psr_type=None
)


# %%
df.head()

# %%
df.describe()

# %%
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(15, 5))
plot = sns.lineplot(df)
plt.setp(plot.get_xticklabels(), rotation=90)

# %%
df.to_csv("outfile.csv")

# %%

# methods that return Pandas Series
client.query_day_ahead_prices(country_code, start=start, end=end)
client.query_net_position(country_code, start=start, end=end, dayahead=True)
client.query_crossborder_flows(country_code_from, country_code_to, start, end)
client.query_scheduled_exchanges(
    country_code_from, country_code_to, start, end, dayahead=False
)
client.query_net_transfer_capacity_dayahead(
    country_code_from, country_code_to, start, end
)
client.query_net_transfer_capacity_weekahead(
    country_code_from, country_code_to, start, end
)
client.query_net_transfer_capacity_monthahead(
    country_code_from, country_code_to, start, end
)
client.query_net_transfer_capacity_yearahead(
    country_code_from, country_code_to, start, end
)
client.query_intraday_offered_capacity(
    country_code_from, country_code_to, start, end, implicit=True
)
client.query_offered_capacity(
    country_code_from,
    country_code_to,
    start,
    end,
    contract_marketagreement_type,
    implicit=True,
)
client.query_aggregate_water_reservoirs_and_hydro_storage(country_code, start, end)

# %%

# methods that return Pandas DataFrames
client.query_load(country_code, start=start, end=end)
client.query_load_forecast(country_code, start=start, end=end)
client.query_load_and_forecast(country_code, start=start, end=end)
client.query_generation_forecast(country_code, start=start, end=end)
client.query_wind_and_solar_forecast(country_code, start=start, end=end, psr_type=None)
client.query_generation(country_code, start=start, end=end, psr_type=None)
client.query_generation_per_plant(country_code, start=start, end=end, psr_type=None)
client.query_installed_generation_capacity(
    country_code, start=start, end=end, psr_type=None
)
client.query_installed_generation_capacity_per_unit(
    country_code, start=start, end=end, psr_type=None
)
client.query_imbalance_prices(country_code, start=start, end=end, psr_type=None)
client.query_contracted_reserve_prices(
    country_code, start, end, type_marketagreement_type, psr_type=None
)
client.query_contracted_reserve_amount(
    country_code, start, end, type_marketagreement_type, psr_type=None
)
client.query_unavailability_of_generation_units(
    country_code,
    start=start,
    end=end,
    docstatus=None,
    periodstartupdate=None,
    periodendupdate=None,
)
client.query_unavailability_of_production_units(
    country_code,
    start,
    end,
    docstatus=None,
    periodstartupdate=None,
    periodendupdate=None,
)
client.query_unavailability_transmission(
    country_code_from,
    country_code_to,
    start,
    end,
    docstatus=None,
    periodstartupdate=None,
    periodendupdate=None,
)
client.query_withdrawn_unavailability_of_generation_units(country_code, start, end)
client.query_import(country_code, start, end)
client.query_generation_import(country_code, start, end)
client.query_procured_balancing_capacity(
    country_code, start, end, process_type, type_marketagreement_type=None
)
