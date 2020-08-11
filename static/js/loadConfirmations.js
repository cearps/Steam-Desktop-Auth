function loadConfirmations() {
  var x = document.getElementById("loader");
  x.style.display = "block"; // Show loader
  var x = document.getElementById("confirmationDiv");
  x.style.display = "block";
  $.ajax({
    url: "/_send_confirmations/",
    success: function(output){
      $("#confirmations").html(output)
      var x = document.getElementById("loader");
      x.style.display = "none"; // Hide loader
    }
  });
}

function acceptConfirmations(){
  var x = document.getElementById("loader");
  x.style.display = "block"; // Show loader
  var checkedCheckers = [];
  $.each($("input[name='confirmationChecker']:checked"), function(){
    checkedCheckers.push($(this).val());
  });
  if(checkedCheckers && checkedCheckers.length){ // check that at least one item is selected
    $.ajax({
      type: "POST",
      url: "/_accept_confirmations/",
      data: {"data": checkedCheckers},
      dataType: 'json',
      contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
      success: function(output){
        $("#confirmations").html(output)
        var x = document.getElementById("loader");
        x.style.display = "none"; // Hide loader
      }
    });
  } else {
    var x = document.getElementById("loader");
    x.style.display = "none"; // Hide loader
  }
}

function cancelConfirmations(){
  var x = document.getElementById("loader");
  x.style.display = "block"; // Show loader
  var checkedCheckers = [];
  $.each($("input[name='confirmationChecker']:checked"), function(){
    checkedCheckers.push($(this).val());
  });
  if(checkedCheckers && checkedCheckers.length){ // check that at least one item is selected
    $.ajax({
      type: "POST",
      url: "/_cancel_confirmations/",
      data: {"data": checkedCheckers},
      dataType: 'json',
      contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
      success: function(output){
        $("#confirmations").html(output)
        var x = document.getElementById("loader");
        x.style.display = "none"; // Hide loader
      }
    });
  } else {
    var x = document.getElementById("loader");
    x.style.display = "none"; // Hide loader
  }
}
