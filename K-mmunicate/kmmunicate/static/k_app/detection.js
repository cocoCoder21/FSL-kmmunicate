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
 
  if (detections.multiHandedness.length === 0){
    Array.prototype.push.apply(all_keypoints, new Array(126).fill(0.));

  } else if (detections.multiHandedness.length === 1){
    // console.log(detections.multiHandedness[0].label);
   
    for (let point = 0; point < 21; point++){
        delete hand_keypoints[point].visibility
        kp_handler.push(Object.values(hand_keypoints[point]))
    }
    kp_handler = kp_handler.flat()

    //LEFT - RIGHT

        if (detections.multiHandedness[0].label === 'Right'){
          all_keypoints.push( new Array(63).fill(0.));
          all_keypoints.push( kp_handler);
          all_keypoints = all_keypoints.flat()
        } else {
          all_keypoints = kp_handler
          all_keypoints.push(new Array(63).fill(0.));
          all_keypoints = all_keypoints.flat()
          }

  } else { 
    total_keypoints = hand_keypoints.concat(detections.multiHandLandmarks[1])
  
    for (let point = 0; point < 42; point++){
        delete total_keypoints[point].visibility
      all_keypoints.push(Object.values(total_keypoints[point]));
    }
    all_keypoints = all_keypoints.flat()
  }
  
  // HIDDEN HEADER TAG
  $("#hidden-raw").html(all_keypoints);
  document.getElementById("hidden-raw").value = all_keypoints.toString();
//   console.log(document.getElementById("hidden-raw").value ); // .split(',')
  // console.log(all_keypoints)
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
