var autocomplete = [];

function updateHotel() {
    var name = document.getElementById('id_hotels-0-name').value;
    document.getElementById('accom_pre').innerHTML = name;
    document.getElementById('accom_post').innerHTML = name;
}


function checkSubString(a, b) {
    for (i=0;i<


}

function initMap() {
    for (i=0;i<document.getElementById('id_hotels-TOTAL_FORMS').value;i++) {
        autocomplete.push(new google.maps.places.Autocomplete(
            /** @type {!HTMLInputElement} */ (
            document.getElementById('id_hotels-'+i+'-name')), {
                types: ['establishment']
        }));
        autocomplete[autocomplete.length-1].addListener('place_changed',
                                                        updateHotel);
    }
    for (i=0;i<document.getElementById('id_attractions-TOTAL_FORMS').value;i++) {
        autocomplete.push(new google.maps.places.Autocomplete(
            /** @type {!HTMLInputElement} */ (
            document.getElementById('id_attractions-'+i+'-placename')), {
                types: ['establishment']
        }));
    }
    for (i=0;i<document.getElementById('id_placeName_0').value;i++) {
        autocomplete.push(new google.maps.places.Autocomplete(
            /** @type {!HTMLInputElement} */ (
            document.getElementById('id_placeName_'+i)), {
                types: ['establishment']
        }));
    }
}

function initMap2() {
}