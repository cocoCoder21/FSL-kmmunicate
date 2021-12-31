
//   $(document).ready(function(){

//     setInterval(function(){
  
//       // var sign_template = JSON.parse("{{signs|escapejs}}");
//       var sign_template = "{{ signs }}";
//         // var sign_template = JSON.parse("{{ signs }}");
//         console.log("RESPONSE = ", sign_template);
//         var sign_tag = document.getElementById('sign_output');
//         sign_tag.innerHTML=sign_template;

//     }, 3000);

  
  
//     $('#fsl_play').on('click', function () { 
//     var obj = document.createElement('audio');
//     obj.crossOrigin = 'anonymous';
//     var speech = "{% static 'audio/a.mp3' %}";
//     var letter = ['a','b','c'];
    
//     //TEMPLATE TAG AUDIO SIGN
//     // var sign_template = "{{ signs }}";
//     // var sign_audio = speech.slice(0,14) + sign_template +speech.slice(15)

//     obj.src = speech; 
//     obj.play(); 
// });

// //     $("fsl_play").click(function(){
// // console.log('PLAYED SUCCESSFULLY!')
// // const audio = new Audio(speech);
// // audio.play();
// // $.ajax({
// //         url: 'http://localhost:8000/kcam/', 
// //         success: function(result){
// //             $("#div1").html(result);
// //           }});
// // });

//   });

