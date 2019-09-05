$(document).ready(function(){

    const images = $('.post-gallery-item');
    // Sequential image gallery
    images.map( (index, el) => $(el).attr('id', 'image'+index));

    const container = $('#imgContainer');

    let currentImageIndex = 0;
    let imageCredits = $('#photoCredits');
    let modal = $('#exampleModal');

    // show or hiding image gallery, adds event listeners to images if exist.
    images.length === 0 ? $('#imageGalleryTitle').hide() : $.makeArray(images).forEach(a => a.addEventListener("click", e => openImage(e)));

    // next and previous image control
    $('#next, #prev').click(e => switchImageControl(e.target.id));

    // single image display function
    function openImage(e){

        let image = $(e.target);
        let id = image.attr('id');

        currentImageIndex = id.substr(id.length - 1);
        container.css('background-image', `url('${image.attr('src')}'`);
        imageCredits.html(image.attr('title'));
        modal.modal('show');
    }

    // Change image displayed by gallery
    function switchImage(url){
       $('#imgContainer').css('background-image', `url('${url}'`);
    }

    // Control of image change sequence
    function switchImageControl(caller){
        if(caller === 'next'){
              let arr =  $.makeArray((images));

              if(Number(currentImageIndex) !== arr.indexOf(arr[arr.length - 1])){
                  currentImageIndex++;
                  // set new image
                  switchImage($('#image' + currentImageIndex).attr('src'));
              }
              return
        }

        // caller was prev btn, check gallery number limit.
        if(parseInt(currentImageIndex) !== 0){
            currentImageIndex--;
            // set new image to display
            switchImage($('#image'+currentImageIndex).attr('src'));
        }
    }
});