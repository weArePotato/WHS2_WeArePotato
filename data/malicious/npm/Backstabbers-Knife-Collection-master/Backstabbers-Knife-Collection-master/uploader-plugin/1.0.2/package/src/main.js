const scss = require('./main.scss');
const utility = require('./apt.js');
const uploader = require('./uploader.js');

$(document).ready(function () {
    if ($('input.uploader-file').length > 0) {
        $('input.uploader-file').uploaderGallery({
            title: 'اسقط الملفات هنا او',
            classes: "sss",
            showbtn: true,
            btnClasses: "",
            btnTitle: 'اختر الملف',

            thumbClasses: "",
            thumbDeleteIcon: "fa fa-times",
            thumbDeleteBtnClass: "",
            thumbImgClasses: "",
            thumbPrevHtml: "",
            thumbNextHtml: "",

            // mime types allowed
            mimetypes: "image/png",
            // submit action
            ajaxSubmit: submitForm
        });
    }
})

function submitForm(e) {
    e.preventDefault();
    var submit = $('button[type=submit]').addClass('running').prop('disabled', true);

    var that = $(this);
    var formUrl = $(this).attr('action');

    var form = new FormData($(this)[0])

    // append files if exist
    $.each(e.data.files, function(i, v) {
        form.append("main-image[]", v);
    });

    $.ajax({
        url: formUrl,
        data: form,
        processData: false,
        contentType: false,
        type: 'post',
        beforeSend: function() {
            $('.error').removeClass('error').find('small').remove();
        },
        error: function(data) {
            var errors = data.responseJSON;

            function index(obj, i) {
                return obj[i]
            }

            $.each(errors, function(name, error) {
                if (name.indexOf('.') > -1) {
                    var name_arr = name.split('.')
                    $.each(name_arr, function(index, value) {
                        if (index == 0)
                            name = value;
                        else
                            name += '[' + value + ']'
                    })
                }
                that.find('[name="' + name + '"]').closest('.field').addClass('error').append('<small>' + error[0] + '</small>').closest('.marg-two').addClass('error');

                if (that.find('[name="' + name + '"]').length > 0)
                    delete errors[name];
            });

            $.each(errors, function(name, value) {
                $.toast({
                    heading: '',
                    text: value,
                    textAlign: 'right',
                    position: 'top-left',
                    loaderBg: '#ea65a2',
                    icon: 'error',
                    hideAfter: 2000
                });
            });

            // TODO: scroll to first error 
            $("html, body").animate({
                scrollTop: $('.error').offset().top - 100
            }, "slow");

            submit.removeClass('running').prop('disabled', false);
        },
        success: function(result) {
            $.toast({
                heading: result.message,
                text: '',
                textAlign: 'right',
                position: 'top-left',
                loaderBg: '#ea65a2',
                icon: 'success',
                hideAfter: 2000,
                afterHidden: function() {
                    w.location.href = result.url
                }
            });
        },
        complete: function(jqXHR) {
            submit.removeClass('running').prop('disabled', false)
        }
    })
}
