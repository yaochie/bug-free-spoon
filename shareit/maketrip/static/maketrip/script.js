var autocomplete = [];

function addField() {
    document.getElementById('id_attractions-TOTAL_FORMS').value++;
}
function delField() {
    document.getElementById('id_attractions-TOTAL_FORMS').value--;
}
function addHotel() {
    document.getElementById('id_hotels-TOTAL_FORMS').value++;
}
function updateHotel() {
    var name = document.getElementById('id_hotels-0-name').value;
    document.getElementById('accom_pre').innerHTML = name;
    document.getElementById('accom_post').innerHTML = name;
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
}

function initMap2() {
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
    for (i=0;i<document.getElementById('id_attractions-TOTAL_FORMS').value;i++) {
        autocomplete.push(new google.maps.places.Autocomplete(
            /** @type {!HTMLInputElement} */ (
            document.getElementById('id_name')), {
                types: ['establishment']
        }));
    }
    for (i=0;i<document.getElementById('id_placeName').value;i++) {
        autocomplete.push(new google.maps.places.Autocomplete(
            /** @type {!HTMLInputElement} */ (
            document.getElementById('id_placeName')), {
                types: ['establishment']
        }));
    }
}

function addAccomm() {
}