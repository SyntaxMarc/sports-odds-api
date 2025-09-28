import requests

BASE_URL = "http://localhost:8000"

def demo():
    print("Fetching MLB odds:")
    print(requests.get(f"{BASE_URL}/odds/mlb").json())

    print("\nFetching NBA odds:")
    print(requests.get(f"{BASE_URL}/odds/nba").json())

    print("\nFetching MLB players:")
    print(requests.get(f"{BASE_URL}/players/mlb").json()[:2])  # Only show first 2 for brevity

    print("\nFetching NBA players:")
    print(requests.get(f"{BASE_URL}/players/nba").json()[:2])

if __name__ == "__main__":
    demo()
