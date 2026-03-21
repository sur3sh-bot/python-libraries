import speedtest 
print("\n Running internet speed test...\n")
try:
    st = speedtest.Speedtest()
    st.get_best_server()
    print(f"Download: {st.download() / 1_000_000:.2f} Mbps")
    print(f"Upload:   {st.upload() / 1_000_000:.2f} Mbps")
    print(f"Ping:     {st.results.ping:.2f} ms")
except Exception as e:
    print(" Error:", e)