$(function(){
    if ($('#dropdownId').children('option:selected').val() == undefined) {
      $('#addFormButton').attr('disabled', true);
    }  
  $('#addFormButton').click(function(){
  console.log('here')
  var donationTarget = '{{ studio_member.id }}'  //i know that i will have problems with this in the future
  var donationSource = $('#dropdownId').children('option:selected').val()
  console.log(donationTarget)
  console.log(donationSource)
  var data = {
          donation_target: donationTarget,
          donation_source: donationSource,
          amount: $('#amountInput').val(),
          description: $('#descriptionInput').val(),
              }
              
  $.ajax({
    url: "/donation/",
    type: 'POST',
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(data),
    success: function(response){
      console.log(data);
      console.log(response);
    },
    error: function(error){
    }
  });
  });
});