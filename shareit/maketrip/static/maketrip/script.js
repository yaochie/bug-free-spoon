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