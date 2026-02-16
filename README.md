Week 1 Day 1 – Infrastructure Setup



Objective:-



Set up the geospatial environment and verify terrain rendering.



Tasks Completed:-



1. Installed docker desktop

2\. Deployed GeoServer via Docker

3\. Enabled CORS in GeoServer

4\. Registered on cesium ion uploaded the elevation GeoTIFF on ion my assets

4\. Initialize CesiumJS Project (Basic Globe)



>>>Create a folder example; D:\\cesium\_day1 

>>>inside the folder create one file example; index.html 

>>> Download cesium and keep the extracted file name Cesium(containing all the libraries) in the D:\\cesium\_day1 folder

>>> put the globe code in the .html file (The code must contain Asset id and token number from cesium ion)

>>> Download python 

>>> Open powershell of D:\\cesium\_day1 

>>> Run python --version

>>> Run cd D:\\GIS\_WEEK\_2\_3\\cesiumday\_1

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



1. Connected to Copernicus Open Access Hub



2\. Queried cloud-free Sentinel-2 imagery



3\. Downloaded required bands (Red, Green, NIR)



4\. Computed NDVI and NDWI



5\. Reprojected to EPSG:3857



......................................................................

......................................................................



Week 1 Day 3 – Automated Publishing to GeoServer



Objective:-



Automate layer publishing.



Tasks Completed:-



1. Integrated GeoServer REST API



pip install -U geoserver-restconfig

from geoserver.catalog import Catalog



2\. Created Workspace



3\. Created Coverage Store



4\. Published NDVI \& NDWI layers



5\. Removed manual UI dependency



Running pipeline.py automatically updates GeoServer layers



......................................................................

......................................................................



Week 1 Day 4 - Frontend Integration (CesiumJS)



Objective:-



Display NDVI \& NDWI layers on 3D globe.



Tasks Completed:-



1. Integrated the data on 3Dglobe through asset id and token on cesium ion



Geoserver → GeoTIFF → Cesuim ion → Asset ID + Token → CesiumJS



Implemented:



1. NDVI toggle



2\. NDWI toggle



3\. Opacity slider



Deliverable

Analytical layers overlayed on terrain



......................................................................

......................................................................



Week 1 Day 5 – Full Pipeline Testing



Objective:-



Validate end-to-end system.



Tasks Completed:-



1. Tested full ETL flow:

Download → Process → Publish → Visualize



2\. Verified terrain alignment



3\. Optimized imagery loading



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

1. Terrain Sampling

Used Cesium’s terrain API

Cesium.sampleTerrainMostDetailed()



* Converted route Cartesian positions to Cartographic coordinates.



* Sampled terrain heights using the active terrain provider.



* Retrieved accurate elevation values for each route point.



2\. Distance calculation 

Cesium.Cartesian3.distance()



* Cumulative distance computed in kilometers for X-axis plotting





3\. Elevation Chart Rendering



* Integrated Chart.js to render a 2D line chart



* Chart Features:



X-axis: Distance (km)



Y-axis: Elevation (m)



Smooth curve rendering



Auto-update when route is completed



4\. Trigger Mechanism



Elevation profile generation is triggered when Stop Route button is clicked. This ensures the chart updates only after route completion.





Deliverable



* Terrain elevation sampling along route
* Cumulative distance computation
* Dynamic 2D elevation profile chart
* Automatic chart update on route completion



....................................................................................................................................................................



Week 2 Day 3 - Water/Obstacle Check 



Implement logic to detect whether a user-drawn route intersects a water body using the NDWI imagery layer.



* If water is detected:

Trigger a UI alert

Change route color to RED



* If safe:

Keep route color CYAN





1. Route Completion Trigger



Water detection runs automatically when:

Stop Route button is clicked

await checkWaterIntersection();



2\. NDWI Sampling Logic (Client-Side Pixel Sampling)



For each route point:

* Convert Cartesian → Cartographic
* Get tile coordinates using:

tilingScheme.positionToTileXY()



Request tile image:

imageryProvider.requestImage()





Extract pixel color using:

getImageData()



3\. Water Detection Rule



Water is identified using strong blue dominance. This logic detects pixels with high water reflectance (NDWI visualization).

if (b > 120 \&\& b > r + 15 \&\& b > g + 15)



....................................................................................................................................................................



Week 2 Day 4 - Dashboard Finalization 



Objective



Refine the application UI/UX, modularize logic, and prepare a polished MVP (Minimum Viable Product) for demonstration.



UI/UX Improvements (Dashboard Consolidation)



All controls were merged into a single left sidebar panel.



&nbsp;Sidebar Sections



* Layers Control



NDVI Toggle



