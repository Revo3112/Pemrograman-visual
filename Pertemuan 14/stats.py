import pandas as pd

def stats_columns(filename, xlabel, ylabel):
    df = pd.read_csv(filename)
    xstats = df[xlabel].describe()
    ystats = df[ylabel].describe()

    return xstats, ystats

if __name__ == "__main__":
    xstats, ystats = stats_columns('tempRainYearly.csv', 'Temp', 'Rain')
    print(xstats)
    print(ystats)