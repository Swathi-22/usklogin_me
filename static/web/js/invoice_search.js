
  $('#search').keyup(function () {
    var invoice_search_key = $('#search').val()
    // alert(this.value)
    if (invoice_search_key != '') {
      var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
      $.ajax({
        url: '/seacrch-invocie/',
        type: 'POST',
        data: {
          'invoice_search_key': invoice_search_key,
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
