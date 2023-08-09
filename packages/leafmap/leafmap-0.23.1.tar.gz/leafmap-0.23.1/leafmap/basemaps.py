"""Module for basemaps. 

More WMS basemaps can be found at the following websites:

1. USGS National Map: https://viewer.nationalmap.gov/services

2. MRLC NLCD Land Cover data: https://www.mrlc.gov/data-services-page

3. FWS NWI Wetlands data: https://www.fws.gov/wetlands/Data/Web-Map-Services.html

"""
import collections
import os
import requests
import folium
import ipyleaflet
import xyzservices.providers as xyz
from .common import check_package, planet_tiles
from typing import Dict, Optional, List

# from box import Box

# Custom XYZ tile services.
xyz_tiles = {
    "OpenStreetMap": {
        "url": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        "attribution": "OpenStreetMap",
        "name": "OpenStreetMap",
    },
    "ROADMAP": {
        "url": "https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
        "attribution": "Google",
        "name": "Google Maps",
    },
    "SATELLITE": {
        "url": "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
        "attribution": "Google",
        "name": "Google Satellite",
    },
    "TERRAIN": {
        "url": "https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}",
        "attribution": "Google",
        "name": "Google Terrain",
    },
    "HYBRID": {
        "url": "https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
        "attribution": "Google",
        "name": "Google Hybrid",
    },
}

