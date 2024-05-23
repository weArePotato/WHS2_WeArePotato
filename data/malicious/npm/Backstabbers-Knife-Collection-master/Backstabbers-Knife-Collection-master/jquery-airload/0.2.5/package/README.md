

Usage:

```
$(function(){
    $.airloadSetup(window.document, {
      success: function(){
        console.info('success'); 
      },
      start: function(){
        console.info('start');
      },
      error: function(){
        console.info('error');
      },
      complete: function(){
        console.info('complete');
      }
    });
})
```