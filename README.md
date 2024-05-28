# Travel-Matcher
Match nearest accommodation to the nearest (airport/train/bus) station in case you don't know where to go in Europe.

## First step
- collect data from transporation sites (now only Ryanair)
    - in Ryanair_robust.py you can change the origin and destination airports and it creates a dataframe containing all prices from today until end of year (you can also change the start and end dates). Then in visualization.py, you can view the scatter plot of prices (make sure to change the filename in read CSV)
- collect data from accommodation sites

## Second step
- match and display top n best matches
