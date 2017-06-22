$(document).ready(function() {
    $('#edit_form').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            ip: {
                validators: {
                    notEmpty: {
                      message:'请填写主机IP地址！'
                    }
                }
            }
        }
    });
});


