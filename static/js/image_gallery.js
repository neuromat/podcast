$(document).ready(function(){
    let currentImageIndex = 0;
    let images = $('.post-gallery-item');

    if(images.length === 0){
        $('#imageGalleryTitle').hide();
    }

    let imageContainer = $('#imgContainer');
    let imageCredits = $('#photoCredits');
    let modal = $('#exampleModal');

    // next and previus image control
    $('#next, #prev').click(function(e){
        switchImageControl(e.target.id);
    });

    // single image display function
    $('.post-gallery-item').click((e) => {
        let currentImage = $(e.target).attr('src');
        let creditsInfo = $(e.target).attr('title');
        let id = $(e.target).attr('id');

        currentImageIndex = id.substr(id.length - 1);
        imageContainer.css('background-image', `url('${currentImage}'`);
        imageCredits.html(creditsInfo);
        modal.modal('show');
    });

    // Change image displayed by gallery
    function switchImage(url){
        $('#imgContainer').css('background-image', `url('${url}'`);
    }

    // Control of image change sequence
    function switchImageControl(caller){
        if(caller === 'next'){
              if(currentImageIndex !== images.length - 1){
                  currentImageIndex++;
                  // set new image
                  let newsrc = $('#image'+currentImageIndex).attr('src');
                  switchImage(newsrc);
              }
              return
        }

        // caller was prev btn, check gallery number limit.
        if(parseInt(currentImageIndex) !== 0){
            currentImageIndex--;
            // Setando nova imagem no display
            let newsrc = $('#image'+currentImageIndex).attr('src');
            switchImage(newsrc);
        }
    }

    // Sequential image gallery
    images.map( (index, el) => {
        $(el).attr('id', 'image'+index);
    });
});