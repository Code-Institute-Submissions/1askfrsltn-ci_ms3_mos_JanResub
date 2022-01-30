/* document script */
$(document).ready(function(){
    /* Mobile sidenav script */
    $('.sidenav').sidenav({edge:"right"});
    
    /* set collapsible popup */
    $('.collapsible').collapsible();
    
    /* character counter */
    $('input#input_text, textarea#textarea2').characterCounter();

    /* datepicker function */
    $('.datepicker').datepicker({
      format: "dd-mm-yyyy",
      setDefaultDate: true,
      yearRange: 1,
      showClearBtn: true,
      i18n:{
        done: "Select"
      }
    });
    
    /* select form list for input field */
    $('select').formSelect();

    /*scrollspy function*/
    $('.scrollspy').scrollSpy({
      scrollOffset:400
    });   
  });