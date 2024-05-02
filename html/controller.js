var session;

// Warten, bis das DOM vollständig geladen ist
document.addEventListener('DOMContentLoaded', function () {
    session = new QiSession('10.57.0.100');

    // Einrichten des Kamerastreams
    setupCameraStream();

    // Ereignishandler für die Steuerungsknöpfe einrichten
    document.getElementById('moveForwardBtn').onclick = moveForward;
    document.getElementById('moveBackwardBtn').onclick = moveBackward;
    document.getElementById('moveRightBtn').onclick = moveRight;
    document.getElementById('moveLeftBtn').onclick = moveLeft;
    document.getElementById('stopBtn').onclick = stopMotion;
});

// Vorwärtsbewegung
function moveForward() {
    move(0, 0, 1);
}

// Rückwärtsbewegung
function moveBackward() {
    move(0, 0, -1);
}

// Rechtsbewegung
function moveRight() {
    move(0, -1, 0);
}

// Links-Bewegung
function moveLeft() {
    move(0, 1, 0);
}

// Bewegung stoppen
function stopMotion() {
    session.service('ALMotion').then(function (motion) {
        motion.stopMove();
    });
}

// Bewegung ausführen
function move(x, y, theta) {
    var distance = parseFloat(document.getElementById('distance').value);

    session.service('ALMotion').then(function (motion) {
        motion.move(distance * x, distance * y, distance * theta);
    });
}

// Kamerastream einrichten
function setupCameraStream() {
    session.service('ALVideoDevice').then(function (videoDevice) {
        var cameraIndex = 0; // Index der Kamera (kann je nach Pepper-Konfiguration variieren)
        var resolution = 2; // Auflösung (2 = 640x480)
        var colorSpace = 11; // Farbraum (11 = RGB)

        // Kamerastream abonnieren
        videoDevice.subscribeCamera('CameraStream', cameraIndex, resolution, colorSpace, 5);

        // Bild vom Kamerastream abrufen und anzeigen
        videoDevice.getImageLocal('CameraStream').then(function (imageData) {
            var videoElement = document.getElementById('videoStream');
            videoElement.src = 'data:image/jpeg;base64,' + imageData[6];
        });
    });
}
