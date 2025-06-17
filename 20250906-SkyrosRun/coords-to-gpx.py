import xml.etree.ElementTree as ET

def create_gpx(coordinates, output_file="output.gpx"):
    """
    Creates a GPX file from a list of (latitude, longitude, elevation) tuples.

    Args:
        coordinates: List of tuples (lat, lon, ele)
        output_file: Output GPX filename
    """
    # GPX root element
    gpx = ET.Element("gpx",
                     version="1.1",
                     creator="CoordinateToGPX",
                     xmlns="http://www.topografix.com/GPX/1/1",
                     xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance",
                     xsi_schemaLocation="http://www.topografix.com/GPX/1/1 "
                                        "http://www.topografix.com/GPX/1/1/gpx.xsd")

    # Create a track element
    trk = ET.SubElement(gpx, "trk")
    ET.SubElement(trk, "name").text = "Generated Track"

    trkseg = ET.SubElement(trk, "trkseg")

    # Add track points with elevation
    for lat, lon, ele in coordinates:
        trkpt = ET.SubElement(trkseg, "trkpt", lat=str(lat), lon=str(lon))
        ET.SubElement(trkpt, "ele").text = str(ele)

    # Write to file
    tree = ET.ElementTree(gpx)
    ET.indent(tree, space="  ", level=0)  # Python 3.9+
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"GPX file written to '{output_file}'")

# Example usage
if __name__ == "__main__":
    from data import latlong, ele

    coords = [x+y for x,y in list(zip(latlong,[(x,) for x in ele]))]
    create_gpx(coords)
