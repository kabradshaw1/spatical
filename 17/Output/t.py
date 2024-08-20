import geopandas as gpd
from multiprocessing import Process
import time
def f(df, i):
    df.to_csv("test%d.csv"%i)
    print("done")

def main():
    df = gpd.read_file("education_board_district.gpkg")

    for i in range(10):
        print(i)
        p=Process(target=f, args=(df, i,))
        p.start()
        #p.join()

if __name__=="__main__":
    main()
