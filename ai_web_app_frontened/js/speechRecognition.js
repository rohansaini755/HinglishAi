if ("webkitSpeechRecognition" in window) {
    let speechRecognition = new webkitSpeechRecognition();
    let final_transcript = "";
  
    speechRecognition.continuous = true;
    speechRecognition.interimResults = true;
    speechRecognition.lang = document.querySelector("#select_dialect").value;
  
    speechRecognition.onstart = () => {
      document.querySelector("#status").style.display = "block";
    };
    speechRecognition.onerror = (err) => {
      document.querySelector("#status").style.display = "none";
      console.log("Speech Recognition Error");
      console.log(err);
    };
    speechRecognition.onend = () => {
      document.querySelector("#status").style.display = "none";
      console.log("Speech Recognition Ended");
    };
  
    speechRecognition.onresult = (event) => {
      let interim_transcript = "";
  
      for (let i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
          final_transcript += event.results[i][0].transcript;
        } else {
          interim_transcript += event.results[i][0].transcript;
        }
      }
      document.querySelector("#final").innerHTML = final_transcript;
      document.querySelector("#interim").innerHTML = interim_transcript;
    };
  
    document.querySelector("#start").onclick = () => {
      speechRecognition.start();
    };
    document.querySelector("#stop").onclick = () => {
      speechRecognition.stop();
    };
  } else {
    console.log("Speech Recognition Not Available");
}

/*   fetchhing data from database */




// document.querySelector("#fetchTextid").onclick = () => {
//     fetchData(this);
// };

// function fetchData(element){
//     let p = fetch("http://13.231.225.7:8000/api/text/")
//     p.then((value1) =>{
//         return value1.json()
//     }).then((value2) => {
//         console.log(value2)
//         const obj = JSON.parse(value2)
//         const text = obj.name
//         const textn = hexToString(obj.hindiText)
//         const hint = obj.hintString
//         const hintn = hexToString(hint)
//         // document.getElementById("textarea2").value = textn
//         document.querySelector("#final2").innerHTML = textn
//         document.querySelector("#final3").innerHTML = hintn
//     })
// }


// function hexToString(hexRepresentation) {
//     let byteArray = new Uint8Array(hexRepresentation.match(/[\da-f]{2}/gi).map(function (h) {
//       return parseInt(h, 16)
//     }))
//     return new TextDecoder().decode(byteArray)
// }