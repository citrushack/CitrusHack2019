var countDownDate = new Date("April 28, 2019 09:00:00").getTime();var x = setInterval(function() {var now = new Date().getTime();var distance = countDownDate - now;var days = Math.floor(distance / (1000 * 60 * 60 * 24));var hours = Math.floor((distance / (1000 * 60 * 60)));var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));var seconds = Math.floor((distance % (1000 * 60)) / 1000);if(hours < 0){hours = "00";} else if(hours < 10){hours = "0" + hours;}if (minutes < 0) {minutes = "00";} else if(minutes < 10) {minutes = "0" + minutes;} if (seconds < 0) {seconds = "00";} else if(seconds < 10) {seconds = "0" + seconds;} document.getElementById("timer").innerHTML = hours + ":" + minutes + ":" + seconds;}, 1000)

$( ".navlink" ).click(function() {
    var links = document.getElementsByTagName('li');
    
    for (i = 0; i < links.length; i++) {
        links[i].classList.remove('active')
    }

    $(this).addClass("active");

});

$( "#home-link" ).click(function() {
    $('.section-container').addClass('hidden');
    $('#home').removeClass('hidden');
});

$( "#home-icon" ).click(function() {
    $('.section-container').addClass('hidden');
    $('#home').removeClass('hidden');
});

$( "#sched-link" ).click(function() {
    $('.section-container').addClass('hidden');
    $('#schedule').removeClass('hidden');
});

$( "#schedule-icon" ).click(function() {
    $('.section-container').addClass('hidden');
    $('#schedule').removeClass('hidden');
});

$( "#map-link" ).click(function() {
    $('.section-container').addClass('hidden');
    $('#map').removeClass('hidden');
});

$( "#map-icon" ).click(function() {
    $('.section-container').addClass('hidden');
    $('#map').removeClass('hidden');
});

$( "#resources-link" ).click(function() {
    $('.section-container').addClass('hidden');
    $('#resources').removeClass('hidden');
});

$( "#resources-icon" ).click(function() {
    $('.section-container').addClass('hidden');
    $('#resources').removeClass('hidden');
});

$( "#judging-link" ).click(function() {
    $('.section-container').addClass('hidden');
    $('#judging').removeClass('hidden');
});

$( "#judging-icon" ).click(function() {
    $('.section-container').addClass('hidden');
    $('#judging').removeClass('hidden');
});

$( "#expo-link" ).click(function() {
    $('.section-container').addClass('hidden');
    $('#expo').removeClass('hidden');
});