NDWI Toggle



Opacity Slider



* Route Tools



Start Route



Stop \& Analyze



Clear Route



Export GeoJSON



* Route Status Indicator



SAFE (Green)



STEEP SLOPE (Orange)



WATER RISK (Red)



* Route Metrics Panel



Distance (km)



Elevation Gain (m)



Maximum Slope (°)



Risk Status



* Elevation Profile Chart



Dynamic line graph using Chart.js





1. Map Initialization Module



Load 3D terrain

Enable terrain depth testing



const viewer = new Cesium.Viewer("cesiumContainer", {

&nbsp; terrain: Cesium.Terrain.fromWorldTerrain(),

});

viewer.scene.globe.depthTestAgainstTerrain = true;





2\. Layer Management Module



Load NDVI layer

Load NDWI layer

Toggle visibility

Adjust opacity

Auto fly-to imagery extent



async function loadLayers()





3\. Route Drawing Module



Click-to-draw polyline

Ground clamping

Real-time route update



Cesium.ScreenSpaceEventHandler



4\. Route Analysis Engine



✔ Terrain Sampling



* Uses Cesium.sampleTerrainMostDetailed



* Extracts elevation data



✔ Distance Calculation



* Computes cumulative route distance



✔ Elevation Gain



* Adds only positive vertical change



✔ Slope Detection



* Calculates slope angle



* Flags route if slope > 25°



✔ NDWI Water Detection



* Tile-level pixel sampling



* Detects blue-dominant pixels



* Flags route as WATER RISK



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

&nbsp; margin: 0;

&nbsp; padding: 0;

&nbsp; width: 100%;

&nbsp; height: 100%;

&nbsp; overflow: hidden;

&nbsp; font-family: sans-serif;

}



.sidebar {

&nbsp; position: absolute;

&nbsp; left: 0;

&nbsp; top: 0;

&nbsp; width: 330px;

&nbsp; height: 100%;

&nbsp; background: rgba(20,20,20,0.97);

&nbsp; color: white;

&nbsp; padding: 20px;

&nbsp; z-index: 999;

&nbsp; overflow-y: auto;

}



.section { margin-bottom: 20px; }



h2, h3 { margin-top: 0; }



button {

&nbsp; width: 100%;

&nbsp; padding: 6px;

&nbsp; margin-top: 6px;

&nbsp; background: #2e86de;

&nbsp; border: none;

&nbsp; color: white;

&nbsp; cursor: pointer;

&nbsp; border-radius: 4px;

}



