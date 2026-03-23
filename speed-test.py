import speedtest #pip install speedtest-cli
#this library lets us measure internet speed directly from code
print("\n Running internet speed test...\n")
try:
    st = speedtest.Speedtest()
    st.get_best_server() #this method finds the best server based on ping
    print(f"Download: {st.download() / 1_000_000:.2f} Mbps")
    print(f"Upload:   {st.upload() / 1_000_000:.2f} Mbps")
    print(f"Ping:     {st.results.ping:.2f} ms")
except Exception as e:
    print(" Error:", e)