// Verbindung zu Pepper herstellen
var session = new QiSession("10.57.0.100");
session.socket().on('connect', function () {
    console.log('QiSession connected!');

    // Akkustand überwachen
    session.service("ALBattery").then(function (battery) {
        // Akkustand abrufen
        battery.getBatteryCharge().then(function (charge) {
            updateBatteryLevel(charge);
        });

        // Aktualisiere Akkustand bei Änderungen
        battery.subscribeBatteryLevel().then(function (subscriber) {
            subscriber.signal.connect(function (charge) {
                updateBatteryLevel(charge);
            });
        });
    }).done();

}).on('disconnect', function () {
    console.log('QiSession disconnected!');
});

// Funktion zur Aktualisierung des Akkustands
function updateBatteryLevel(charge) {
    var batteryLevel = document.getElementById("battery-level");
    batteryLevel.innerText = charge + "%";

    // Farbe je nach Akkustand anpassen
    if (charge >= 50) {
        batteryLevel.style.backgroundColor = "green";
    } else if (charge >= 20) {
        batteryLevel.style.backgroundColor = "orange";
    } else {
        batteryLevel.style.backgroundColor = "red";
    }
}
