jQuery(document).ready(function($) {
    // Check license when clicking import buttons
    $(document).on('click', '.ocdi__gl-item-button', function(e) {
        if (!envatoVerification.verified) {
            e.preventDefault();
            e.stopImmediatePropagation();
            
            // Show our popup
            $('#envato-ocdi-verification-popup').addClass('active');
            
            // Prevent OCDI's default popup
            return false;
        }
    });
    
    // Close popup
    $(document).on('click', '.envato-ocdi-popup-close', function(e) {
        e.preventDefault();
        $('#envato-ocdi-verification-popup').removeClass('active');
    });
    
    // Close when clicking outside content
    $(document).on('click', '#envato-ocdi-verification-popup', function(e) {
        if ($(e.target).is('#envato-ocdi-verification-popup')) {
            $(this).removeClass('active');
        }
    });
    
    // Prevent keyboard shortcuts from bypassing verification
    $(document).on('keydown', function(e) {
        if (!$('#envato-ocdi-verification-popup').hasClass('active')) return;
        
        // Prevent Escape key from closing our popup
        if (e.key === 'Escape') {
            e.preventDefault();
            e.stopImmediatePropagation();
        }
    });

    // Add this to ocdi-popup.js
    function checkVerificationStatus() {
        $.ajax({
            url: envatoVerification.ajaxurl,
            type: 'POST',
            data: {
                action: 'envato_check_verification'
            },
            success: function(response) {
                if (response.data.verified) {
                    // If verified, remove the popup and allow imports
                    $('#envato-ocdi-verification-popup').remove();
                    $('.ocdi__gl-item-button').off('click');
                }
            }
        });
    }

    // Check verification status periodically
    setInterval(checkVerificationStatus, 5000);
});
