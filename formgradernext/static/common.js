$(function() {
    $('.col-md-2 .page-header h1').text('Grader Console (beta)');
    var formGraderPathNext = window.location.origin + '/formgradernext';
    if (window.location.pathname === '/tree' && $('a[href="' + formGraderPathNext + '"]').length === 0) {
        $("#tabs").append(
            $('<li>')
            .append(
                $('<a>')
                .attr('href', formGraderPathNext)
                .attr('target', '_blank')
                .text('Grader Console (beta)')
            )
        );
    }
});
