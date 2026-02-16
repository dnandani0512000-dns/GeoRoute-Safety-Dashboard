eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI4NzU3NzMzYi02YzdhLTRkMTItYjM2NS1iYzE0ZWJkNDA2MzEiLCJpZCI6Mzg3Mjk4LCJpYXQiOjE3NzAyNzkxNDZ9.FrAOqmeY-jMTgzkXrtQPpoPEE5yGkOnSkYSSChmpn94

http://localhost:8000/index.html

Week 1 Day 1 – Infrastructure Setup

Objective:-

Set up the geospatial environment and verify terrain rendering.

Tasks Completed:-

Installed docker desktop
2. Deployed GeoServer via Docker
3. Enabled CORS in GeoServer
4. Registered on cesium ion uploaded the elevation GeoTIFF on ion my assets
4. Initialize CesiumJS Project (Basic Globe)

>>>Create a folder example; D:\cesium_day1 
>>>inside the folder create one file example; index.html 
>>> Download cesium and keep the extracted file name Cesium(containing all the libraries) in the D:\cesium_day1 folder
>>> put the globe code in the .html file (The code must contain Asset id and token number from cesium ion)
>>> Download python 
>>> Open powershell of D:\cesium_day1 
>>> Run python --version
>>> Run cd D:\GIS_WEEK_2_3\cesiumday_1
python -m http.server 8000
>>> http://localhost:8000/index.html

Hosted sample DEM GeoTIFF on GeoServer
WMS → OpenLayers preview of Jodhpur DEM
WCS → GeoServer WCS GetCapabilities / coverage

.............................................................................
.............................................................................

Week 1 Day 2 - Sentinel-2 Automation (Python) in Jupyter Notebook

Objective:-

Automate satellite imagery download and index generation.

Tasks Completed:-

Connected to Copernicus Open Access Hub

2. Queried cloud-free Sentinel-2 imagery

3. Downloaded required bands (Red, Green, NIR)

4. Computed NDVI and NDWI

5. Reprojected to EPSG:3857

......................................................................
......................................................................

Week 1 Day 3 – Automated Publishing to GeoServer

Objective:-

Automate layer publishing.

Tasks Completed:-

Integrated GeoServer REST API

pip install -U geoserver-restconfig
from geoserver.catalog import Catalog

2. Created Workspace

3. Created Coverage Store

4. Published NDVI & NDWI layers

5. Removed manual UI dependency

Running pipeline.py automatically updates GeoServer layers

......................................................................
......................................................................

Week 1 Day 4 - Frontend Integration (CesiumJS)

Objective:-

Display NDVI & NDWI layers on 3D globe.

Tasks Completed:-

Integrated the data on 3Dglobe through asset id and token on cesium ion

Geoserver → GeoTIFF → Cesuim ion → Asset ID + Token → CesiumJS

Implemented:

NDVI toggle

2. NDWI toggle

3. Opacity slider

Deliverable
Analytical layers overlayed on terrain

......................................................................
......................................................................

Week 1 Day 5 – Full Pipeline Testing

Objective:-

Validate end-to-end system.

Tasks Completed:-

Tested full ETL flow:
Download → Process → Publish → Visualize

2. Verified terrain alignment

3. Optimized imagery loading

Deliverable
Fully functional data pipeline

........................................................................
........................................................................

Week 2 Day 1 – Route Drawing Tool

Objective

Enable user route plotting on terrain.

Tasks Completed

Implemented polyline drawing

Used ScreenSpaceEventHandler to capture mouse clicks.

Used viewer.scene.pickPosition() to get terrain coordinates.

Enabled clampToGround property Enabled terrain adherence

Exports as route.geojson

........................................................................
........................................................................

Week 2 Day 2 - Elevation Profiling

Objectives
Terrain Sampling
Used Cesium’s terrain API
Cesium.sampleTerrainMostDetailed()

Converted route Cartesian positions to Cartographic coordinates.

Sampled terrain heights using the active terrain provider.

Retrieved accurate elevation values for each route point.

2. Distance calculation 
Cesium.Cartesian3.distance()

Cumulative distance computed in kilometers for X-axis plotting


3. Elevation Chart Rendering

Integrated Chart.js to render a 2D line chart

Chart Features:

X-axis: Distance (km)

Y-axis: Elevation (m)

Smooth curve rendering

Auto-update when route is completed

4. Trigger Mechanism

Elevation profile generation is triggered when Stop Route button is clicked. This ensures the chart updates only after route completion.


