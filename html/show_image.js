document.addEventListener("DOMContentLoaded", function() {
    var imageElement = document.getElementById("randomImage");
    var imageFiles = [
        "bild1.png",
        "bild2.png",
        "bild3.png",
        "bild4.png"
    ];

    var randomIndex = Math.floor(Math.random() * imageFiles.length);
    var selectedImage = imageFiles[randomIndex];
    var imagePath = "http://10.57.0.100/apps/voice_handler/images/" + selectedImage;

    imageElement.src = imagePath;
});