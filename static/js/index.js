function initMap() {
    const Toronto = {lat: 43.653, lng: -79.383};
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 10,
        center: Toronto,
    });

    const marker = new google.maps.Marker({
        position: Toronto,
        map,
        title: "Soosh | Sushi Store"
    });
}