let detections = {};

const videoElement = document.getElementsByClassName('input_video')[0];
const canvasElement = document.getElementsByClassName('output_canvas')[0];
const canvasCtx = canvasElement.getContext('2d');
// const KeypointMemo = memoizer(get_keypoints)

// function memoizer(fn){
//   let cache = {};

//   return function(val){
//     if (cache[n] != undefined ) {
//       return cache[n]
//     } else {
//       let result = fun(n)
//       cache[n] = result
//       return result
//     }
//   }
// }

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
      kp_handler.push(hand_keypoints[point].x, hand_keypoints[point].y,
        hand_keypoints[point].z);
    }

    //LEFT - RIGHT

        if (detections.multiHandedness[0].label === 'Right'){
          Array.prototype.push.apply(all_keypoints, new Array(63).fill(0.));
          Array.prototype.push.apply(all_keypoints, kp_handler);
        } else {
          all_keypoints = kp_handler
          Array.prototype.push.apply(all_keypoints, new Array(63).fill(0.));
          }

  } else {
    total_keypoints = hand_keypoints.concat(detections.multiHandLandmarks[1])
  
    for (let point = 0; point < 42; point++){
      all_keypoints.push(total_keypoints[point].x, total_keypoints[point].y,
        total_keypoints[point].z);
    }
  
  }
  
  // HIDDEN HEADER TAG
  $("#hidden-raw").html(all_keypoints);
  document.getElementById("hidden-raw").value = all_keypoints.toString();
  console.log(document.getElementById("hidden-raw").value ); // .split(',')

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
