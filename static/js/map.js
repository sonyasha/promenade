// var dataurl = '{% url "mapdata" %}';
// var pointsurl = '{% url "pointsdata" %}';
// var neighburl = '{% url "neighborhoodsdata" %}';
// var dataurl = '/map/mapdata/';
// var pointsurl = '/map/pointsdata';
// var neighburl = '/map/neighborhoodsdata';



window.addEventListener("map:init", function (event) {
    var map = event.detail.map;
    // Download GeoJSON data with Ajax
    urlsdata.forEach(el => {
        fetch(el)
        .then(function(resp) {
        return resp.json();
        })
        .then(function(data) {
            L.geoJson(data, {
            onEachFeature: function onEachFeature(feature, layer) {
            var props = feature.properties;
            var content = `<h3>${props.name}</h3>`;
            layer.bindPopup(content);
        }}).addTo(map);
        });
    });
});

// window.addEventListener("map:init", function (event) {
//     var map = event.detail.map;
//     // Download GeoJSON data with Ajax
//     path_data.forEach(el => {
//         fetch(el)
//         .then(function(resp) {
//         return resp.json();
//         })
//         .then(function(data) {
//             L.geoJson(data, {
//             onEachFeature: function onEachFeature(feature, layer) {
//             var props = feature.properties;
//             var content = `<h3>${props.name}</h3>`;
//             layer.bindPopup(content);
//         }}).addTo(map);
//         });
//     });
// });

// fetch(neighburl)
//     .then(function(resp) {
//     return resp.json();
//     })
//     .then(function(data) {
//         L.geoJson(data, {
//         onEachFeature: function onEachFeature(feature, layer) {
//         var props = feature.properties;
//         var content = `<h3>${props.name}</h3>`;
//         layer.bindPopup(content);
//     }}).addTo(map);
//     });

// fetch(pointsurl)
//     .then(function(resp) {
//     return resp.json();
//     })
//     .then(function(data) {
//         L.geoJson(data, {
//             onEachFeature: function onEachFeature(feature, layer) {
//             var props = feature.properties;
//             var content = `<h3>${props.name}</h3>`;
//             layer.bindPopup(content);
//         }}).addTo(map);
//     });
// fetch(dataurl)
//     .then(function(resp) {
//     return resp.json();
//     })
//     .then(function(data) {
//         L.geoJson(data, {
//             onEachFeature: function onEachFeature(feature, layer) {
//             var props = feature.properties;
//             //var content = `<img width="50" src="${props.picture_url}"/><h3>${props.title}</h3><p>${props.description}</p>`;
//             var content = `<h3>${props.name}</h3><p>${props.description}</p>`;
//             layer.bindPopup(content);
//         }}).addTo(map);
//     });  

