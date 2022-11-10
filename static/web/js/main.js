// =================== new_service
$(document).ready(function () {

    // required elements
    var imgPopup = $('.img-popup');
    var imgCont = $('.container__img-holder');
    var popupImage = $('.img-popup img');
    var closeBtn = $('.close-btn');

    // handle events
    imgCont.on('click', function () {
        var img_src = $(this).children('img').attr('src');
        imgPopup.children('img').attr('src', img_src);
        imgPopup.addClass('opened');
    });

    $(imgPopup, closeBtn).on('click', function () {
        imgPopup.removeClass('opened');
        imgPopup.children('img').attr('src', '');
    });

    popupImage.on('click', function (e) {
        e.stopPropagation();
    });

});


// ======================sidebar


$(document).ready(function () {
    $("#demo").addClass('main-panel-marg')
})
$("#test").click(function () {
    $("#demo").toggleClass('main-panel-marg')
    $("#demo2").toggleClass('content-div')

});



// ============== Support request form

$(document).on('submit', 'form.ajax', function (e) {
    e.preventDefault();
    var $this = $(this);
    var data = new FormData(this);
    var action_url = $this.attr('action');
    var reset = $this.hasClass('reset');
    var reload = $this.hasClass('reload');
    var redirect = $this.hasClass('redirect');
    var redirect_url = $this.attr('data-redirect');

    $.ajax({
        url: action_url,
        type: 'POST',
        data: data,
        cache: false,
        contentType: false,
        processData: false,
        dataType: "json",

        success: function (data) {

            var status = data.status;
            var title = data.title;
            var message = data.message;
            var pk = data.pk;

            if (status == "true") {
                if (title) {
                    title = title;
                } else {
                    title = "Success";
                }

                Swal.fire({
                    title: title,
                    html: message,
                    icon: 'success',
                }).then(function () {
                    if (redirect) {
                        window.location.href = redirect_url;
                    }
                    if (reload) {
                        window.location.reload();
                    }
                    if (reset) {
                        window.location.reset();
                    }
                });

            } else {
                if (title) {
                    title = title;
                } else {
                    title = "An Error Occurred";
                }
                Swal.fire({
                    title: title,
                    html: message,
                    icon: "error"
                });

            }
        },
        error: function (data) {
            var title = "An error occurred";
            var message = "something went wrong";
            Swal.fire({
                title: title,
                html: message,
                icon: "error"
            });
        }
    });
});


// ============================FAQ

const toggleBtn = document.querySelectorAll('.toggle-btn');

toggleBtn.forEach(btn => {
    btn.addEventListener('click', () => {
        btn.parentNode.classList.toggle('active')  //only toggles the parent node which is the '.faq-card' here
    })
})




//   ============payment success alert

$('#pay-btn').click(function () { go(50) });
$('#ok').click(function () { go(5000) });

setTimeout(function () { go(50) }, 700);
setTimeout(function () { go(500) }, 2000);

function go(nr) {
    $('.bb').fadeToggle(200);
    $('.message').toggleClass('comein');
    $('.check').toggleClass('scaledown');
    $('#pay-btn').fadeToggle(nr);
}