Deliverable

Terrain elevation sampling along route
Cumulative distance computation
Dynamic 2D elevation profile chart
Automatic chart update on route completion

....................................................................................................................................................................

Week 2 Day 3 - Water/Obstacle Check 

Implement logic to detect whether a user-drawn route intersects a water body using the NDWI imagery layer.

If water is detected:
Trigger a UI alert
Change route color to RED

If safe:
Keep route color CYAN


Route Completion Trigger

Water detection runs automatically when:
Stop Route button is clicked
await checkWaterIntersection();

2. NDWI Sampling Logic (Client-Side Pixel Sampling)

For each route point:
Convert Cartesian → Cartographic
Get tile coordinates using:
tilingScheme.positionToTileXY()

Request tile image:
imageryProvider.requestImage()


Extract pixel color using:
getImageData()

3. Water Detection Rule

Water is identified using strong blue dominance. This logic detects pixels with high water reflectance (NDWI visualization).
if (b > 120 && b > r + 15 && b > g + 15)

....................................................................................................................................................................

Week 2 Day 4 - Dashboard Finalization 

Objective

Refine the application UI/UX, modularize logic, and prepare a polished MVP (Minimum Viable Product) for demonstration.

UI/UX Improvements (Dashboard Consolidation)

All controls were merged into a single left sidebar panel.

 Sidebar Sections

Layers Control

NDVI Toggle

NDWI Toggle

Opacity Slider

Route Tools

Start Route

Stop & Analyze

Clear Route

Export GeoJSON

Route Status Indicator

SAFE (Green)

STEEP SLOPE (Orange)

WATER RISK (Red)

Route Metrics Panel

Distance (km)

Elevation Gain (m)

Maximum Slope (°)

Risk Status

Elevation Profile Chart

Dynamic line graph using Chart.js


Map Initialization Module

Load 3D terrain
Enable terrain depth testing

const viewer = new Cesium.Viewer("cesiumContainer", {
  terrain: Cesium.Terrain.fromWorldTerrain(),
});
viewer.scene.globe.depthTestAgainstTerrain = true;


2. Layer Management Module

Load NDVI layer
Load NDWI layer
Toggle visibility
Adjust opacity
Auto fly-to imagery extent

async function loadLayers()


3. Route Drawing Module

Click-to-draw polyline
Ground clamping
Real-time route update

Cesium.ScreenSpaceEventHandler

4. Route Analysis Engine

✔ Terrain Sampling

Uses Cesium.sampleTerrainMostDetailed

Extracts elevation data

✔ Distance Calculation

Computes cumulative route distance

✔ Elevation Gain

Adds only positive vertical change

✔ Slope Detection

Calculates slope angle

Flags route if slope > 25°

✔ NDWI Water Detection

Tile-level pixel sampling

Detects blue-dominant pixels

Flags route as WATER RISK

Deliverable Achieved

✔ Unified professional dashboard
✔ Automated terrain + water safety detection
✔ Real-time visual risk feedback
✔ Elevation chart integration
✔ Export functionality
✔ Clean, structured, modular code
✔ Demo-ready MVP


http://localhost:8080/geoserver

http://localhost:8000/index.html

TOKEN "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI4NzU3NzMzYi02YzdhLTRkMTItYjM2NS1iYzE0ZWJkNDA2MzEiLCJpZCI6Mzg3Mjk4LCJpYXQiOjE3NzAyNzkxNDZ9.FrAOqmeY-jMTgzkXrtQPpoPEE5yGkOnSkYSSChmpn94"


FINAL CODE TO 3D Geospatial Dashboard

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>GeoRoute Safety Dashboard</title>

<script src="https://cesium.com/downloads/cesiumjs/releases/1.113/Build/Cesium/Cesium.js"></script>
<link href="https://cesium.com/downloads/cesiumjs/releases/1.113/Build/Cesium/Widgets/widgets.css" rel="stylesheet"/>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
html, body, #cesiumContainer {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  font-family: sans-serif;
}

.sidebar {
  position: absolute;
  left: 0;
  top: 0;
  width: 330px;
  height: 100%;
  background: rgba(20,20,20,0.97);
  color: white;
  padding: 20px;
  z-index: 999;
  overflow-y: auto;
}

.section { margin-bottom: 20px; }

h2, h3 { margin-top: 0; }

button {
  width: 100%;
  padding: 6px;
  margin-top: 6px;
  background: #2e86de;
  border: none;
  color: white;
  cursor: pointer;
  border-radius: 4px;
}

