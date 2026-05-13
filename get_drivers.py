import fastf1
import os

cache_path = "/__pycache__"
if not os.path.exists(cache_path):
  os.makedirs(cache_path)
fastf1.Cache.enable_cache(cache_path)

drivers = {}

# TODO: rewrite function to avoid the 500 calls/h limit

for year in range(2010, 2027):
  schedule = fastf1.get_event_schedule(year)
  for _, event in schedule.iterrows():
    if event.is_testing():
      continue
    try:
      session = fastf1.get_session(year, event['RoundNumber'], 'R')
      session.load()
      for driver_code in session.drivers:
        if driver_code not in drivers:
          car_data = session.car_data[driver_code]
          if not car_data.empty:
            number = car_data['DriverNumber'].iloc[0]
            driver_info = session.get_driver(driver_code)
            full_name = f"{driver_info['FirstName']} {driver_info['LastName']}"
            drivers[driver_code] = (full_name, number)
    except:
        pass

# sort by last name
sorted_drivers = sorted(drivers.items(), key=lambda x: x[1][0].split()[-1])

numbers = [num for _, (_, num) in sorted_drivers]
names = [name for _, (name, _) in sorted_drivers]