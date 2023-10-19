import os
import pandas as pd
import spotipy 
import seaborn as sns
import matplotlib.pyplot as plt
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
load_dotenv()



client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

artist_data = 'spotify:artist:6fuALtryzj4cq7vkglKLxq'

app = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret))
results = app.artist_top_tracks(artist_data)

if results:
    tracks = results["tracks"][:10]
    tracks = [{k: (v/(1000*60))%60 if k == 
               "duration_ms" else v for k, 
               v in track.items() if k in 
               ["name", "popularity", "duration_ms"]} for track in tracks]

tracks_df = pd.DataFrame.from_records(tracks)
tracks_df.sort_values(["popularity"], ascending=False, inplace=True)
print(tracks_df.head(3))

scatter_plot = sns.scatterplot(data = tracks_df, x = "popularity", y = "duration_ms")
fig = scatter_plot.get_figure()
fig.savefig("scatter_plot.png")