# Custom WMS tile services.
wms_tiles = {
    "FWS NWI Wetlands": {
        "url": "https://www.fws.gov/wetlands/arcgis/services/Wetlands/MapServer/WMSServer?",
        "layers": "1",
        "name": "FWS NWI Wetlands",
        "attribution": "FWS",
        "format": "image/png",
        "transparent": True,
    },
    "FWS NWI Wetlands Raster": {
        "url": "https://www.fws.gov/wetlands/arcgis/services/Wetlands_Raster/ImageServer/WMSServer?",
        "layers": "0",
        "name": "FWS NWI Wetlands Raster",
        "attribution": "FWS",
        "format": "image/png",
        "transparent": True,
    },
    "NLCD 2019 CONUS Land Cover": {
        "url": "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2019_Land_Cover_L48/wms?",
        "layers": "NLCD_2019_Land_Cover_L48",
        "name": "NLCD 2019 CONUS Land Cover",
        "attribution": "MRLC",
        "format": "image/png",
        "transparent": True,
    },
    "NLCD 2016 CONUS Land Cover": {
        "url": "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2016_Land_Cover_L48/wms?",
        "layers": "NLCD_2016_Land_Cover_L48",
        "name": "NLCD 2016 CONUS Land Cover",
        "attribution": "MRLC",
        "format": "image/png",
        "transparent": True,
    },
    "NLCD 2013 CONUS Land Cover": {
        "url": "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2013_Land_Cover_L48/wms?",
        "layers": "NLCD_2013_Land_Cover_L48",
        "name": "NLCD 2013 CONUS Land Cover",
        "attribution": "MRLC",
        "format": "image/png",
        "transparent": True,
    },
    "NLCD 2011 CONUS Land Cover": {
        "url": "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2011_Land_Cover_L48/wms?",
        "layers": "NLCD_2011_Land_Cover_L48",
        "name": "NLCD 2011 CONUS Land Cover",
        "attribution": "MRLC",
        "format": "image/png",
        "transparent": True,
    },
    "NLCD 2008 CONUS Land Cover": {
        "url": "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2008_Land_Cover_L48/wms?",
        "layers": "NLCD_2008_Land_Cover_L48",
        "name": "NLCD 2008 CONUS Land Cover",
        "attribution": "MRLC",
        "format": "image/png",
        "transparent": True,
    },
    "NLCD 2006 CONUS Land Cover": {
        "url": "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2006_Land_Cover_L48/wms?",
        "layers": "NLCD_2006_Land_Cover_L48",
        "name": "NLCD 2006 CONUS Land Cover",
        "attribution": "MRLC",
        "format": "image/png",
        "transparent": True,
    },
    "NLCD 2004 CONUS Land Cover": {
        "url": "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2004_Land_Cover_L48/wms?",
        "layers": "NLCD_2004_Land_Cover_L48",
        "name": "NLCD 2004 CONUS Land Cover",
        "attribution": "MRLC",
        "format": "image/png",
        "transparent": True,
    },
    "NLCD 2001 CONUS Land Cover": {
        "url": "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2001_Land_Cover_L48/wms?",
        "layers": "NLCD_2001_Land_Cover_L48",
        "name": "NLCD 2001 CONUS Land Cover",
        "attribution": "MRLC",
        "format": "image/png",
        "transparent": True,
    },
    "USGS NAIP Imagery": {
        "url": "https://imagery.nationalmap.gov/arcgis/services/USGSNAIPImagery/ImageServer/WMSServer?",
        "layers": "USGSNAIPImagery:NaturalColor",
        "name": "USGS NAIP Imagery",
        "attribution": "USGS",
        "format": "image/png",
        "transparent": True,
    },
    "USGS NAIP Imagery False Color": {
        "url": "https://imagery.nationalmap.gov/arcgis/services/USGSNAIPImagery/ImageServer/WMSServer?",
        "layers": "USGSNAIPImagery:FalseColorComposite",
        "name": "USGS NAIP Imagery False Color",
        "attribution": "USGS",
        "format": "image/png",
        "transparent": True,
    },
    "USGS NAIP Imagery NDVI": {
        "url": "https://imagery.nationalmap.gov/arcgis/services/USGSNAIPImagery/ImageServer/WMSServer?",
        "layers": "USGSNAIPImagery:NDVI_Color",
        "name": "USGS NAIP Imagery NDVI",
        "attribution": "USGS",
        "format": "image/png",
        "transparent": True,
    },
    "USGS Hydrography": {
        "url": "https://basemap.nationalmap.gov/arcgis/services/USGSHydroCached/MapServer/WMSServer?",
        "layers": "0",
        "name": "USGS Hydrography",
        "attribution": "USGS",
        "format": "image/png",
        "transparent": True,
    },
    "USGS 3DEP Elevation": {
        "url": "https://elevation.nationalmap.gov/arcgis/services/3DEPElevation/ImageServer/WMSServer?",
        "layers": "33DEPElevation:Hillshade Elevation Tinted",
        "name": "USGS 3DEP Elevation",
        "attribution": "USGS",
        "format": "image/png",
        "transparent": True,
    },
    "ESA WorldCover 2020": {
        "url": "https://services.terrascope.be/wms/v2",
        "layers": "WORLDCOVER_2020_MAP",
        "name": "ESA Worldcover 2020",
        "attribution": "ESA",
        "format": "image/png",
        "transparent": True,
    },
    "ESA WorldCover 2020 S2 FCC": {
        "url": "https://services.terrascope.be/wms/v2",
        "layers": "WORLDCOVER_2020_S2_FCC",
        "name": "ESA Worldcover 2020 S2 FCC",
        "attribution": "ESA",
        "format": "image/png",
        "transparent": True,
    },
    "ESA WorldCover 2020 S2 TCC": {
        "url": "https://services.terrascope.be/wms/v2",
        "layers": "WORLDCOVER_2020_S2_TCC",
        "name": "ESA Worldcover 2020 S2 TCC",
        "attribution": "ESA",
        "format": "image/png",
        "transparent": True,
    },
    "ESA WorldCover 2021": {
        "url": "https://services.terrascope.be/wms/v2",
        "layers": "WORLDCOVER_2021_MAP",
        "name": "ESA Worldcover 2021",
        "attribution": "ESA",
        "format": "image/png",
        "transparent": True,
    },
    "ESA WorldCover 2021 S2 FCC": {
        "url": "https://services.terrascope.be/wms/v2",
        "layers": "WORLDCOVER_2021_S2_FCC",
        "name": "ESA Worldcover 2021 S2 FCC",
        "attribution": "ESA",
        "format": "image/png",
        "transparent": True,
    },
    "ESA WorldCover 2021 S2 TCC": {
        "url": "https://services.terrascope.be/wms/v2",
        "layers": "WORLDCOVER_2021_S2_TCC",
        "name": "ESA Worldcover 2021 S2 TCC",
        "attribution": "ESA",
        "format": "image/png",
        "transparent": True,
    },
}


