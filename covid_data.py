import json
import pandas as pd
import matplotlib.pyplot as plt



fig, (a, b) = plt.subplots(1, 2, figsize=(13, 5))
data[["Total Confirmed Cases", "Active Cases", "Total Recovered", "Total Deaths"]].plot(ax=a, title="Cumulative")
b.bar(data.index, data["Daily Confirmed Cases"])
b.set_title("Daily new cases")
fig.autofmt_xdate() # this here will tilts the date labels so they don’t overlap.
plt.savefig("covid_data.png")# here i saved the graph as a png file in the current directory.