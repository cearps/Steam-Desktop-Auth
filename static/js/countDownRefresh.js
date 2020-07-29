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
    location.reload();
  }
};
var timeVar = parseInt($('#timeCode').text());
progress(timeVar, timeVar, $('#progressBar'));
