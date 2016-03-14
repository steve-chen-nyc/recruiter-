'use strict'

$(function(){

    $("#typed").typed({
        stringsElement: $('#typed-strings'),
        cursorChar: "",
    });


    $(document).on('click', function(){
      $('#typed').hide();
    })

  $('#Container').mixItUp({
    animation: {
      effects: 'fade translateX(100%)',
  		reverseOut: false
    }

  });

  let renderTemplate_show_companies = Handlebars.compile($('template#company-template').html());

  $.ajax({
    url:"/company",
    method:"GET",
  }).done((data) => {
    let company = data.results;
    showCompany(company);
  })

  let showCompany = (data) => {
    let results = $('.result');
    let compiledTemplate = renderTemplate_show_companies({companies: data});
    results.html('').append(compiledTemplate)
  }
});
