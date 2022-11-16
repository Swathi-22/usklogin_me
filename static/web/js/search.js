
  $('#search-tile').keyup(function () {
    var search_Key = $('#search-tile').val()
    // alert(this.value)
    if (search_Key != '') {
      var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
      $.ajax({
        url: '/search/',
        type: 'POST',
        data: {
          'search_Key': search_Key,
          csrfmiddlewaretoken: csrftoken

        },
        success: function (response) {
            console.log(response['template'])
            $('#demo2').empty()
            $('#demo2').append(response['template'])

        }
      })
    }
    else{
        window.location.reload();
    }

  });




  