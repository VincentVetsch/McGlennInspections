$.widget( "ui.timespinner", $.ui.spinner, {
    options: {
        // seconds
        step: 60 * 10000,
        // hours
        page: 60
},

_parse: function( value ) {
    if ( typeof value === "string" ) {
    // already a timestamp
    if ( Number( value ) == value ) {
        return Number( value );
    }
    return +Globalize.parseDate( value );
    }
    return value;
},

_format: function( value ) {
    return Globalize.format( new Date(value), "t" );
    }
});

$(function() {
    $( ".datepicker" ).datepicker();
});

$(function() {
    $( ".spinner" ).spinner({
        spin: function( event, ui ) {
            if ( ui.value > 20 ) {
                $( this ).spinner( "value", 0 );
                return false;
            } else if ( ui.value < 0 ) {
                $( this ).spinner( "value", 20 );
            return false;
            }
        }
    });

    $( ".spinner-footage" ).spinner({
        step: 100,
        spin: function( event, ui ) {
            if ( ui.value > 10000 ) {
                $( this ).spinner( "value", 0 );
                return false;
            } else if ( ui.value < 0 ) {
                $( this ).spinner( "value", 10000 );
            return false;
            }
        }
    });
    $( ".spinner-time").timespinner();
    $( "#culture" ).change(function() {
            var current = $( ".spinner-time" ).timespinner( "value" );
            Globalize.culture( $(this).val() );
        $( ".spinner-time" ).timespinner( "value", current );
    });

});

