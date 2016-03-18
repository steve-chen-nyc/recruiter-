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

  var renderTemplate_show_companies = Handlebars.compile($('template#company-template').html());

  $.ajax({
    url:"/company",
    method:"GET",
  }).done(function(data){
    var company = data.results;
    showCompany(company);
  })

  var showCompany = function(data){
    var results = $('.result');
    var compiledTemplate = renderTemplate_show_companies({companies: data});
    results.html('').append(compiledTemplate)
  }
});