button:hover { background: #1b4f72; }



input\[type="range"] { width: 100%; }



.status-box {

&nbsp; padding: 10px;

&nbsp; border-radius: 6px;

&nbsp; text-align: center;

&nbsp; font-weight: bold;

&nbsp; margin-top: 10px;

}



.safe { background: #1e8449; }

.warning { background: #d68910; }

.danger { background: #c0392b; }



.metrics {

&nbsp; background: #2c3e50;

&nbsp; padding: 10px;

&nbsp; border-radius: 6px;

&nbsp; font-size: 13px;

&nbsp; line-height: 1.6;

}



.chart-box {

&nbsp; background: white;

&nbsp; padding: 10px;

&nbsp; border-radius: 6px;

}

</style>

</head>

<body>



<div id="cesiumContainer"></div>



<div class="sidebar">

&nbsp; <h2>GeoRoute Safety Dashboard</h2>



&nbsp; <div class="section">

&nbsp;   <h3>Layers</h3>

&nbsp;   <label><input type="checkbox" id="ndviToggle" checked> NDVI</label><br/>

&nbsp;   <label><input type="checkbox" id="ndwiToggle" checked> NDWI</label><br/><br/>

&nbsp;   Opacity

&nbsp;   <input type="range" id="opacity" min="0" max="1" step="0.05" value="0.7">

&nbsp; </div>



&nbsp; <div class="section">

&nbsp;   <h3>Route Tools</h3>

&nbsp;   <button id="startDraw">Start Route</button>

&nbsp;   <button id="stopDraw">Stop \& Analyze</button>

&nbsp;   <button id="clearRoute">Clear Route</button>

&nbsp;   <button id="saveRoute">Export GeoJSON</button>

&nbsp; </div>



&nbsp; <div class="section">

&nbsp;   <h3>Route Status</h3>

&nbsp;   <div id="statusBox" class="status-box safe">SAFE</div>

&nbsp; </div>



&nbsp; <div class="section">

&nbsp;   <h3>Route Metrics</h3>

&nbsp;   <div id="metricsBox" class="metrics">

&nbsp;     Distance: - <br/>

&nbsp;     Elevation Gain: - <br/>

&nbsp;     Max Slope: - <br/>

&nbsp;     Risk: -

&nbsp;   </div>

&nbsp; </div>



&nbsp; <div class="section">

&nbsp;   <h3>Elevation Profile</h3>

&nbsp;   <div class="chart-box">

&nbsp;     <canvas id="elevationChart"></canvas>

&nbsp;   </div>

&nbsp; </div>

</div>



<script>



// ================= TOKEN =================

Cesium.Ion.defaultAccessToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI4NzU3NzMzYi02YzdhLTRkMTItYjM2NS1iYzE0ZWJkNDA2MzEiLCJpZCI6Mzg3Mjk4LCJpYXQiOjE3NzAyNzkxNDZ9.FrAOqmeY-jMTgzkXrtQPpoPEE5yGkOnSkYSSChmpn94";



// ================= MAP =================

const viewer = new Cesium.Viewer("cesiumContainer", {

&nbsp; terrain: Cesium.Terrain.fromWorldTerrain(),

});

viewer.scene.globe.depthTestAgainstTerrain = true;



// ================= LAYERS =================

let ndviLayer, ndwiLayer;



async function loadLayers() {



&nbsp; const ndviProvider = await Cesium.IonImageryProvider.fromAssetId(4440174);

&nbsp; const ndwiProvider = await Cesium.IonImageryProvider.fromAssetId(4440176);



&nbsp; ndviLayer = viewer.imageryLayers.addImageryProvider(ndviProvider);

&nbsp; ndwiLayer = viewer.imageryLayers.addImageryProvider(ndwiProvider);



&nbsp; ndviLayer.alpha = 0.7;

&nbsp; ndwiLayer.alpha = 0.7;



&nbsp; viewer.camera.flyTo({ destination: ndviProvider.rectangle });



&nbsp; document.getElementById("ndviToggle").onchange =

&nbsp;   e => ndviLayer.show = e.target.checked;



&nbsp; document.getElementById("ndwiToggle").onchange =

&nbsp;   e => ndwiLayer.show = e.target.checked;



&nbsp; document.getElementById("opacity").oninput =

&nbsp;   e => {

&nbsp;     ndviLayer.alpha = e.target.value;

&nbsp;     ndwiLayer.alpha = e.target.value;

&nbsp;   };

}

loadLayers();



// ================= ROUTE =================

let positions = \[];

let routeEntity = null;

let drawing = false;

let elevationChart;



const handler = new Cesium.ScreenSpaceEventHandler(viewer.scene.canvas);



handler.setInputAction(click => {

&nbsp; if (!drawing) return;

&nbsp; const cartesian = viewer.scene.pickPosition(click.position);

&nbsp; if (!cartesian) return;



&nbsp; positions.push(cartesian);



&nbsp; if (!routeEntity) {

&nbsp;   routeEntity = viewer.entities.add({

&nbsp;     polyline: {

&nbsp;       positions: new Cesium.CallbackProperty(() => positions, false),

&nbsp;       width: 4,

&nbsp;       material: Cesium.Color.CYAN,

&nbsp;       clampToGround: true

&nbsp;     }

&nbsp;   });

&nbsp; }

}, Cesium.ScreenSpaceEventType.LEFT\_CLICK);



document.getElementById("startDraw").onclick = () => drawing = true;



document.getElementById("clearRoute").onclick = () => {

&nbsp; positions = \[];

&nbsp; if (routeEntity) viewer.entities.remove(routeEntity);

&nbsp; routeEntity = null;

&nbsp; updateStatus("SAFE");

};



document.getElementById("stopDraw").onclick = async () => {

&nbsp; drawing = false;

&nbsp; await analyzeRoute();

};



// ================= ANALYSIS ENGINE =================

async function analyzeRoute() {



&nbsp; const terrainData = await Cesium.sampleTerrainMostDetailed(

&nbsp;   viewer.terrainProvider,

&nbsp;   positions.map(p => Cesium.Cartographic.fromCartesian(p))

&nbsp; );



&nbsp; let distance = 0;

&nbsp; let elevationGain = 0;

&nbsp; let maxSlope = 0;

&nbsp; let waterDetected = false;



&nbsp; for (let i = 1; i < terrainData.length; i++) {



&nbsp;   const vertical = terrainData\[i].height - terrainData\[i-1].height;

&nbsp;   const horizontal = Cesium.Cartesian3.distance(

&nbsp;     positions\[i-1], positions\[i]

&nbsp;   );



&nbsp;   distance += horizontal;



&nbsp;   if (vertical > 0) elevationGain += vertical;



&nbsp;   const slope = Cesium.Math.toDegrees(Math.atan(Math.abs(vertical)/horizontal));

&nbsp;   if (slope > maxSlope) maxSlope = slope;



&nbsp;   if (slope > 25) routeEntity.polyline.material = Cesium.Color.ORANGE;

&nbsp; }



&nbsp; // WATER CHECK (Tile Sampling)

&nbsp; const imageryProvider = ndwiLayer.imageryProvider;

&nbsp; const tilingScheme = imageryProvider.tilingScheme;



&nbsp; for (let pos of positions) {

&nbsp;   const carto = Cesium.Cartographic.fromCartesian(pos);

&nbsp;   const level = imageryProvider.maximumLevel || 14;

&nbsp;   const tileXY = tilingScheme.positionToTileXY(carto, level);

&nbsp;   if (!tileXY) continue;



&nbsp;   const image = await imageryProvider.requestImage(tileXY.x, tileXY.y, level);

&nbsp;   if (!image) continue;



&nbsp;   const canvas = document.createElement("canvas");

&nbsp;   canvas.width = image.width;

&nbsp;   canvas.height = image.height;

&nbsp;   const ctx = canvas.getContext("2d");

&nbsp;   ctx.drawImage(image, 0, 0);



&nbsp;   const rect = tilingScheme.tileXYToRectangle(tileXY.x, tileXY.y, level);



&nbsp;   const x = (carto.longitude - rect.west)/(rect.east-rect.west)\*image.width;

&nbsp;   const y = (rect.north - carto.latitude)/(rect.north-rect.south)\*image.height;



&nbsp;   const pixel = ctx.getImageData(Math.floor(x), Math.floor(y), 1, 1).data;



&nbsp;   if (pixel\[2] > 120 \&\& pixel\[2] > pixel\[0] + 15) {

&nbsp;     waterDetected = true;

&nbsp;     break;

&nbsp;   }

&nbsp; }



&nbsp; // PRIORITY LOGIC

&nbsp; if (waterDetected) {

&nbsp;   routeEntity.polyline.material = Cesium.Color.RED;

&nbsp;   updateStatus("WATER RISK");

&nbsp; } else if (maxSlope > 25) {

&nbsp;   routeEntity.polyline.material = Cesium.Color.ORANGE;

&nbsp;   updateStatus("STEEP SLOPE");

&nbsp; } else {

&nbsp;   routeEntity.polyline.material = Cesium.Color.CYAN;

&nbsp;   updateStatus("SAFE");

&nbsp; }



&nbsp; updateMetrics(distance, elevationGain, maxSlope);

&nbsp; generateElevationProfile(terrainData, distance);

}



// ================= UI UPDATE =================

function updateStatus(text) {



&nbsp; const box = document.getElementById("statusBox");

&nbsp; box.className = "status-box";



&nbsp; if (text === "SAFE") box.classList.add("safe");

&nbsp; else if (text === "STEEP SLOPE") box.classList.add("warning");

&nbsp; else box.classList.add("danger");



&nbsp; box.innerText = text;

}



function updateMetrics(distance, gain, slope) {

&nbsp; document.getElementById("metricsBox").innerHTML =

&nbsp;   "Distance: " + (distance/1000).toFixed(2) + " km<br/>" +

&nbsp;   "Elevation Gain: " + gain.toFixed(2) + " m<br/>" +

&nbsp;   "Max Slope: " + slope.toFixed(2) + "°<br/>" +

&nbsp;   "Risk: " + document.getElementById("statusBox").innerText;

}



// ================= CHART =================

function generateElevationProfile(data, totalDistance) {



&nbsp; let distances = \[];

&nbsp; let elevations = \[];

&nbsp; let cumulative = 0;



&nbsp; for (let i = 0; i < data.length; i++) {



&nbsp;   if (i > 0) {

&nbsp;     cumulative += Cesium.Cartesian3.distance(

&nbsp;       positions\[i-1], positions\[i]

&nbsp;     );

&nbsp;   }



&nbsp;   distances.push((cumulative/1000).toFixed(2));

&nbsp;   elevations.push(data\[i].height.toFixed(2));

&nbsp; }



&nbsp; const ctx = document.getElementById("elevationChart").getContext("2d");



&nbsp; if (elevationChart) elevationChart.destroy();



&nbsp; elevationChart = new Chart(ctx, {

&nbsp;   type: "line",

&nbsp;   data: {

&nbsp;     labels: distances,

&nbsp;     datasets: \[{

&nbsp;       label: "Elevation (m)",

&nbsp;       data: elevations,

&nbsp;       borderColor: "blue",

&nbsp;       tension: 0.3

&nbsp;     }]

&nbsp;   }

&nbsp; });

}



</script>

</body>

</html>



