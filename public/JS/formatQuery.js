
function format(location){
	var bad_char = location.indexOf("-");
    if(bad_char) location = location.slice(bad_char + 1, location.length);

    return location;
}

module.exports = format;