def _unpack_sub_parameters(var, param):
    temp = var
    for sub_param in param.split("."):
        temp = getattr(temp, sub_param)
    return temp


def get_xyz_dict(free_only: bool = True, france: bool = False) -> Dict:
    """Returns a dictionary of xyz services.

    Args:
        free_only (bool, optional): Whether to return only free xyz tile services that do not require an access token. Defaults to True.
        france (bool, optional): Whether include Geoportail France basemaps. Defaults to False.

    Returns:
        dict: A dictionary of xyz services.
    """

    xyz_dict_tmp = {}
    for item in xyz.values():
        try:
            name = item["name"]
            tile = _unpack_sub_parameters(xyz, name)
            if _unpack_sub_parameters(xyz, name).requires_token():
                if free_only:
                    pass
                else:
                    xyz_dict_tmp[name] = tile
            else:
                xyz_dict_tmp[name] = tile
            tile["type"] = "xyz"

        except Exception:
            for sub_item in item:
                name = item[sub_item]["name"]
                tile = _unpack_sub_parameters(xyz, name)
                if _unpack_sub_parameters(xyz, name).requires_token():
                    if free_only:
                        pass
                    else:
                        xyz_dict_tmp[name] = tile
                else:
                    xyz_dict_tmp[name] = tile
                tile["type"] = "xyz"

    xyz_dict = {}

    if france:
        xyz_dict = xyz_dict_tmp
    else:
        for key in xyz_dict_tmp:
            if "France" not in key:
                xyz_dict[key] = xyz_dict_tmp[key]

    xyz_dict = collections.OrderedDict(sorted(xyz_dict.items()))
    return xyz_dict


def xyz_to_leaflet() -> Dict:
    """Convert xyz tile services to ipyleaflet tile layers.

    Returns:
        dict: A dictionary of ipyleaflet tile layers.
    """
    leaflet_dict = {}

    for key in xyz_tiles:
        xyz_tiles[key]["type"] = "xyz"
        name = xyz_tiles[key]["name"]
        leaflet_dict[key] = xyz_tiles[key]

    for key in wms_tiles:
        wms_tiles[key]["type"] = "wms"
        name = wms_tiles[key]["name"]
        leaflet_dict[key] = wms_tiles[key]

    xyz_dict = get_xyz_dict()
    for item in xyz_dict:
        name = xyz_dict[item].name
        xyz_dict[item]["url"] = xyz_dict[item].build_url()
        leaflet_dict[name] = xyz_dict[item]

    return leaflet_dict


def xyz_to_pydeck() -> Dict:
    """Convert xyz tile services to pydeck custom tile layers.

    Returns:
        dict: A dictionary of pydeck tile layers.
    """

    check_package("pydeck", "https://deckgl.readthedocs.io/en/latest/installation.html")
    import pydeck as pdk

    pydeck_dict = {}

    for key in xyz_tiles:
        url = xyz_tiles[key]["url"]
        pydeck_dict[key] = url

    xyz_dict = get_xyz_dict()
    for item in xyz_dict:
        url = xyz_dict[item].build_url()
        pydeck_dict[item] = url

        if os.environ.get("PLANET_API_KEY") is not None:
            planet_dict = planet_tiles(tile_format="ipyleaflet")
            for tile in planet_dict:
                pydeck_dict[tile] = planet_dict[tile].url

    pdk.settings.custom_libraries = [
        {
            "libraryName": "MyTileLayerLibrary",
            "resourceUri": "https://cdn.jsdelivr.net/gh/giswqs/pydeck_myTileLayer@master/dist/bundle.js",
        }
    ]

    for key in pydeck_dict:
        pydeck_dict[key] = pdk.Layer("MyTileLayer", pydeck_dict[key], key)

    return pydeck_dict


