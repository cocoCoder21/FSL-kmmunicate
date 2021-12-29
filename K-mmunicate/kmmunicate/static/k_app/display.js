// ====================== UPDATE KCAM HTML =======================
// var output = '{{ SIGN|escapejs }}';

// function write_sign(sign) {

//   // console.log() // sanity check

//   $('#sign_output').html('').load(
//       output
//       // sign
//   ); 

//   };

// $.post(function(data){
//   var signdata = data.sign
//   // var html = data.html;
//   $("#sign_output").replaceWith(signdata);
//   // do_whatever(signdata);
// })

// $.getJSON("/abc/?x="+3,
//     function(data){
//       console.log(data['sign'])
//     });

// function display_sign(){
//   $.ajax({
//         url: 'http://localhost:8000/kcam/',
//         success: function(response) {
//             document.getElementById('sign_output').innerHTML = response['sign'];
//         },
//         complete: function(){
//           setTimeout(display_sign, 1000);
//         }
//       });
// }

//============================================================================
// function refresh() {
//     $.ajax({
//        url: '{% cam %}',
//        success: function(data) {
//           $('#test').html(data.s);
//        }
//     });
//  };
//  $(function() {
//     refresh();
//     var int = setInterval("refresh()", 10000);
//  });
    
//=========================================================================
  
  // function autorefresh() {
  //       // auto refresh page after 1 second
  //       setInterval('display_sign()', 1000);
  // }
  
  // function refreshPage() {
  //   $.ajax({
  //     url: "{% url 'cam' %}",
  //     success: function(response) {
  //     // $('#sign_output').html(data);
  //     document.getElementById('sign_output').innerHTML = response['sign'];
  //     }
  //   });
  // }
  
  
  
// $.ajax({
//       url: 'http://localhost:8000/kcam/',
//       success: function(response) {

//     //Get string content of h4
//       var sign_holder = $("#sign_output").html();
//       console.log(sign_holder)


//       document.getElementById('sign_output').innerHTML = sign_holder;
//       }


//     //   ,complete: function(){setTimeout(display_sign, 1000);}

// });


// $.ajax({
//     url: 'http://localhost:8000/kcam/',    
//     type: 'GET',
//     dataType: 'json',
//     success: function(data){ 
//     console.log(data.mystring);
                                
//     }
// });

// $(document).ready(function(){
//   console.log(response);
//   $.ajax({
//       type: 'POST',
//       dataType: 'json',
//       url: 'k_app/kcam/',
//       data: data,
//       success: function(response) {
//            console.log(response.message);
//            $('#test').append(response.data);
//      }
//   });
// });


// setTimeout(function() { myFunction("I love You !!!"); }, 3000);

// function myFunction(value) {
//   document.getElementById("demo").innerHTML = value;
// }

// function display_sign(response){
//   console.log(response);
//   document.getElementById('sign_output').innerHTML = response;
// }

// $.ajax({
//       url: 'http://localhost:8000/kcam/',
//       success: function(response) {
//         console.log(response);
//       $('#sign_output').html(response);
//       console.log(response);
//       // document.getElementById('sign_output').innerHTML = 0;
//       }
//     });

// $(document).ready(function(){

//     setInterval(function(){
//       var dt = new Date();
//       $('test').text(dt.getSeconds());
//       console.log($('test').text());
//     }, 2000);

    
    
// });