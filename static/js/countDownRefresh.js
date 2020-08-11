function progress(timeleft, timetotal, $element) {
  var progressBarWidth = timeleft * $element.width() / timetotal;
  $element
      .find('div')
      .animate({ width: progressBarWidth }, timeleft == timetotal ? 0 : 1000, "linear")
      .html(timeleft + " seconds till new code");
  if(timeleft > 0) {
      setTimeout(function() {
          progress(timeleft - 1, timetotal, $element);
  }, 1000);
  }
  else {
    $.ajax({
      url: "/_get_code/",
      success: function(data){
        timeVal = parseInt(JSON.stringify(data['timeLeft']));
        authVal = (JSON.stringify(data['code'])).split("\"").join("");
        $('#timeCode').html(timeVal);
        $('#authCode').val(authVal);
        var timeVar = timeVal;
        progress(timeVar, timeVar, $('#progressBar'));
      }
    });
  }
};
var timeVar = parseInt($('#timeCode').text());
progress(timeVar, timeVar, $('#progressBar'));