def xyz_to_folium() -> Dict:
    """Convert xyz tile services to folium tile layers.

    Returns:
        dict: A dictionary of folium tile layers.
    """
    folium_dict = {}

    for key in xyz_tiles:
        name = xyz_tiles[key]["name"]
        url = xyz_tiles[key]["url"]
        attribution = xyz_tiles[key]["attribution"]
        folium_dict[key] = folium.TileLayer(
            tiles=url,
            attr=attribution,
            name=name,
            overlay=True,
            control=True,
            max_zoom=22,
        )

    for key in wms_tiles:
        name = wms_tiles[key]["name"]
        url = wms_tiles[key]["url"]
        layers = wms_tiles[key]["layers"]
        fmt = wms_tiles[key]["format"]
        transparent = wms_tiles[key]["transparent"]
        attribution = wms_tiles[key]["attribution"]
        folium_dict[key] = folium.WmsTileLayer(
            url=url,
            layers=layers,
            name=name,
            attr=attribution,
            fmt=fmt,
            transparent=transparent,
            overlay=True,
            control=True,
        )

    xyz_dict = get_xyz_dict()
    for item in xyz_dict:
        name = xyz_dict[item].name
        url = xyz_dict[item].build_url()
        attribution = xyz_dict[item].attribution
        if "max_zoom" in xyz_dict[item].keys():
            max_zoom = xyz_dict[item]["max_zoom"]
        else:
            max_zoom = 22
        folium_dict[name] = folium.TileLayer(
            tiles=url,
            attr=attribution,
            name=name,
            max_zoom=max_zoom,
            overlay=True,
            control=True,
        )

    if os.environ.get("PLANET_API_KEY") is not None:
        planet_dict = planet_tiles(tile_format="folium")
        folium_dict.update(planet_dict)

    return folium_dict


def xyz_to_heremap() -> Dict:
    """Convert xyz tile services to hermap tile layers.

    Returns:
        dict: A dictionary of heremap tile layers.
    """

    try:
        import here_map_widget
    except ImportError:
        raise ImportError(
            'This module requires the hermap package. Please install it using "pip install here-map-widget-for-jupyter".'
        )

    # Built-in heremap tile services.
    here_tiles = {
        "HERE_RASTER_NORMAL_MAP": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.raster.normal.map
        ),
        "HERE_RASTER_NORMAL_BASE": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.raster.normal.base
        ),
        "HERE_RASTER_NORMAL_BASE_NIGHT": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.raster.normal.basenight
        ),
        "HERE_RASTER_NORMAL_LABELS": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.raster.normal.labels
        ),
        "HERE_RASTER_NORMAL_TRANSIT": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.raster.normal.transit
        ),
        "HERE_RASTER_NORMAL_XBASE": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.raster.normal.xbase
        ),
        "HERE_RASTER_NORMAL_XBASE_NIGHT": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.raster.normal.xbasenight
        ),
        "HERE_RASTER_SATELLITE_MAP": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.raster.satellite.map
        ),
        "HERE_RASTER_SATELLITE_LABELS": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.raster.satellite.labels
        ),
        "HERE_RASTER_SATELLITE_BASE": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.raster.satellite.base
        ),
        "HERE_RASTER_SATELLITE_XBASE": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.raster.satellite.xbase
        ),
        "HERE_RASTER_TERRAIN_MAP": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.raster.terrain.map
        ),
        "HERE_RASTER_TERRAIN_LABELS": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.raster.terrain.labels
        ),
        "HERE_RASTER_TERRAIN_BASE": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.raster.terrain.base
        ),
        "HERE_RASTER_TERRAIN_XBASE": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.raster.terrain.xbase
        ),
        "HERE_VECTOR_NORMAL_MAP": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.vector.normal.map
        ),
        "HERE_VECTOR_NORMAL_TRUCK": here_map_widget.DefaultLayers(
            layer_name=here_map_widget.DefaultLayerNames.vector.normal.truck
        ),
    }

    heremap_dict = {}

    for key in xyz_tiles:
        name = xyz_tiles[key]["name"]
        url = xyz_tiles[key]["url"]
        attribution = xyz_tiles[key]["attribution"]
        heremap_dict[key] = here_map_widget.TileLayer(
            provider=here_map_widget.ImageTileProvider(
                url=url, attribution=attribution, name=name
            )
        )

    xyz_dict = get_xyz_dict()
    for item in xyz_dict:
        name = xyz_dict[item].name
        url = xyz_dict[item].build_url()
        attribution = xyz_dict[item].attribution
        if "max_zoom" in xyz_dict[item].keys():
            max_zoom = xyz_dict[item]["max_zoom"]
        else:
            max_zoom = 22
        heremap_dict[name] = here_map_widget.TileLayer(
            provider=here_map_widget.ImageTileProvider(
                url=url, attribution=attribution, name=name, max_zoom=max_zoom
            )
        )

    heremap_dict.update(here_tiles)

    return heremap_dict


