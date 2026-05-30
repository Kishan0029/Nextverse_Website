// In your admin.js file
jQuery(document).ready(function($) {
    $('#verify-purchase-code').on('click', function(e) {
        e.preventDefault();
        
        var $button = $(this);
        var $result = $('#verification-result');
        var purchaseCode = $('#envato-purchase-code').val();
        
        $button.text(envato_verification_vars.verifying_text).prop('disabled', true);
        $result.removeClass('success error').hide();
        
        $.ajax({
            url: envato_verification_vars.ajaxurl,
            type: 'POST',
            data: {
                action: 'verify_envato_purchase',
                purchase_code: purchaseCode
            },
            dataType: 'json',
            success: function(response) {
                if (response.success) {
                    $result.addClass('success').html(
                        '<p>' + response.data.message + '</p>' +
                        '<div class="client-details-preview">' +
                        '<h4>Client Details</h4>' +
                        '<p><strong>Username:</strong> ' + response.data.client_data.username + '</p>' +
                        '<p><strong>Email:</strong> ' + response.data.client_data.email + '</p>' +
                        '<p><strong>Product:</strong> ' + response.data.client_data.product + '</p>' +
                        '<p><strong>Support Until:</strong> ' + 
                        (response.data.client_data.supported_until ? new Date(response.data.client_data.supported_until).toLocaleDateString() : 'N/A') + 
                        '</p>' +
                        '</div>'
                    ).show();
                    
                    // Reload the page to show full details
                    setTimeout(function() {
                        location.reload();
                    }, 2000);
                } else {
                    $result.addClass('error').html('<p>' + response.data.message + '</p>').show();
                }
            },
            error: function() {
                $result.addClass('error').html('<p>' + envato_verification_vars.error_text + '</p>').show();
            },
            complete: function() {
                $button.text(envato_verification_vars.verify_text).prop('disabled', false);
            }
        });
    });
    
});
