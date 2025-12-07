function RunEmotionDetection() {
  const textToAnalyze = document.getElementById("textToAnalyze").value;

  fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`)
    .then((response) => response.text())
    .then((data) => {
      document.getElementById("result").innerHTML = data;
    })
    .catch((error) => {
      document.getElementById("result").innerHTML =
        "Error calling the emotion detection service.";
      console.error("Error:", error);
    });
}

