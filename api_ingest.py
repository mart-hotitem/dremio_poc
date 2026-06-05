from dremioframe.client import DremioClient


client = DremioClient(
    hostname="https://830c66aa-62b3-4caa-9259-53efcfaa4104.dremio.eu01.onstackit.cloud",
    pat="vmFzAHpKTkayJLJo9RIBjz8SthyJ8xlDp8kR0E8DA9txeTjMug7pRlunGH+vYg==",
    #"eyJraWQiOiI2NmQ0MWVjZS0wNWFmLTQ4ZTUtOTZiNi1hOWUyYjcwMDg5MTkiLCJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiI1NThkN2QyNC1jZTAxLTRmZGMtYTg4MS02ZTA4OTNiOTY5NGEiLCJhdWQiOiI0MWE0ZmM3YS0xODE4LTRjNGYtYjg5Zi0wMjNhNDAxODIxZjgiLCJuYmYiOjE3Nzk4NzEwMTUsImlzcyI6ImRyZW1pbzovLzQxYTRmYzdhLTE4MTgtNGM0Zi1iODlmLTAyM2E0MDE4MjFmOCIsImV4cCI6MTc3OTg3NDYxNSwiaWF0IjoxNzc5ODcxMDE1LCJqdGkiOiI4MmE0NGZlNC0zYjFmLTQzMTAtYTFlYi1mOGU2ODE2ZGI5MzMifQ.TGOwnDSDugtjqJDEcSq_xuNgn1Vixo4qNIojSFQE7Lo-8NA3PwaZZjTk6A64mZ4g3bDZVPHzipYJzbuMfZk4IQ",
    #username="mdijk",
    #password="U6OF+Yg5}+Qh*Gy",
    tls=True,
    mode="v26",
    flight_port=32010
)

print(f"\nClient Configuration:")
print(f"  Mode: {client.mode}")
print(f"  Hostname: {client.hostname}")
print(f"  REST Port: {client.port}")
print(f"  Flight Port: {client.flight_port}")
print(f"  Base URL: {client.base_url}")
print(f"  Project ID: {client.project_id}")

try:    
    # Test catalog access
    catalog = client.catalog.list_catalog()
    print(f"✅ Connected successfully! Found {len(catalog)} catalog items.")
    
    # Test query execution (requires Arrow Flight)
    result = client.query("SELECT 1 as test")
    print(f"✅ Query execution successful!")
    print(result)
    
except Exception as e:
    print(f"❌ Connection failed: {e}")
    import traceback
    traceback.print_exc()

# df = client.query("""
#     select * from open_catalog_poc.raw.rdw_gekentekende_voertuigen limit 10
# """)

#print(df)