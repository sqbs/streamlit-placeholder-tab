
# Placeholder Tab

It makes a tab with a custom page title.

## Bookmarklet

Creates or renames based on the active tab.

```
javascript:(function(){
  var app_url = 'https://placeholder-tab.streamlit.app/';
  if (window.location.href.indexOf(app_url) > -1) {
    var message = 'Rename tab?';
    var target = '_parent';
  } else {
    var message = 'Enter a name for your tab';
    var target = '_blank';
  }
  var tab_name = prompt(message);
  if (tab_name) window.open(`${app_url}?title=${tab_name}`, target);
})();
```
