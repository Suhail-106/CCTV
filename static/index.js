function navbar() {
    var icons = document.querySelectorAll('.navbar h1');
    icons.forEach(function (icon) {
        icon.addEventListener('click', function (event) { 
            event.stopPropagation();
            icons.forEach(h1 => h1.style.color = 'white');
            icon.style.color = "lightblue";
        }); 
    });
    document.addEventListener('click', function () {
          icons.forEach(icon => icon.style.color = "white");  
    });
    
}

function imagesaved() {
    document.getElementById('imagesaved').classList.toggle('active');
}
function imagesavedr() {
    document.getElementById('imagesaved').classList.remove('active');
}

function imagesaved1() {
    document.getElementById('imagesaved1').classList.toggle('active');
}
function imagesaved1r() {
    document.getElementById('imagesaved1').classList.remove('active');
}




function checkEmail() {
    const emailInput = document.getElementById('email1');
    const errorSpan = document.getElementById('error-message');

    // yahan tum validation kar sakte ho
    if (emailInput.value.trim() === '') {
        emailInput.classList.remove('border-red-500');
        emailInput.classList.add('border-white');
        errorSpan.classList.add('hidden');
    } else {
        // example: agar email valid format nahi hai to error dikhana
        if (!emailInput.value.includes('@')) {
            emailInput.classList.remove('border-white');
            emailInput.classList.add('border-red-500');
            errorSpan.classList.remove('hidden');
        } else {
            emailInput.classList.remove('border-red-500');
            emailInput.classList.add('border-white');
            errorSpan.classList.add('hidden');
        }
    }
}

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;

    // Google Maps link
    const mapsLink = `https://maps.google.com/?q=${lat},${lon}`;

    // Address input me Google Maps link store kar do
    const addressInput = document.getElementById("Address1");
    addressInput.value = mapsLink;
}

function showError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            alert("User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            alert("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
            alert("An unknown error occurred.");
            break;
    }
}


document.addEventListener('DOMContentLoaded', function () {
    const items = document.querySelectorAll('.items p');
    const images = document.querySelectorAll('.image_container img');

    function showImage(item) {
        const imgId = item.getAttribute('data-imgs');
        images.forEach(img => {
            img.classList.add('hidden');  // sab hide karo
        });
        document.getElementById('myImage' + imgId).classList.remove('hidden');  // sirf selected show karo
    }

    function hideImages() {
        images.forEach(img => {
            img.classList.add('hidden'); // mouse bahar nikalne par sab hide
        });
    }

    items.forEach(item => {
        item.addEventListener('mouseover', () => {
            showImage(item);
        });

        item.addEventListener('mouseout', () => {
            hideImages();
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const items1 = document.querySelectorAll('.items2 p');
    const images1 = document.querySelectorAll('.image_container2 img');

    function showImage1(item) {
        const imgId = item.getAttribute('data-imgs2');
        images1.forEach(img => {
            img.classList.add('hidden');  // sab hide karo
        });
        document.getElementById('myImage2' + imgId).classList.remove('hidden');  // sirf selected show karo
    }

    function hideImages1() {
        images1.forEach(img => {
            img.classList.add('hidden'); // mouse bahar nikalne par sab hide
        });
    }

    items1.forEach(item => {
        item.addEventListener('mouseover', () => {
            showImage1(item);
        });

        item.addEventListener('mouseout', () => {
            hideImages1();
        });
    });
});


function profile() {
    document.getElementById('profile').classList.toggle('active');
}
function profileR() {
    document.getElementById('profile').classList.remove('active');
}



