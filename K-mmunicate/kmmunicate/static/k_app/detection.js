let detections = {};

const videoElement = document.getElementsByClassName('input_video')[0];
const canvasElement = document.getElementsByClassName('output_canvas')[0];
const canvasCtx = canvasElement.getContext('2d');



function get_keypoints(results) {
  detections = results;
  let all_keypoints = [];  //collector
  let total_keypoints = 0;  //2 hand keypoints concatenated
  let kp_handler = [];
  let hand_keypoints =detections.multiHandLandmarks[0]
  

  // ================================================================
  if (detections.multiHandedness.length == 0){
    Array.prototype.push.apply(all_keypoints, new Array(126).fill(0.));
    

  } else if (detections.multiHandedness.length == 1){
    // console.log(detections.multiHandedness[0].label);
   
    for (let point = 0; point < 21; point++){
      kp_handler.push(hand_keypoints[point].x, hand_keypoints[point].y,
        hand_keypoints[point].z);
    }

    //RIGHT - LEFT  

    // if (detections.multiHandedness[0].label == 'Right'){
    //   all_keypoints = kp_handler
    //   Array.prototype.push.apply(all_keypoints, new Array(63).fill(0.));
    // }else{
    //   Array.prototype.push.apply(all_keypoints, new Array(63).fill(0.));
    //   Array.prototype.push.apply(all_keypoints, kp_handler);
    //   }
    

    //LEFT - RIGHT

    if (detections.multiHandedness[0].label == 'Right'){
      Array.prototype.push.apply(all_keypoints, new Array(63).fill(0.));
      Array.prototype.push.apply(all_keypoints, kp_handler);
    }else{
      all_keypoints = kp_handler
      Array.prototype.push.apply(all_keypoints, new Array(63).fill(0.));
      }



      // console.log(detections.multiHandedness[0].label, "RESULT >>> ", all_keypoints);

  } else {
    total_keypoints = hand_keypoints.concat(detections.multiHandLandmarks[1])
  
    for (let point = 0; point < 42; point++){
      all_keypoints.push(total_keypoints[point].x, total_keypoints[point].y,
        total_keypoints[point].z);
    }
  
  }

  let framed_keypoints = Array(30).fill(all_keypoints);
   

      $.ajax({
        url: 'http://localhost:8000/kcam/',
        type: 'POST',
        data: JSON.stringify({
          handResponse: all_keypoints
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

  //     framed_keypoints = []

  // $("fsl_play").click(function(){
  //   $.get('http://localhost:8000/kcam/', function(data){
  //     console.log(data);
  //   });
  // });

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
  width: 800,
  height: 580
});
camera.start();