document.addEventListener("DOMContentLoaded", function() {
    var videoElement = document.getElementById("randomVideo");
    var videoFiles = [
        "video1.mp4",
        "video2.mp4",
        "video3.mp4",
        "video4.mp4"
    ];
    
    var randomIndex = Math.floor(Math.random() * videoFiles.length);
    var selectedVideo = videoFiles[randomIndex];
    //var videoPath = "/home/nao/voice_handler/videos/" + selectedVideo;
    var videoPath = "http://10.57.0.100/apps/voice_handler/videos/" + selectedVideo;

    videoElement.src = videoPath;    
    videoElement.muted = true;    
    videoElement.play();
    
    // Vollbildmodus aktivieren, wenn das Video abgespielt wird
    videoElement.addEventListener("play", function() {
        if (videoElement.requestFullscreen) {
            videoElement.requestFullscreen();
        } else if (videoElement.mozRequestFullScreen) {
            videoElement.mozRequestFullScreen();
        } else if (videoElement.webkitRequestFullscreen) {
            videoElement.webkitRequestFullscreen();
        } else if (videoElement.msRequestFullscreen) {
            videoElement.msRequestFullscreen();
        }

        // Ton aktivieren
        videoElement.muted = false;
    });
});