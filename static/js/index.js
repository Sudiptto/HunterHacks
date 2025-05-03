// NOTE THIS IS WHERE THE GOOGLE MAPS API + PARSED GEO DATA WILL TAKE PLACE IN 


setTimeout(function(){
    document.querySelector(".preloader").style.display = "none";
  }, 1000);
  
  if (!sessionStorage.getItem('page_reloaded')) {
    sessionStorage.setItem('page_reloaded', true);
    location.reload();
  }
  
  let map, infoWindow;
  // Create info
  
  
  function initMap() {
  
    map = new google.maps.Map(document.getElementById("map"), {
      // default location 
      center: { lat: 40.650002, lng: -73.949997 },
      zoom: 15,
      disableDefaultUI: true,
      mapTypeId: 'satellite' 
      // fullscreenControl: false
    });
    infoWindow = new google.maps.InfoWindow();

    /*ADDED A LEGEND TO THE MAPS -> NOTE FOR SASHA & SAMIN -> HERE YOU CAN EDIT THE STYLES OF THE KEY APPEARING ON THE TOP LEFT */
    /* IF YOU WANT TO ADD CUSTOM ICONS TO THE LEGEND, IE: ACCESSIBILITY & SUCH CREATE A NEW FOLDER ICONS & U CAN PUT PNG FILES IN THEM */
    const legend = document.createElement("div");
    legend.id = "legend";
    legend.style.backgroundColor = "transparent";
    legend.style.border = "1px solid #ccc";
    legend.style.padding = "10px";
    legend.style.position = "absolute";
    legend.style.top = "10px";
    legend.style.left = "10px";
    legend.style.zIndex = "1";
    legend.style.maxWidth = "200px";
    legend.style.boxShadow = "2px 2px 5px rgba(0, 0, 0, 0.2)";

    const title = document.createElement("h3");
    title.textContent = "Bathrooms";
    title.style.backgroundColor = "black"
    title.style.fontSize = "14px"; // Adjust font size
    title.style.fontWeight = "bold"; // Make the text bold
    title.style.marginBottom = "8px"; // Add some spacing below the title
    legend.appendChild(title);
    // Define legend items
    const legendItems = [
        { iconUrl: "http://maps.google.com/mapfiles/ms/icons/green-dot.png", description: "Public Bathrooms" },
        { iconUrl: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png", description: "Crowd Sourced Bathrooms" }
    ];

    // Create legend items and add them to the legend
    for (const item of legendItems) {
        const legendItem = document.createElement("div");
        legendItem.classList.add("legend-item");

        const icon = document.createElement("img");
        icon.src = item.iconUrl;
        icon.alt = item.description;

        const description = document.createElement("span");
        description.textContent = item.description;

        legendItem.appendChild(icon);
        legendItem.appendChild(description);
        legend.appendChild(legendItem);
    }

    // Add the legend to the map container
    const mapContainer = document.getElementById("map");
    mapContainer.appendChild(legend);

    locationButton.addEventListener("click", () => {

      // Try HTML5 geolocation.
      if (navigator.geolocation) {
        
        navigator.geolocation.getCurrentPosition(
          (position) => {
            const pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude,
            };
            infoWindow.open(map);
            map.setCenter(pos);
          },
          () => {
            handleLocationError(true, infoWindow, map.getCenter());
          }
        );
      } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
      }
     });
     
     // CLICK FUNCTION
     google.maps.event.addListener(map, 'dblclick', function(event){
      let marker = new google.maps.Marker({
          position: event.latLng,
          map: map,
          draggable: true,
          icon: {
            url:"http://maps.google.com/mapfiles/ms/icons/pink-dot.png"
          }
       });
    
       google.maps.event.addListener(marker,'dblclick', function(event){
          marker.setMap(null);
          
       });
  
      let geocoder = new google.maps.Geocoder();
      let latLng = event.latLng;
      
    
      // Send a geocoding request to Google Maps Geocoding API.
      geocoder.geocode({ location: latLng }, (results, status) => {
        if (status === google.maps.GeocoderStatus.OK) {
          // Extract the postal code (zipcode) from the geocoding results.
          const zipcode = findZipCodeInResults(results[0]);
          
          // Extract the exact latitude and longitude as strings.
          const latitude = latLng.lat().toString();
          const longitude = latLng.lng().toString();
          
          // Create an object with latitude, longitude, and zipcode.
          const locationData = {
            latitude: latitude,
            longitude: longitude,
            zipcode: zipcode,
          };
          
        }
      });
      })
     
  }
  
  
  window.initMap = initMap;




  
 