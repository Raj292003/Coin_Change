import time, Coin_Change

def test(D,n):
    start_time=time.perf_counter()
    result=Coin_Change.cp(D,n)
    end_time=time.perf_counter()
    run_time=end_time-start_time
    print(result,run_time,sep="\n")
