$(document).ready(function() {
    $('#create_form').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            create_hostname: {
                message: '主机名无效',
                validators: {
                    notEmpty: {
                        message: '主机名不能为空'
                    },
                    stringLength: {
                        min: 3,
                        max: 30,
                        message: '主机名的长度在3和30之间'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z0-9_]+$/,
                        message: '主机名只能由字母、数字和下划线'
                    }
                }
            },
            create_ip: {
                validators: {
                    notEmpty: {
                      message:'请填写主机ip！'
                    }
                }
            }
        }
    });
});

