$(document).ready(function(){

    // Enable Carousel Controls
    $(".carousel-control-prev").click(function(){
        $("#carouselExampleIndicators").carousel("prev");
    });
    $(".carousel-control-next").click(function(){
        $("#carouselExampleIndicators").carousel("next");
    });
});

$("#carouselExampleIndicators").on('slide.bs.carousel', function(event){
   if (event.to === 0) {
     $("#img-name").text("Me in my car!");
     $("#location").text("Las Vegas, NV");
   } else if (event.to === 1) {
     $("#img-name").text("Hidden Beauties");
     $("#location").text("Mt Charleston, Clark County");
   } else if (event.to === 2) {
     $("#img-name").text("My cute lil dog");
     $("#location").text("Las Vegas, NV");
   } else if (event.to === 3) {
    $("#img-name").text("A pretty view of Athens");
    $("#location").text("Athens, Greece");
  }
    else if (event.to === 4) {
    $("#img-name").text("The Sistine Chapel");
    $("#location").text("Vatican City");
  } else if (event.to === 5) {
    $("#img-name").text("On the hill, a picture of Athens");
    $("#location").text("Athens, Greece");
  } else if (event.to === 6) {
    $("#img-name").text("Pre-covid rustle and bustle in Athens");
    $("#location").text("Athens, Greece");
  } else if (event.to === 7) {
    $("#img-name").text("La Sagrada Familia");
    $("#location").text("Barcelona, Spain");
  }
});

