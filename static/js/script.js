/* document script */
$(document).ready(function(){
    /* Mobile sidenav script */
    $('.sidenav').sidenav({edge:"right"});
    
    /* set collapsible popup */
    $('.collapsible').collapsible();
    
    /* character countr */
    $('input#input_text, textarea#textarea1').characterCounter();

    /* datepicker function */
    $('.datepicker').datepicker({
      format: "dd mmm, yyyy",
      yearRange: 3,
      showClearBtn: true,
      i18n:{
        done: "Select"
      }
    });
  });