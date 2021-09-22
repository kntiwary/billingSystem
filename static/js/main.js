    $(document).ready(function(){

        $(".btn").click(function(){

            console.log("hello")



                    $.ajax({
                        type: "GET",
                        dataType: "json",
                        url:"http://127.0.0.1:8000/temp/1/details/",
                        success: function(data)
                        {
                            alert("i got data now i will parse it as i want to display it");
                        },

                       })

        });
    });


//$(document).ready(function (e) {
//
//    $('#A').click(function (e) { //Default mouse Position
//        alert(e.pageX + ' , ' + e.pageY);
//                    $.ajax({
//                        type: "GET",
//                        dataType: "json",
//                        url:"/1/details/",
//                        success: function(data)
//                        {
//                            alert("i got data now i will parse it as i want to display it");
//                        },
//
//                       })
//
//
//    });
//});
