credit: https://github.com/tomasrasymas/geo-heatmap

Based on tomasrasymas's geo-heatmap project. Modified to ingest WiGLE CSV files and generate WiFi heatmaps based on GPS
coordinates and signal strength (RSSI).

## Install
```bash
pipx install git+https://github.com/stealthlabs-io/wiglecsv-to-heatmap.git
```

## Usage
```bash
wigle-heatmap -c kismet.wiglecsv -s ssid,to,filter -o client.html
```

## Options

- `-c, --csv`: Path to WiGLE CSV file
- `-s, --ssid`: Comma-separated list of SSIDs to filter
- `-o, --output`: Output HTML file path

