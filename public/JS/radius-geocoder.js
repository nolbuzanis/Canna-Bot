var crg = require('city-reverse-geocoder');

// console.log(test.getNearestCitiesRadius(43.761539, -79.411079, 50, 50));

// Based on a bearing, and distance from a given lat/lon, return the nearest city from that point along the circle
function findCityMinimumRadius(lat, lon, dist, deg) {

    var latRad = toRadians(lat);
    var lonRad = toRadians(lon);

    var φ1 = latRad;
    var λ1 = lonRad;

    var d = dist;

    var R = 6371;

    var brng = deg;

    var φ2 = Math.asin( Math.sin(φ1)*Math.cos(d/R) + Math.cos(φ1)*Math.sin(d/R)*Math.cos(brng) );
    var λ2 = λ1 + Math.atan2(Math.sin(brng)*Math.sin(d/R)*Math.cos(φ1), Math.cos(d/R)-Math.sin(φ1)*Math.sin(φ2));

    //console.log("φ2: " + φ2);
    //console.log("λ2: " + λ2);

    var lat2 = toDegrees(φ2);
    var lon2 = toDegrees(λ2);

    //console.log(crg(lat2, lon2, 1));
    return crg(lat2, lon2, 1);
}

// Convert a value in degree to radians
function toRadians(deg) {
    return deg * 0.017453292519943295;
}

// Convert a value in radians to degrees
function toDegrees(rad) {
   return (180 / Math.PI) * rad;
}

// Determine the straight line distance between two lat/lon
function findLatLonDistance(lat1, lon1, lat2, lon2) {
    var R = 6371e3; // metres
    var φ1 = toRadians(lat1);
    var φ2 = toRadians(lat2);
    var Δφ = toRadians((lat2-lat1));
    var Δλ = toRadians((lon2-lon1));

    var a = Math.sin(Δφ/2) * Math.sin(Δφ/2) +
            Math.cos(φ1) * Math.cos(φ2) *
            Math.sin(Δλ/2) * Math.sin(Δλ/2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));

    var d = R * c;

    return d;
}

//findCityMinimumRadius(43.761539, -79.411079, 100, 0);

function removeDuplicates(myArr, prop) {
    return myArr.filter((obj, pos, arr) => {
        return arr.map(mapObj => mapObj[prop]).indexOf(obj[prop]) === pos;
    });
}

var findCities = function(lat, lon, dist){
    var cities = [];

    for (var deg = 0; deg < 360; deg++){
        var result = findCityMinimumRadius(lat, lon, dist, deg);
        result[0].distance = findLatLonDistance(lat, lon, result[0].latitude, result[0].longitude);
        cities.push(result[0]);
    }

    cities.sort(function (a, b) {
        if (a.distance === b.distance)
            return 0;
        if (a.distance > b.distance)
            return 1;
        else
            return -1;
    });

    var uniqueCities = removeDuplicates(cities, 'city');

    console.log(uniqueCities);

    console.log(uniqueCities.length);

    var obj = {};

    for ( var i=0, len=uniqueCities.length; i < len; i++ ){
        obj[uniqueCities[i]['city']] = uniqueCities[i];
    }

    cities = new Array();

    for ( var key in obj ){
        cities.push(obj[key]);
    }

    return (cities);

}

module.exports = findCities;
