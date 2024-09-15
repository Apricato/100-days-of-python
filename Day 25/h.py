import pandas as pd

data = {
  "Duration": [50, 40, None, None, 90, 20],
  "Pulse": [109, 140, 110, 125, 138, 170]
}

df = pd.DataFrame(data)

print(df.count())
