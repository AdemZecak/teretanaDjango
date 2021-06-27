/*------------------
        PROGRESS BAR
    --------------------*/


    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    let checked = document.querySelectorAll('input:checked');
    let percentage = checked.length / checkboxes.length;
    const progress = document.querySelector('.progress');
    
    checkboxes.forEach(function(checkbox){
        checkbox.addEventListener( 'click', function(){
            checked = document.querySelectorAll('input:checked');
            percentage = (checked.length / checkboxes.length) * 100;
            progress.style.width = percentage + '%';
        } );
    });
