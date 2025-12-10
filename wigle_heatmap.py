import folium
from folium.plugins import HeatMap
import pandas as pd
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument('-c', '--csv', dest='csv', type=str, required=False,
                        help='Path to CSV data file', default='heatmap.csv')
    parser.add_argument('-s', '--ssid', dest='ssid', type=str, required=False,
                        help='List of in scope SSID', default='')
    parser.add_argument('-o', '--output', dest='output', type=str, required=False,
                        help='Path of html geographical heatmap', default='geo_heatmap.html')
    map_zoom_start = 17
    heatmap_radius = 25
    heatmap_blur = 15
    heatmap_min_opacity = 0.5
    heatmap_max_zoom = 20

    args = parser.parse_args()

    print('*' * 50)
    for i in vars(args):
        print(str(i) + ' - ' + str(getattr(args, i)))

    print('*' * 50)

    try:

        ssid_set = set(args.ssid.split(',')) if args.ssid else set()
        for_map = pd.read_csv(args.csv, sep=',', skiprows=1)
        if ssid_set:
            for_map = for_map[for_map['SSID'].isin(ssid_set)]
        else:
            for_map = for_map
        for_map = for_map.dropna(subset=['CurrentLatitude', 'CurrentLongitude'])
        center_lat = for_map['CurrentLatitude'].mean()
        center_lon = for_map['CurrentLongitude'].mean()
        location = [center_lat, center_lon]
        hmap = folium.Map(location=location,
                          zoom_start=map_zoom_start,
                          tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                          attr='Esri')

        hmap_data = [[row['CurrentLatitude'], row['CurrentLongitude'], max(0, (100 + row['RSSI']) * 2)] for index, row
                     in
                     for_map.iterrows()]

        hm = folium.plugins.HeatMap(hmap_data,
                                    min_opacity=heatmap_min_opacity,
                                    radius=heatmap_radius,
                                    blur=heatmap_blur,
                                    max_zoom=heatmap_max_zoom,
                                    gradient={
                                        0.0: 'blue',
                                        0.3: 'cyan',
                                        0.5: 'lime',
                                        0.7: 'yellow',
                                        1.0: 'red'
                                    }
                                    )

        hmap.add_child(hm)

        hmap.save(args.output)

        print('Output: %s' % args.output)
    except:
        import traceback

        print('Error occurred!')
        print(traceback.format_exc())


if __name__ == '__main__':
    main()
