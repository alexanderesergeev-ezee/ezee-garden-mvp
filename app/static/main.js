(function initMap() {
  const mapElement = document.getElementById("map");
  if (!mapElement || typeof L === "undefined") {
    return;
  }

  const map = L.map("map").setView([55.751244, 37.618423], 9);

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: "© OpenStreetMap",
  }).addTo(map);

  L.marker([55.751244, 37.618423])
    .addTo(map)
    .bindPopup("Москва: демо-точка для MVP")
    .openPopup();
})();