def xyz_to_plotly() -> Dict:
    """Convert xyz tile services to plotly tile layers.

    Returns:
        dict: A dictionary of plotly tile layers.
    """
    plotly_dict = {}

    for key in xyz_tiles:
        url = xyz_tiles[key]["url"]
        attribution = xyz_tiles[key]["attribution"]
        plotly_dict[key] = {
            "below": "traces",
            "sourcetype": "raster",
            "sourceattribution": attribution,
            "source": [url],
            "name": key,
        }

    xyz_dict = get_xyz_dict()
    for item in xyz_dict:
        name = xyz_dict[item].name
        url = xyz_dict[item].build_url()
        attribution = xyz_dict[item].attribution

        plotly_dict[name] = {
            "below": "traces",
            "sourcetype": "raster",
            "sourceattribution": attribution,
            "source": [url],
            "name": name,
        }

    return plotly_dict


def xyz_to_bokeh() -> Dict:
    """Convert xyz tile services to bokeh tile layers.

    Returns:
        dict: A dictionary of bokeh tile layers.
    """
    from bokeh.models import WMTSTileSource

    bokeh_dict = {}

    for key in xyz_tiles:
        url = xyz_tiles[key]["url"]
        attribution = xyz_tiles[key]["attribution"]
        tile_options = {
            "url": url,
            "attribution": attribution,
        }
        bokeh_dict[key] = WMTSTileSource(**tile_options)

    xyz_dict = get_xyz_dict()
    for item in xyz_dict:
        url = xyz_dict[item].build_url()
        attribution = xyz_dict[item].attribution
        key = xyz_dict[item].name
        tile_options = {
            "url": url,
            "attribution": attribution,
        }
        bokeh_dict[key] = WMTSTileSource(**tile_options)

    return bokeh_dict


def search_qms(keywords, limit=10):
    """Search qms files for keywords. Reference: https://github.com/geopandas/xyzservices/issues/65

    Args:
        keywords (str): Keywords to search for.
        limit (int): Number of results to return.
    """
    QMS_API = "https://qms.nextgis.com/api/v1/geoservices"

    services = requests.get(
        f"{QMS_API}/?search={keywords}&type=tms&epsg=3857&limit={str(limit)}"
    )
    services = services.json()
    if services["count"] == 0:
        return None
    elif services["count"] <= limit:
        return services["results"]
    else:
        return services["results"][:limit]


def get_qms(service_id: str) -> Dict:
    QMS_API = "https://qms.nextgis.com/api/v1/geoservices"
    service_details = requests.get(f"{QMS_API}/{service_id}")
    return service_details.json()


def qms_to_leafmap(service_id: str) -> Dict:
    service_details = get_qms(service_id)
    name = service_details["name"]
    url = service_details["url"]
    attribution = service_details["copyright_text"]

    layer = ipyleaflet.TileLayer(url=url, name=name, attribution=attribution)
    return layer
