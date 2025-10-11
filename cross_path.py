import pandas as pd
from sklearn.neighbors import BallTree
import numpy as np

EARTH_RADIUS = 6371000

data = [
    # === GROUP 1: Morning rush hour at central square ===
    # 4 users crossing paths simultaneously (u1, u2, u3, u4)
    {'uid': 'u1', 'lat': 23.780600, 'lon': 90.279400, 'timestamp': '2025-10-10T08:30:00'},
    {'uid': 'u2', 'lat': 23.780605, 'lon': 90.279395, 'timestamp': '2025-10-10T08:30:15'},
    {'uid': 'u3', 'lat': 23.780595, 'lon': 90.279405, 'timestamp': '2025-10-10T08:30:30'},
    {'uid': 'u4', 'lat': 23.780602, 'lon': 90.279398, 'timestamp': '2025-10-10T08:30:45'},
    
    # === GROUP 2: Coffee shop meetup ===
    # u5 meets u6, then u7 joins
    {'uid': 'u5', 'lat': 23.781200, 'lon': 90.280100, 'timestamp': '2025-10-10T09:15:00'},
    {'uid': 'u6', 'lat': 23.781205, 'lon': 90.280105, 'timestamp': '2025-10-10T09:15:20'},
    {'uid': 'u7', 'lat': 23.781195, 'lon': 90.280095, 'timestamp': '2025-10-10T09:16:00'},
    
    # === GROUP 3: Bus stop encounter ===
    # u8 and u9 waiting for bus
    {'uid': 'u8', 'lat': 23.782000, 'lon': 90.281500, 'timestamp': '2025-10-10T10:00:00'},
    {'uid': 'u9', 'lat': 23.782003, 'lon': 90.281503, 'timestamp': '2025-10-10T10:00:30'},
    
    # === GROUP 4: Park walking paths ===
    # u10 crosses u1's path from earlier
    {'uid': 'u10', 'lat': 23.780610, 'lon': 90.279410, 'timestamp': '2025-10-10T08:32:00'},
    
    # === GROUP 5: Office building entrance ===
    # u2 meets u8 later in the day
    {'uid': 'u2', 'lat': 23.783000, 'lon': 90.282000, 'timestamp': '2025-10-10T12:00:00'},
    {'uid': 'u8', 'lat': 23.783005, 'lon': 90.282005, 'timestamp': '2025-10-10T12:00:10'},
    
    # === GROUP 6: Lunch time restaurant ===
    # u3, u4, u5 gathering for lunch
    {'uid': 'u3', 'lat': 23.784000, 'lon': 90.283000, 'timestamp': '2025-10-10T13:00:00'},
    {'uid': 'u4', 'lat': 23.784002, 'lon': 90.283002, 'timestamp': '2025-10-10T13:00:15'},
    {'uid': 'u5', 'lat': 23.783998, 'lon': 90.282998, 'timestamp': '2025-10-10T13:00:30'},
    
    # === GROUP 7: Evening gym session ===
    # u6 and u7 workout partners
    {'uid': 'u6', 'lat': 23.785000, 'lon': 90.284000, 'timestamp': '2025-10-10T18:00:00'},
    {'uid': 'u7', 'lat': 23.785001, 'lon': 90.284001, 'timestamp': '2025-10-10T18:00:05'},
    
    # === GROUP 8: Shopping mall ===
    # u9 and u10 coincidentally shopping
    {'uid': 'u9', 'lat': 23.786000, 'lon': 90.285000, 'timestamp': '2025-10-10T15:30:00'},
    {'uid': 'u10', 'lat': 23.786005, 'lon': 90.285005, 'timestamp': '2025-10-10T15:30:25'},
    
    # === GROUP 9: Train station platform ===
    # Multiple users waiting for train
    {'uid': 'u1', 'lat': 23.787000, 'lon': 90.286000, 'timestamp': '2025-10-10T17:45:00'},
    {'uid': 'u3', 'lat': 23.787002, 'lon': 90.286002, 'timestamp': '2025-10-10T17:45:10'},
    {'uid': 'u6', 'lat': 23.786998, 'lon': 90.285998, 'timestamp': '2025-10-10T17:45:20'},
    
    # === GROUP 10: Final evening crossing ===
    # u2 and u10 last crossing of the day
    {'uid': 'u2', 'lat': 23.788000, 'lon': 90.287000, 'timestamp': '2025-10-10T20:00:00'},
    {'uid': 'u10', 'lat': 23.788003, 'lon': 90.287003, 'timestamp': '2025-10-10T20:00:08'},
]

df = pd.DataFrame(data)

df['timestamp'] = pd.to_datetime(df['timestamp']).astype('int64') // 10**9

def find_crosspaths(df, distance_m=50, time_window_s=300):

    coords = np.radians(df[['lat','lon']])

    tree = BallTree(coords,metric="haversine")

    results = []
    radius = distance_m / EARTH_RADIUS

    for i , row in df.iterrows():
        uid_i , time_i = row['uid'], row['timestamp']

        indices = tree.query_radius([coords.values[i]], r=radius)[0]

        for j in indices:
            
            if i == j:
                continue
            
            uid_j, time_j = df.loc[j,'uid'], df.loc[j,'timestamp']
            
            if uid_j == uid_i:
                continue
            
            time_diff = abs(time_i - time_j)
          
            if time_diff <= time_window_s:
                results.append({
                    'user_a': uid_i,
                    'user_b': uid_j,
                    'time_diff_s': time_diff
                }) 
    return pd.DataFrame(results).drop_duplicates()


crosspaths = find_crosspaths(df, distance_m=30, time_window_s=300)
print(crosspaths)