button:hover { background: #1b4f72; }

input[type="range"] { width: 100%; }

.status-box {
  padding: 10px;
  border-radius: 6px;
  text-align: center;
  font-weight: bold;
  margin-top: 10px;
}

.safe { background: #1e8449; }
.warning { background: #d68910; }
.danger { background: #c0392b; }

.metrics {
  background: #2c3e50;
  padding: 10px;
  border-radius: 6px;
  font-size: 13px;
  line-height: 1.6;
}

.chart-box {
  background: white;
  padding: 10px;
  border-radius: 6px;
}
</style>
</head>
<body>

<div id="cesiumContainer"></div>

<div class="sidebar">
  <h2>GeoRoute Safety Dashboard</h2>

  <div class="section">
    <h3>Layers</h3>
    <label><input type="checkbox" id="ndviToggle" checked> NDVI</label><br/>
    <label><input type="checkbox" id="ndwiToggle" checked> NDWI</label><br/><br/>
    Opacity
    <input type="range" id="opacity" min="0" max="1" step="0.05" value="0.7">
  </div>

  <div class="section">
    <h3>Route Tools</h3>
    <button id="startDraw">Start Route</button>
    <button id="stopDraw">Stop & Analyze</button>
    <button id="clearRoute">Clear Route</button>
    <button id="saveRoute">Export GeoJSON</button>
  </div>

  <div class="section">
    <h3>Route Status</h3>
    <div id="statusBox" class="status-box safe">SAFE</div>
  </div>

  <div class="section">
    <h3>Route Metrics</h3>
    <div id="metricsBox" class="metrics">
      Distance: - <br/>
      Elevation Gain: - <br/>
      Max Slope: - <br/>
      Risk: -
    </div>
  </div>

  <div class="section">
    <h3>Elevation Profile</h3>
    <div class="chart-box">
      <canvas id="elevationChart"></canvas>
    </div>
  </div>
</div>

<script>

// ================= TOKEN =================
Cesium.Ion.defaultAccessToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI4NzU3NzMzYi02YzdhLTRkMTItYjM2NS1iYzE0ZWJkNDA2MzEiLCJpZCI6Mzg3Mjk4LCJpYXQiOjE3NzAyNzkxNDZ9.FrAOqmeY-jMTgzkXrtQPpoPEE5yGkOnSkYSSChmpn94";

// ================= MAP =================
const viewer = new Cesium.Viewer("cesiumContainer", {
  terrain: Cesium.Terrain.fromWorldTerrain(),
});
viewer.scene.globe.depthTestAgainstTerrain = true;

// ================= LAYERS =================
let ndviLayer, ndwiLayer;

async function loadLayers() {

  const ndviProvider = await Cesium.IonImageryProvider.fromAssetId(4440174);
  const ndwiProvider = await Cesium.IonImageryProvider.fromAssetId(4440176);

  ndviLayer = viewer.imageryLayers.addImageryProvider(ndviProvider);
  ndwiLayer = viewer.imageryLayers.addImageryProvider(ndwiProvider);

  ndviLayer.alpha = 0.7;
  ndwiLayer.alpha = 0.7;

  viewer.camera.flyTo({ destination: ndviProvider.rectangle });

  document.getElementById("ndviToggle").onchange =
    e => ndviLayer.show = e.target.checked;

  document.getElementById("ndwiToggle").onchange =
    e => ndwiLayer.show = e.target.checked;

  document.getElementById("opacity").oninput =
    e => {
      ndviLayer.alpha = e.target.value;
      ndwiLayer.alpha = e.target.value;
    };
}
loadLayers();

// ================= ROUTE =================
let positions = [];
let routeEntity = null;
let drawing = false;
let elevationChart;

const handler = new Cesium.ScreenSpaceEventHandler(viewer.scene.canvas);

handler.setInputAction(click => {
  if (!drawing) return;
  const cartesian = viewer.scene.pickPosition(click.position);
  if (!cartesian) return;

  positions.push(cartesian);

  if (!routeEntity) {
    routeEntity = viewer.entities.add({
      polyline: {
        positions: new Cesium.CallbackProperty(() => positions, false),
        width: 4,
        material: Cesium.Color.CYAN,
        clampToGround: true
      }
    });
  }
}, Cesium.ScreenSpaceEventType.LEFT_CLICK);

document.getElementById("startDraw").onclick = () => drawing = true;

document.getElementById("clearRoute").onclick = () => {
  positions = [];
  if (routeEntity) viewer.entities.remove(routeEntity);
  routeEntity = null;
  updateStatus("SAFE");
};

document.getElementById("stopDraw").onclick = async () => {
  drawing = false;
  await analyzeRoute();
};

// ================= ANALYSIS ENGINE =================
async function analyzeRoute() {

  const terrainData = await Cesium.sampleTerrainMostDetailed(
    viewer.terrainProvider,
    positions.map(p => Cesium.Cartographic.fromCartesian(p))
  );

  let distance = 0;
  let elevationGain = 0;
  let maxSlope = 0;
  let waterDetected = false;

  for (let i = 1; i < terrainData.length; i++) {

    const vertical = terrainData[i].height - terrainData[i-1].height;
    const horizontal = Cesium.Cartesian3.distance(
      positions[i-1], positions[i]
    );

    distance += horizontal;

    if (vertical > 0) elevationGain += vertical;

    const slope = Cesium.Math.toDegrees(Math.atan(Math.abs(vertical)/horizontal));
    if (slope > maxSlope) maxSlope = slope;

    if (slope > 25) routeEntity.polyline.material = Cesium.Color.ORANGE;
  }

  // WATER CHECK (Tile Sampling)
  const imageryProvider = ndwiLayer.imageryProvider;
  const tilingScheme = imageryProvider.tilingScheme;

  for (let pos of positions) {
    const carto = Cesium.Cartographic.fromCartesian(pos);
    const level = imageryProvider.maximumLevel || 14;
    const tileXY = tilingScheme.positionToTileXY(carto, level);
    if (!tileXY) continue;

    const image = await imageryProvider.requestImage(tileXY.x, tileXY.y, level);
    if (!image) continue;

    const canvas = document.createElement("canvas");
    canvas.width = image.width;
    canvas.height = image.height;
    const ctx = canvas.getContext("2d");
    ctx.drawImage(image, 0, 0);

    const rect = tilingScheme.tileXYToRectangle(tileXY.x, tileXY.y, level);

    const x = (carto.longitude - rect.west)/(rect.east-rect.west)*image.width;
    const y = (rect.north - carto.latitude)/(rect.north-rect.south)*image.height;

    const pixel = ctx.getImageData(Math.floor(x), Math.floor(y), 1, 1).data;

    if (pixel[2] > 120 && pixel[2] > pixel[0] + 15) {
      waterDetected = true;
      break;
    }
  }

  // PRIORITY LOGIC
  if (waterDetected) {
    routeEntity.polyline.material = Cesium.Color.RED;
    updateStatus("WATER RISK");
  } else if (maxSlope > 25) {
    routeEntity.polyline.material = Cesium.Color.ORANGE;
    updateStatus("STEEP SLOPE");
  } else {
    routeEntity.polyline.material = Cesium.Color.CYAN;
    updateStatus("SAFE");
  }

  updateMetrics(distance, elevationGain, maxSlope);
  generateElevationProfile(terrainData, distance);
}

// ================= UI UPDATE =================
function updateStatus(text) {

  const box = document.getElementById("statusBox");
  box.className = "status-box";

  if (text === "SAFE") box.classList.add("safe");
  else if (text === "STEEP SLOPE") box.classList.add("warning");
  else box.classList.add("danger");

  box.innerText = text;
}

function updateMetrics(distance, gain, slope) {
  document.getElementById("metricsBox").innerHTML =
    "Distance: " + (distance/1000).toFixed(2) + " km<br/>" +
    "Elevation Gain: " + gain.toFixed(2) + " m<br/>" +
    "Max Slope: " + slope.toFixed(2) + "°<br/>" +
    "Risk: " + document.getElementById("statusBox").innerText;
}

// ================= CHART =================
function generateElevationProfile(data, totalDistance) {

  let distances = [];
  let elevations = [];
  let cumulative = 0;

  for (let i = 0; i < data.length; i++) {

    if (i > 0) {
      cumulative += Cesium.Cartesian3.distance(
        positions[i-1], positions[i]
      );
    }

    distances.push((cumulative/1000).toFixed(2));
    elevations.push(data[i].height.toFixed(2));
  }

  const ctx = document.getElementById("elevationChart").getContext("2d");

  if (elevationChart) elevationChart.destroy();

  elevationChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: distances,
      datasets: [{
        label: "Elevation (m)",
        data: elevations,
        borderColor: "blue",
        tension: 0.3
      }]
    }
  });
}

</script>
</body>
</html>
