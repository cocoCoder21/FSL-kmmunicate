let detections = {};

const videoElement = document.getElementsByClassName('input_video')[0];
const canvasElement = document.getElementsByClassName('output_canvas')[0];
const canvasCtx = canvasElement.getContext('2d');



function get_keypoints(results) {
  detections = results;
  const all_keypoints = [];  //collector
  let total_keypoints = 0;  //2 hand keypoints concatenated
  let hand_keypoints =detections.multiHandLandmarks[0]


  if (detections.multiHandLandmarks.length == 0){
    let null_filler = new Array(126).fill(0.);
    Array.prototype.push.apply(all_keypoints, null_filler);
    

  } else if (detections.multiHandLandmarks.length == 1){
    

    for (let point = 0; point < 21; point++){
      all_keypoints.push(hand_keypoints[point].x, hand_keypoints[point].y,
        hand_keypoints[point].z);

    }

    let null_filler = new Array(63).fill(0.);
    Array.prototype.push.apply(all_keypoints, null_filler);
    
  } else {
    total_keypoints = hand_keypoints.concat(detections.multiHandLandmarks[1])
  
    for (let point = 0; point < 42; point++){
      all_keypoints.push(total_keypoints[point].x, total_keypoints[point].y,
        total_keypoints[point].z);
    }
  
  }

  let framed_keypoints = Array(30).fill(all_keypoints);
  
  // var URL = "{% 'url cam' %}";
  // var h_data = JSON.stringify({
  //   handResponse: all_keypoints
  // })

      $.ajax({
        url: 'http://localhost:8000/kcam/',
        type: 'POST',
        data: JSON.stringify({
          handResponse: framed_keypoints
        }),
        contentType: "application/json",
        // dataType: "json",
        headers: {"X-CSRFToken":'{{ csrf_token }}'},
        success: function (result) {
            // console.log(typeof(h_data))
            console.log("successful post ajax request!");
        },
        error: function (result) {
            console.log("error: ajax request failed.");
        }
      });

      framed_keypoints = []

}


const hands = new Hands({locateFile: (file) => {
  return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
}});

hands.setOptions({
  maxNumHands: 2,
  modelComplexity: 1,
  minDetectionConfidence: 0.5,
  minTrackingConfidence: 0.5
});

hands.onResults(get_keypoints);


const camera = new Camera(videoElement, {
  onFrame: async () => {
    await hands.send({image: videoElement});
  },
  width: 640,
  height: 480
});
camera.start();