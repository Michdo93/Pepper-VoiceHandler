var session;

// Warten, bis das DOM vollständig geladen ist
document.addEventListener('DOMContentLoaded', function () {
    session = new QiSession('10.57.0.100');

    // Steuerelemente einrichten
    setupControls();

    // Galerie laden
    loadGallery();
});

// Funktion zum Einrichten der Steuerelemente
function setupControls() {
    var captureBtn = document.getElementById('captureBtn');
    captureBtn.onclick = takePicture;
}

// Funktion zum Aufnehmen eines Fotos
function takePicture() {
    var resolution = parseInt(document.getElementById('resolution').value);
    var pictureFormat = parseInt(document.getElementById('pictureFormat').value);

    session.service('ALPhotoCapture').then(function (photoCapture) {
        photoCapture.setResolution(resolution);
        photoCapture.setPictureFormat(pictureFormat);
        var currentDate = new Date().toISOString().replace(/:/g, '-');
        var fileName = "/home/nao/recordings/cameras/" + currentDate + "." + (pictureFormat === 0 ? 'jpg' : 'png'); // Bildformat festlegen
        photoCapture.takePicture(fileName).then(function () {
            loadGallery(); // Galerie neu laden
        });
    });
}

// Funktion zum Laden der Galerie
function loadGallery() {
    var imageList = document.getElementById('imageList');
    imageList.innerHTML = '';

    // Hier die URLs der Bilder dynamisch generieren
    var imageDir = '/home/nao/recordings/cameras/';
    var imageFiles = ['bild1.jpg', 'bild2.jpg', 'bild3.jpg']; // Beispiel für Dateinamen

    for (var i = 0; i < imageFiles.length; i++) {
        var imgElement = document.createElement('img');
        imgElement.src = imageDir + imageFiles[i];
        imgElement.alt = imageFiles[i];
        imgElement.className = 'gallery-image'; // Klasse für CSS-Styling hinzufügen
        imageList.appendChild(imgElement);
    }
}
