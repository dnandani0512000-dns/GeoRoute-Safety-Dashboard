# ==========================
# DAY 3: GEOSERVER PUBLISHING
# ==========================
pip install -U geoserver-restconfig
from geoserver.catalog import Catalog
import os
import requests
from requests.auth import HTTPBasicAuth
from geoserver.catalog import Catalog

# ==========================
# CONFIG
# ==========================
GEOSERVER_URL = "http://localhost:8080/geoserver/rest"
USERNAME = "admin"
PASSWORD = "geoserver"

WORKSPACE = "jojariproject"

RASTERS = {
    "pre_ndvi":  "data/results/pre_ndvi_clip.tif",
    "post_ndvi": "data/results/post_ndvi_clip.tif",
    "pre_ndwi":  "data/results/pre_ndwi_clip.tif",
    "post_ndwi": "data/results/post_ndwi_clip.tif",
}

# ==========================
# CONNECT
# ==========================
cat = Catalog(GEOSERVER_URL, USERNAME, PASSWORD)

# ==========================
# CREATE WORKSPACE
# ==========================
if not cat.get_workspace(WORKSPACE):
    cat.create_workspace(WORKSPACE, WORKSPACE)
    print("Workspace created:", WORKSPACE)
else:
    print("ℹ Workspace exists:", WORKSPACE)

# ==========================
# HELPER: PUBLISH VIA RAW REST
# ==========================
import requests
from requests.auth import HTTPBasicAuth

def publish_coverage_raw(workspace, store, layer_name):
    # Get native coverage name
    url_list = f"http://localhost:8080/geoserver/rest/workspaces/{workspace}/coveragestores/{store}/coverages.json"
    r = requests.get(url_list, auth=HTTPBasicAuth("admin", "geoserver"))
    r.raise_for_status()
    covs = r.json()["coverages"]["coverage"]
    native_name = covs[0]["name"]   # ← this is pre_ndvi_store
    print("Native coverage name:", native_name)

    # Publish using native name
    url_pub = f"http://localhost:8080/geoserver/rest/workspaces/{workspace}/coveragestores/{store}/coverages"
    headers = {"Content-Type": "application/xml"}
    xml = f"""
    <coverage>
        <name>{layer_name}</name>
        <nativeName>{native_name}</nativeName>
    </coverage>
    """
    r2 = requests.post(url_pub, data=xml.strip(), headers=headers, auth=HTTPBasicAuth("admin", "geoserver"))
    if r2.status_code not in (200, 201):
        print("Publish failed:", r2.status_code, r2.text)
        r2.raise_for_status()
    print("Layer published:", layer_name)

# ==========================
# UPLOAD STORES + PUBLISH LAYERS
# ==========================
for layer_name, raster_path in RASTERS.items():

    if not os.path.exists(raster_path):
        print("File not found:", raster_path)
        continue

    raster_path = os.path.abspath(raster_path)
    store_name = layer_name + "_store"

    # Create store (upload GeoTIFF)
    store = cat.get_store(store_name, WORKSPACE)
    if store is None:
        print("Uploading:", raster_path)
        store = cat.create_coveragestore(
            name=store_name,
            workspace=WORKSPACE,
            path=raster_path,
            upload_data=True
        )
        print("Store created:", store_name)
    else:
        print("Store exists:", store_name)

    # Publish layer if missing
    qualified_name = f"{WORKSPACE}:{layer_name}"
    layer = cat.get_layer(qualified_name)

    if layer is None:
        print("Publishing layer:", qualified_name)
        publish_coverage_raw(WORKSPACE, store_name, layer_name)
    else:
        print("Layer already exists:", qualified_name)

print("\nGeoServer pipeline finished successfully!")
